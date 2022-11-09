import json
import os


def choose_dish():
    pass


def add_dishes(dish: str, kind: str, practice: str):
    # 读取json文件中的数据
    item_list = []
    with open('dishes.json', 'r', encoding='UTF-8') as f:
        load_dict = json.load(f)
        num_item = len(load_dict)
        for i in range(num_item):
            temp_dish = load_dict[i]['dish']
            temp_kind = load_dict[i]['kind']
            temp_practice = load_dict[i]['practice']
            temp_item = {'dish': temp_dish, 'kind': temp_kind, 'practice': temp_practice}
            item_list.append(temp_item)
    # 在末尾添加本次新增的菜式
    new_item = {'dish': dish, 'kind': kind, 'practice': practice}
    item_list.append(new_item)
    with open('dishes.json', 'w', encoding='UTF-8') as f:
        json.dump(item_list, f, ensure_ascii=False)
