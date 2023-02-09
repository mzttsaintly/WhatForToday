<script setup lang="ts">
import { ref } from 'vue'

const meat = ref('')

const vegetable = ref('')

const spices = ref('')

const process = ref([])
</script>

<template>
    <div class="show">
        <div class="materials">
            <p class="meat">{{ meat }}</p>
            <p class="vegetable">{{ vegetable }}</p>
            <p class="spices">{{ spices }}</p>
        </div>
        <div class="process">
            <li v-for="(item, index) in process" :key="index">
                {{ item }}
            </li>
        </div>
    </div>
</template>

<style>
body {
    margin: 0;
}
.editor {
    height: 100vh;
    display: flex;
}
.input, .output {
    overflow: auto;
    width: 50%;
    height: 100%;
    box-sizing: border-box;
    padding: 0 20px;
}
.input {
    border: none;
    border-right: 1px solid #ccc;
    resize: none;
    outline: none;
    background-color: #f6f6f6;
    font-size: 14px;
    font-family: 'Monaco' courier monospace;
    padding: 20px;
}
code {
    color: #f66;
}
</style>