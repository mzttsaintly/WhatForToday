from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from loguru import logger

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Z:/WhatForToday/backEnd/dishes.db"
app.config["JSON_AS_ASCII"] = False
db.init_app(app)


class Dishes(db.Model):
    __tablename__ = "Dishes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    material = db.Column(db.JSON)
    quantity = db.Column(db.JSON)
    operate = db.Column(db.JSON)
    tips = db.Column(db.JSON)


with app.app_context():
    db.create_all()
    logger.debug("正在创建表")


@app.route("/")
def hello():
    return "<a href=‘http://127.0.0.1:5000/add_dishes’>this</a>"


@app.route("/add_dishes", methods=['POST'])
def add_dishes():
    # 接受数据
    material = request.json.get('material')
    quantity = request.json.get('quantity')
    operate = request.json.get('operate')
    tips = request.json.get('tips')
    # 写入
    db.session.add(Dishes(material=material, quantity=quantity, operate=operate, tips=tips))
    db.session.commit()
    res = jsonify(material=material, quantity=quantity, operate=operate, tips=tips)
    return res


@app.route("/query_dishes", methods=['POST'])
def query_dishes():
    # 查询条件
    material_in_dishes = request.json.get('material_in_dishes')
    quantity_in_dishes = request.json.get('quantity_in_dishes')

