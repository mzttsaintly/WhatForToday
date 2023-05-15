<script setup>
import { ref, reactive } from 'vue'
import axios from "axios";
const test_url = ref('http://127.0.0.1:5000/add_dishes')
const new_name = ref("")
const new_material = ref("")
const new_quantity = ref("")
const new_operate = ref("")
const new_tips = ref("")

const vFocus = {
  mounted: (el) => el.focus()
}

const new_dish = reactive({
    "name": new_name,
    "material": new_material,
    "quantity": new_quantity,
    "operate": new_operate,
    "tips": new_tips
})

function submit_dish() {
    axios.post(test_url.value, new_dish).then(function (res) {
        console.log(res)
    })
    
}

const new_material_array = reactive([{data:""}])
const new_quantity_array = reactive({})
const new_operate_array = reactive({})
const new_tips_array = reactive({})

// 材料栏
function delete_material_input(item) {
    if (new_material_array.length<=1) {
        return false;
    }
    new_material_array.splice(new_material_array.indexOf(item), 1)
}

function add_material_input() {
    this.new_material_array.push({data:""})
}

function merge_material() {
    let msg = ""
    for (let m of new_material_array) {
        msg += m.data;
        msg += ';'
    }
    console.log(msg)
    return msg
}
</script>

<template>
    <form class="add" :action="test_url" method="post">
        <div class="name">
            <label for="name" class="name">输入名字：</label>
            <input type="text" class="name" v-model="new_name">
            <p>{{ new_name }}</p>
        </div>

        <div class="material">
            <label for="material" class="material">输入材料，不同材料以分号(;)分隔：</label>
            <input type="text" class="material" v-model="new_material">
            <p>{{ new_material }}</p>
        </div>

        <div class="quantity">
            <label for="quantity" class="quantity">输入数量，以分号(;)分隔：</label>
            <input type="text" class="quantity" v-model="new_quantity">
            <p>{{ new_quantity }}</p>
        </div>

        <div class="operate">
            <label for="operate" class="operate">输入操作步骤，以分号(;)分隔：</label>
            <input type="text" class="operate" v-model="new_operate">
            <p>{{ new_operate }}</p>
        </div>

        <div class="tips">
            <label for="tips" class="tips">输入注意事项：</label>
            <input type="text" class="tips" v-model="new_tips">
            <p>{{ new_tips }}</p>
        </div>

        <div class="submit">
            <input type="button" class="submit" value="提交" @click="submit_dish">
        </div>
    </form>

    <div class="new">
        <div class="material" v-for="item in new_material_array" :key="item.id">
            <el-input type="input" placeholder="输入所需材料" v-model="item.data" v-focus></el-input>
            <el-button type="danger" @click="delete_material_input(item)">-</el-button>
        </div>
        <el-button type="primary" @click="add_material_input()">+</el-button>
        <el-button type="success" @click="merge_material">提交</el-button>
    </div>
</template>