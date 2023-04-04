# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from loguru import logger
import os

from sqlalchemy.engine.row import Row

basedir = os.path.abspath(os.path.dirname(__name__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "backEnd", "dishes.db")
logger.debug(app.config["SQLALCHEMY_DATABASE_URI"])
app.config["JSON_AS_ASCII"] = False
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy()
db.init_app(app)


class Dishes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    material = db.Column(db.JSON)
    quantity = db.Column(db.JSON)
    operate = db.Column(db.JSON)
    tips = db.Column(db.JSON)
    # material = db.Column(db.String)
    # quantity = db.Column(db.String)
    # operate = db.Column(db.String)
    # tips = db.Column(db.String)


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
    logger.debug(res)
    return res


@app.route("/query_material", methods=['POST'])
def query_dishes_by_material():
    # 查询条件
    material = request.json.get('material')
    t = f"%{material}%"
    logger.debug(t)
    # dishes = db.first_or_404(db.select(Dishes).order_by(Dishes.material))
    dishes = db.first_or_404(db.select(Dishes).filter(Dishes.material.like(t)))
    res = {"material": dishes.material, "quantity": dishes.quantity, "operate": dishes.operate, "tips": dishes.tips}

    return jsonify(res)
