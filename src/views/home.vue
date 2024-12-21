<template>
  <div  class="background">
    
  <KCol>
    <KCell></KCell>
    <KCell>
<KRow>
  <KCell>
    <el-timeline>
        <el-timeline-item timestamp="2023-10-1">
            <el-text>内容</el-text>
        </el-timeline-item>
    </el-timeline>
    </KCell>
  <KCell><el-card header="我是卡片">
        <KText>文字文字</KText>
            </el-card></KCell>
  <KCell>
    <el-popover
        placement="top-start"
        title="Title"
        :width="200"
        trigger="hover"
        content="this is content, this is content, this is content"
      >
        <template #reference>
          <el-button class="m-2">Hover to activate</el-button>
        </template>
      </el-popover>
        <el-calendar /></KCell>
</KRow>
    </KCell>
    <KCell>
        <el-space wrap></el-space><KP>
        <KText class="text-center">关于我们
招贤纳士
商务合作
寻求报道

400-660-0108

kefu@csdn.net

在线客服
工作时间 8:30-22:00<br>
公安备案号11010502030143
京ICP备19004658号
京网文〔2020〕1039-165号
经营性网站备案信息
北京互联网违法和不良信息举报中心<br>
家长监护
网络110报警服务
中国互联网举报中心
Chrome商店下载
账号管理规范
版权与免责声明
版权申诉
出版物许可证
营业执照<br>
©1999-2024北京创新乐知网络技术有限公司</KText>
            </KP>
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