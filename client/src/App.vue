<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<template>

  <header class="p-3 bg-dark text-white">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <RouterLink to="/" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
          <img class="bi me-2" width="100" height="50" role="img" aria-label="GreenTown" src="@/assets/img/logo_green_town.png" alt="logo" />
        </RouterLink>

        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
          <li><RouterLink to="/" class="nav-link px-2 text-white">[ Карта ]</RouterLink></li>
          <li><RouterLink to="/list_trees" class="nav-link px-2 text-white">[ Список ]</RouterLink></li>
          <li><RouterLink to="/filter_trees" class="nav-link px-2 text-white">[ Фильтр ]</RouterLink></li>
        </ul>

        <div class="text-end">
          <button type="button" class="btn btn-outline-light me-2" onclick="location.href='/admin/';">[ Админка ]</button>
        </div>
      </div>
    </div>
  </header>

  <RouterView />

</template>

<script>
export default {
  name: "App"
}
</script>

<style scoped>

</style>
