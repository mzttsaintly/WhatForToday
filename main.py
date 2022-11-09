import json
from json import JSONEncoder
import os


class Dish:
    def __int__(self, name, kind, time, practice):
        self.name = name
        self.kind = kind
        self.time = time
        self.practice = practice

    def show_practice(self):
        return self.practice


class DishEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def choose_dish(num: int):
    pass


def add_dishes(dish_name: str, kind: str, practice: str):
    # 读取json文件中的数据
    item_list = []
    with open('dishes.json', 'r', encoding='UTF-8') as f:
        load_dict = json.load(f)
        num_item = len(load_dict)
        if num_item != 0:
            for i in range(num_item):
                temp_dish = load_dict[i]['dish_name']
                temp_kind = load_dict[i]['kind']
                temp_practice = load_dict[i]['practice']
                temp_item = {'dish_name': temp_dish, 'kind': temp_kind, 'practice': temp_practice}
                item_list.append(temp_item)
    # 在末尾添加本次新增的菜式
    new_item = {'dish_name': dish_name, 'kind': kind, 'practice': practice}
    item_list.append(new_item)
    with open('dishes.json', 'w', encoding='UTF-8') as f:
        json.dump(item_list, f, ensure_ascii=False)


def alter_dish():
    pass


if __name__ == "__main__":
    print("分开输入菜品名字，种类，制作方法")
    input_name = input()
    input_kind = input()
    input_practice = input()
    add_dishes(input_name, input_kind, input_practice)
