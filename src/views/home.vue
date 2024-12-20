<template>
  <div  class="background">

      
  <KCol>
    <KCell>
    <el-carousel style="width:100%; height:500px; overflow:hidden;" :autoplay="false" @change="handleCarouselChange">
      <el-carousel-item style="width:100%; height:500px; overflow:hidden;">
        <div style="display:flex; justify-content:center; align-items:center; width:100%; height:100%; overflow:hidden;">
      <img src="/pictures/5rr0tedn.png" alt="描述文字1" style=" object-fit:cover;">
    </div>
      </el-carousel-item>
      <el-carousel-item style="width:100%; height:500px; overflow:hidden;">
        <div style="display:flex; justify-content:center; align-items:center; width:100%; height:100%; overflow:hidden;">
      <img src="/pictures/neuy55er.png" alt="描述文字1" style=" object-fit:cover;">
    </div>
      </el-carousel-item>
      <el-carousel-item style="width:100%; height:500px; overflow:hidden;">
        <div style="display:flex; justify-content:center; align-items:center; width:100%; height:100%; overflow:hidden;">
      <img src="/pictures/hospital3.png" alt="描述文字1" style=" object-fit:cover;">
    </div>
      </el-carousel-item>
    </el-carousel>
        </KCell>

    <KCell><el-space wrap></el-space></KCell>
    
                
  <KRow>
   
                  <KCell ><el-calendar  style="width:600px;height:500px;background-color: rgba(255, 255, 255, 0.5);margin-left: 0px;"/>
      </KCell>
                

    

    <KCell class="background">
        <KCell><el-card header="我是卡片" style="width:600px;height:500px;weight:500px;background-color: rgba(255, 255, 255, 0.5);margin-left: 0px;"/></KCell></KCell>
        <KCell >
    
              
        
    
   </KCell></KRow></KCol>
      </div>
</template>
<script setup>
import { defineRouteMeta, KDashboard } from "@kesplus/kesplus";

</script>

<style>
.page {
  height: 1000px;
}
</style>

<style>
.el-calendar {
  margin-left: 50px; /* 这里的20px可以根据需要调整 */
  width: 900px;
  height: 600px;
}
</style>

<style>
.page {
  height: 1000px;
}

.el-calendar {
  margin-left: 50px; /* 这里的20px可以根据需要调整 */
  width: 900px;
  height: 600px;
}

.custom-tabs .el-tabs__nav-wrap::after,
.custom-tabs .el-tabs__nav-scroll {
  height: 500px !important; /* 调整为你想要的高度 */
}

.custom-tabs .el-tabs__item {
  height: 500px !important; /* 调整为你想要的高度 */
  line-height: 500px !important; /* 调整为与高度一致，以垂直居中 */
}
</style>

<style scoped>
.background {
  background-color: #d0d3df;

}
</style>