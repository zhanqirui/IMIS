<template>
    
 <div
    class=" background_style absolute left-0 right-0 top-0 h-20 flex justify-between flex-items-center px-25 <sm:px-8 "
  >
    <div class="flex flex-items-center">
      

      <div class="ml-4 text-5">
        <!-- <span class="ml-1 dark:color-#fff"> {{ model.name + "" }}</span> -->
      </div>
    </div>
    <div class="flex flex-items-center">
    </div>
  
        
            <KText style="color: #ffffff; font-size: 30px; font-family: 'Arial', sans-serif;">欢迎来到IMIS系统！</KText></div> 
            <!-- <img
  src="\pictures\R-C.jpg"
  class="max-h- 24px"
  width="2000" height="1000"
  style="position: absolute; top: 0px; left: 0px;"
  alt="Your Image Description"
     ><div
    class="absolute left-0 right-0 top-0 h-20 flex justify-between flex-items-center px-25 <sm:px-8"
  >
    <div class="flex flex-items-center">
      

      <div class="ml-4 text-5">
        
      </div>
    </div>
    <div class="flex flex-items-center">
    </div>
  </div></img> -->
    
     
</template>

<script setup>
import { useModel } from "@kesplus/kesplus";
defineOptions({
  name: "LoginTop",
});
const model = useModel("@@initialState");
</script>
