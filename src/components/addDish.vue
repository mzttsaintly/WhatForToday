<script setup>
import { ref } from 'vue'
// import axios from "axios";
const test_url = ref('http://127.0.0.1:5000/add_dishes')
const new_dish = ref({})

</script>

<template>
    <form class="add" :action="test_url" method="post">
        <div class="name">
            <label for="name" class="name">输入名字：</label>
            <input type="text" class="name">
        </div>

        <div class="material">
            <label for="material" class="material">输入材料，不同材料以分号(;)分隔：</label>
            <input type="text" class="material">
        </div>

        <div class="quantity">
            <label for="quantity" class="quantity">输入数量，以分号(;)分隔：</label>
            <input type="text" class="quantity">
        </div>

        <div class="operate">
            <label for="operate" class="operate">输入操作步骤，以分号(;)分隔：</label>
            <input type="text" class="operate">
        </div>

        <div class="tips">
            <label for="tips" class="tips">输入注意事项：</label>
            <input type="text" class="tips">
        </div>

        <div class="submit">
            <input type="submit" class="submit" value="提交">
        </div>
    </form>
</template>