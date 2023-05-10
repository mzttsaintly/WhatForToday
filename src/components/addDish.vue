<script setup>
import { ref, reactive } from 'vue'
import axios from "axios";
axios.defaults.baseURL = '/api'
const test_url = ref('http://127.0.0.1:5000/add_dishes')
const new_name = ref("")
const new_material = ref("")
const new_quantity = ref("")
const new_operate = ref("")
const new_tips = ref("")

const new_dish = reactive({
    "name": new_name,
    "material": new_material,
    "quantity": new_quantity,
    "operate": new_operate,
    "tips": new_tips
})

function submit_dish() {
    const res = axios.post('http://127.0.0.1:5000/add_dishes', new_dish)
    console.log(res)
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
</template>