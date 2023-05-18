<script setup>
import { ref, reactive } from 'vue'
import axios from "axios";
const test_url = ref('http://127.0.0.1:5000/add_dishes')

const new_name = ref("")

// const new_dish = reactive({
//     "name": new_name,
//     "material": new_material,
//     "quantity": new_quantity,
//     "operate": new_operate,
//     "tips": new_tips
// })

// function submit_dish() {
//     axios.post(test_url.value, new_dish).then(function (res) {
//         console.log(res)
//     })

// }

const new_material_and_quantity_array = reactive([{ material_name: "", material_quantity: "" }])
const new_operate_array = reactive([{ data: "" }])
const new_tips_array = reactive([{ data: "" }])

// 材料栏
function delete_material_input(item) {
    if (new_material_and_quantity_array.length <= 1) {
        return false;
    }
    new_material_and_quantity_array.splice(new_material_and_quantity_array.indexOf(item), 1)
}

function add_material_input() {
    this.new_material_and_quantity_array.push({ material_name: "", material_quantity: "" })
}

function merge_material() {
    let msg_m = ""
    let msg_q = ""
    for (let m of new_material_and_quantity_array) {
        msg_m += m.material_name;
        msg_m += ';'
        msg_q += m.material_quantity;
        msg_q += ';'
    }
    console.log("material:" + msg_m)
    console.log("quantity:" + msg_q)
    return [msg_m, msg_q]
}

// 操作栏
function delete_operate_input(item) {
    if (new_operate_array.length <= 1) {
        return false;
    }
    new_operate_array.splice(new_operate_array.indexOf(item), 1)
}

function add_operate_input() {
    this.new_operate_array.push({ data: "" })
}

function merge_operate_input() {
    let msg = ""
    for (let m of new_operate_array) {
        msg += m.data;
        msg += ';'
    }
    console.log("operate:" + msg)
    return msg
}

// tips栏
function delete_tips_input(item) {
    if (new_tips_array.length <= 1) {
        return false;
    }
    new_tips_array.splice(new_tips_array.indexOf(item), 1)
}

function add_tips_input() {
    this.new_tips_array.push({ data: "" })
}

function merge_tips_input() {
    let msg = ""
    for (let m of new_tips_array) {
        msg += m.data;
        msg += ';'
    }
    console.log("tips:" + msg)
    return msg
}

// 提交
function post_button() {
    let [material, quantity] = merge_material()
    let operate = merge_operate_input()
    let tips = merge_tips_input()
    console.log("button:" + new_name.value, material, quantity, operate, tips)
    const new_dish = reactive({
        "name": new_name,
        "material": material,
        "quantity": quantity,
        "operate": operate,
        "tips": tips
    })

    function submit_dish() {
        axios.post(test_url.value, new_dish).then(function (res) {
            console.log(res)
        })

    }
}
</script>

<template>
    <div class="new">
        <div class="new_name">
            <el-input type="input" placeholder="输入菜品名称" v-model="new_name"></el-input>
        </div>

        <div class="material-div">
            <div class="kuangkuang" v-for="item in new_material_and_quantity_array" :key="item.id">
                <el-input type="input" placeholder="输入所需材料" v-model="item.material_name"></el-input>
                <el-input type="input" placeholder="输入材料数量" v-model="item.material_quantity"></el-input>
                <el-button type="danger" @click="delete_material_input(item)">-</el-button>
            </div>
            <el-button class="add_button" type="primary" @click="add_material_input()">+</el-button>

        </div>

        <div class="operate-div">
            <div class="kuangkuang" v-for="item in new_operate_array" :key="item.id">
                <el-input type="input" placeholder="输入操作步骤" v-model="item.data"></el-input>
                <el-button type="danger" @click="$event => delete_operate_input(item)">-</el-button>
            </div>
            <el-button type="primary" @click="$event => add_operate_input()">+</el-button>
        </div>

        <div class="tips-div">
            <div class="kuangkuang" v-for="item in new_tips_array" :key="item.id">
                <el-input type="input" placeholder="输入注意事项" v-model="item.data"></el-input>
                <el-button type="danger" @click="$event => delete_tips_input(item)">-</el-button>
            </div>
            <el-button type="primary" @click="$event => add_tips_input()">+</el-button>
        </div>

        <el-button type="success" @click="post_button">提交</el-button>
    </div>
</template>

<style>
.add {
    display: none;
}

.new {
    display: flex;
    flex-direction: row;
    border: 2px;

}

.new.material-div {
    display: flex;
    flex-direction: row;
}

.kuangkuang {
    display: flex;
    flex-direction: row;
    margin: 2px;
}

.add_button {
    align-items: center;
}
</style>