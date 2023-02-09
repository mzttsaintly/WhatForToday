<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import display from './components/display_.vue'
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

  <RouterView />
</template>

<style scoped>

</style>
