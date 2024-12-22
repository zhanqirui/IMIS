<template>
  <div  class="background">
    
  <KCol>
    <KCell><KCell><div class="background_style1" style="height: 100px; width: 100%;text-align: center;display: flex; justify-content: center; align-items: center; color: white;">
  地址：北京市海淀区中关村南大街22号 邮编：100081 总机：010-62179977 预约咨询：010-62179665/ 82195390
</div></KCell></KCell>
    <KCell>

              <KCol>
                <KRow>
                  <KCell>
                    <KCell><div style="height: 100px; width: 100%;text-align: center;display: flex; justify-content: center; align-items: center; color: white;">

</div></KCell>
    <el-popover
        placement="top-start"
        title="Title"
        :width="200"
        trigger="hover"
        content="this is content, this is content, this is content"
      >
        
      </el-popover>
        <el-calendar /></KCell>
        
  <KCell>
    <KCell><div style="height: 100px; width: 100%;text-align: center;display: flex; justify-content: center; align-items: center; color: white;">

</div></KCell>
    <el-timeline>
      <el-timeline-item timestamp="2023-10-1">
      <el-card>
        <h4>标题1</h4>
        <p>这里是一些描述信息。</p>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="2023-11-15">
      <el-card>
        <h4>标题2</h4>
        <p>这里是一些描述信息。</p>
        <el-button type="primary">操作按钮</el-button>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="2023-12-20">
      <el-card>
        <h4>标题3</h4>
        <p>这里是一些描述信息。</p>
        <el-image src="/pictures/Canva Middle School (2).png" alt="示例图片"></el-image>
      </el-card>
    </el-timeline-item>
    </el-timeline>
    </KCell>
  

</KRow>
                
              </KCol>
    </KCell>
    <KCell>
      <KCell><div class="background_style1" style="height: 100px; width: 100%;text-align: center;display: flex; justify-content: center; align-items: center; color: white;">
  地址：北京市海淀区中关村南大街22号 邮编：100081 总机：010-62179977 预约咨询：010-62179665/ 82195390
</div></KCell>
</KCell>
  </KCol>
      <div>
    
    
  </div>  
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
  .text-center {
  text-align: center;
}
}
</style>