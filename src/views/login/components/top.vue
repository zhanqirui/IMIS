<template>
  <img
  src="C:\Users\24941\IMIS\pictures\R-C.jpg"
  class="max-h- 24px"
  width="2000" height="1000"
  style="position: absolute; top: 0px; left: 0px;"
  alt="Your Image Description"
     />
     <img
  src="C:\Users\24941\IMIS\pictures\logi.png"
  class="max-h- 24px"
  width="50" height="50"
  style="position: absolute; top: 20px; left: 30px;"
  alt="Your Image Description"
     />
     <div
    class="absolute left-0 right-0 top-0 h-20 flex justify-between flex-items-center px-25 <sm:px-8"
  >
    <div class="flex flex-items-center">
      

      <div class="ml-4 text-5">
        <span class="ml-1 dark:color-#fff"> {{ model.name + "" }}</span>
      </div>
    </div>
    <div class="flex flex-items-center">
    </div>
  </div><div
    class="absolute left-0 right-0 top-0 h-20 flex justify-between flex-items-center px-25 <sm:px-8"
  >
    <div class="flex flex-items-center">
      

      <div class="ml-4 text-5">
        <span class="ml-1 dark:color-#fff"> {{ model.name + "" }}</span>
      </div>
    </div>
    <div class="flex flex-items-center">
    </div>
  </div><div
    class="absolute left-0 right-0 top-0 h-20 flex justify-between flex-items-center px-25 <sm:px-8"
  >
    <div class="flex flex-items-center">
      

      <div class="ml-4 text-5">
        <span class="ml-1 dark:color-#fff"> {{ model.name + "" }}</span>
      </div>
    </div>
    <div class="flex flex-items-center">
    </div>
  </div><div
    class="absolute left-0 right-0 top-0 h-20 flex justify-between flex-items-center px-25 <sm:px-8"
  >
    <div class="flex flex-items-center">
      

      <div class="ml-4 text-5">
        <span class="ml-1 dark:color-#fff"> {{ model.name + "" }}</span>
      </div>
    </div>
    <div class="flex flex-items-center">
    </div>
  </div>
</template>

<script setup>
import { useModel } from "@kesplus/kesplus";
defineOptions({
  name: "LoginTop",
});
const model = useModel("@@initialState");
</script>
