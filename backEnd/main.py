# -*- coding: utf-8 -*-
from sqlalchemy.exc import IntegrityError
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from loguru import logger
import os
import json

basedir = os.path.abspath(os.path.dirname(__name__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(basedir, "backEnd", "dishes.db")
logger.debug(app.config["SQLALCHEMY_DATABASE_URI"])
app.config["JSON_AS_ASCII"] = False
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy()
db.init_app(app)


class Dishes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)
    material = db.Column(db.String)
    quantity = db.Column(db.String)
    operate = db.Column(db.String)
    tips = db.Column(db.String)


def dish_to_json(dishes: Dishes):
    res = {"name": dishes.name,
           "material": dishes.material,
           "quantity": dishes.quantity,
           "operate": dishes.operate,
           "tips": dishes.tips}
    return jsonify(res)


with app.app_context():
    db.create_all()
    logger.debug("正在创建表")


@app.route("/")
def hello():
    return "<a href=‘http://127.0.0.1:5000/add_dishes’>this</a>"


@app.route("/add_dishes", methods=['POST'])
def add_dishes():
    # 接受数据
    name = request.json.get('name')
    material = request.json.get('material')
    quantity = request.json.get('quantity')
    operate = request.json.get('operate')
    tips = request.json.get('tips')

    # 写入
    try:
        db.session.add(Dishes(name=name, material=material,
                       quantity=quantity, operate=operate, tips=tips))
        db.session.commit()
        res = jsonify(name=name, material=material,
                      quantity=quantity, operate=operate, tips=tips)
        logger.debug(res)
    except IntegrityError:
        return "不可插入重复的条目，请先删除旧条目"
    return res


@app.route("/query_material", methods=['POST', 'GET'])
def query_dishes_by_material():
    # 查询条件
    if request.method == 'POST':
        material = request.json.get('material')
        
    else:
        material = request.args.get('material')
    t = f"%{material}%"
    # first_or_404: 返回第一个对象，若找不到则返回404，参数为查询语句
    # filter：不可组合查询，需连续调用filter函数
    dishes = db.first_or_404(db.select(Dishes).filter(
        Dishes.material.like(t)), description="找不到该菜式")
    res = dish_to_json(dishes)

    return res


@app.route("/query_material_all/", methods=['GET', 'POST'])
def query_dishes_by_material_all():
    # 查询条件
    if request.method == 'POST':
        material = request.json.get('material')
        
    else:
        material = request.args.get('material')
    t = f"%{material}%"
    # first_or_404: 返回第一个对象，若找不到则返回404，参数为查询语句
    # filter：不可组合查询，需连续调用filter函数
    dishes_list = db.session.execute(
        db.select(Dishes).filter(Dishes.material.like(t))).scalars()
    res = []
    for i in dishes_list:
        res.append(dish_to_json(i))
    return res


@app.route("/query_name", methods=['POST', 'GET'])
def query_dishes_by_name():
    if request.method == 'POST':
        dishes_name = request.json.get('name')
        
    else:
        dishes_name = request.args.get('name')
    
    t = f"%{dishes_name}%"
    logger.debug(t)
    dishes = db.first_or_404(db.select(Dishes).filter(
        Dishes.name.like(t)), description="找不到该菜式")
    res = dish_to_json(dishes)
    return res


@app.route("/query_id", methods=['POST', 'GET'])
def query_dishes_by_id():
    if request.method == 'POST':
        dishes_id = request.json.get('id')
        
    else:
        dishes_id = request.args.get('id')
    
    t = int(dishes_id)
    logger.debug(t)
    dishes = db.get_or_404(Dishes, t, description="找不到该菜式")
    res = dish_to_json(dishes)
    return res

@app.route("/random")
def random_dish():
    logger.debug("准备随机条目")
    dishes = db.first_or_404(db.select(Dishes).order_by(db.func.random()).limit(1))
    logger.debug(str(dishes))
    res = dish_to_json(dishes)
    return res


@app.route("/del", methods=['POST'])
def del_by_name():
    dishes_name = request.json.get('name')
    t = f"{dishes_name}"
    logger.debug(t)
    dishes = db.first_or_404(db.select(Dishes).filter(
        Dishes.name == t), description="找不到该菜式")
    db.session.delete(dishes)
    db.session.commit()
    return "已删除"
