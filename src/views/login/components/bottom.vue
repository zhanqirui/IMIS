<!-- eslint-disable vue/no-v-html -->
<template>
  <div
    class="absolute bottom-0 left-0 right-0 h-20 flex justify-between flex-items-center px-25 <sm:px-8"
  >
    
  <div  class="w-full text-center dark:color-#fff" style="color: #ffffff;font-size: 24px;" v-html="copyRight"></div></div>
</template>

<script setup>
import { computed } from "vue";
import { useModel } from "@kesplus/kesplus";
defineOptions({
  name: "LoginBottom",
});
const model = useModel("@@initialState");
const copyRight = computed(() => {
  return model.copyright || "Copy Right @ 西北工业大学IMIS开发团队";
});
</script>
