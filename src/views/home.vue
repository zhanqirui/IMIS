<template>
  <div class="page">

      
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
                  <KCell><el-calendar /></KCell>
                  <KCell>
                    <!-- <div v-html="currentExplanation"></div> -->
                  </KCell>
                </KRow>
  </KCol>
      </div>
</template>
<script setup>
import { defineRouteMeta, KDashboard } from "@kesplus/kesplus";


// defineOptions({
//   name: "UserHome",
// });
// </script>
// <script>
// defineRouteMeta({
//   name: "home",
//   title: "工作台",
//   "keep-alive": true,
//   icon: "HomeFilled",
//   isAffix: true,
// });


// export default {
//   data() {
//     return {
//       items: [
//         { image: '/pictures/5rr0tedn.png', explanation: '解释文本1' },
//         { image: '/pictures/neuy55er.png', explanation: '解释文本2' },
//         { image: '/pictures/hospital3.png', explanation: '解释文本3' },
//       ],
//             currentExplanation: ''
//     };
//   },
//   methods: {
//     handleCarouselChange(newIndex, oldIndex) {
//       // 更新当前解释文本
//       this.currentExplanation = this.items[newIndex].explanation;
//     }
//   }
// };
// </script>

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