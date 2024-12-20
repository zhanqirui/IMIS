<template>
  <div class="page">
    <KDashboard />
  </div>
</template>
<script setup>
import { defineRouteMeta, KDashboard } from "@kesplus/kesplus";
// import { access } from '@kesplus/kesplus';
// import { useRouter, onBeforeMount } from 'vue-router';

// const router = useRouter();

// onBeforeMount(() => {
//   const role = access.getRole();

//   if (role === 'admin') {
//     return router.replace('/patient');
//   } else if (role === 'user') {
//     return router.replace('/user-dashboard');
//   } else {
//     return router.replace('/login');
//   }
// });

defineOptions({
  name: "UserHome",
});
</script>
<script>
defineRouteMeta({
  name: "home",
  title: "工作台",
  "keep-alive": true,
  icon: "HomeFilled",
  isAffix: true,
});
</script>

<style>
.page {
  height: 1000px;
}
</style>
