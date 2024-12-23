<template>
  <div  class="background">
    
  <KCol>
    <KCell><KCell><div class="background_style1" style="height: 100px; width: 100%;text-align: center;display: flex; justify-content: center; align-items: center; color: white;">
  欢迎您来到IMIS系统！
</div></KCell></KCell>
    <KCell>

              <KCol>
                <KRow>
                  <KCell>
                    <KCell><div style="height: 20px; width: 100%;text-align: center;display: flex; justify-content: center; align-items: center; color: white;">

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
        <KCell style="height: 100%; width: 100px;text-align: center;display: flex; justify-content: center; align-items: center; color: white;"></KCell>
        
  <KCell>
    <KCell><div style="height: 100px; width: 100%;text-align: center;display: flex; justify-content: center; align-items: center; color: white;">

</div></KCell>
    <el-timeline>
      <el-timeline-item timestamp="2024-11-20">
      <el-card style="width:700px;">
        <h4>项目启动</h4>
        <p>小组正式成立，新建文件夹完毕。商讨大作业题目为结合大模型诊疗的医院信息系统。</p>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="2024-11-25">
      <el-card style="width:700px;">
        <h4>概念设计</h4>
        <p>通过共同商讨后，确定了大概的系统架构，并开始进行概念设计。完成了数据流图和功能描述。小组成员为了更好地做出系统，和在医院任职的家人沟通，以求做出效果更好的设计。</p>
        <el-button type="primary">操作按钮</el-button>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="2024-11-28">
      <el-card style="width:700px;">
        <h4>提交初步报告</h4>
        <p>小组成员完成初步的进度进展报告并提交。</p>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="2024-12-10">
      <el-card style="width:700px;">
        <h4>logo与名称</h4>
        <p>我们将我们的数据库系统命名为：integrative medical intelligence system，简称为IMIS。我们希望我们的系统将“综合”，“”智能””医疗”“信息”“系统”融合在一起。同时我们设计了一个logo。</p>
        <el-image src="/pictures/Canva Middle School (2).png" alt="示例图片"></el-image>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="2024-12-12">
      <el-card style="width:700px;">
        <h4>正式启动</h4>
        <p>项目正式启动，我们选择国产数据库系统金仓进行开发。小组成员部署了kesplus框架。创建github仓库进行协作开发。</p>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="2024-12">
      <el-card style="width:700px;">
        <h4>开发过程</h4>
        <p>全力开发中……</p>
        <el-image style = "height: 300px" src="/pictures/work.jpg" alt="示例图片"></el-image>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="2024-12">
      <el-card style="width:700px;">
        <h4>Done!</h4>
        <p>呵，长大了！<br>经过将近两个月的设计开发工作, IMIS终于完成了!git的版本记录中,存放了我们124次提交记录,累计修改约20000行代码,实现了医院信息系统的基本功能。从11月中旬到12月下旬,我们终于完成了本项目的开发,并且对基本功能完成了测试。<br>完结撒花!</p>
      </el-card>
    </el-timeline-item>
    </el-timeline><div style="height: 100px; width: 100%;text-align: center;display: flex; justify-content: center; align-items: center; color: white;">

</div>
    </KCell>
  

</KRow>
                
              </KCol>
    </KCell>
    <KCell>
      <KCell><div class="background_style1" style="position: fixed; bottom: 0; left: 0; width: 100%; height: 100px; text-align: center; display: flex; justify-content: center; align-items: center; color: white;">
  地址：陕西省西安市长安区西北工业大学计算机学院 邮编：xxxxxx <br>本项目使用素材均来源于网络，如有侵权请联系本人删除
</div></KCell>
</KCell>
  </KCol>
      <div>
    
    
  </div>  
      </div>
</template>
<script setup>
import { defineRouteMeta, KDashboard } from "@kesplus/kesplus";


import { useRouter, useRoute } from "@@/core/coreExports";
const router = useRouter();
function navigateTo() {
  router.push({ path: "/patient_view" });
}
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