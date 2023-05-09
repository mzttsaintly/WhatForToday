<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import display from './components/display_.vue'
import addDish from './components/addDish.vue'
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/Display">show</RouterLink>
      </nav>
    </div>
  </header>
  <display />
  <addDish />
  <RouterView />
</template>

<style scoped>

</style>
