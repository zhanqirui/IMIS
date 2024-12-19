<template>
  <KPage>
    
  <KSection><KRow>
  <KCell><el-image src="/pictures/zqr.png" style="width: 100px; height: 50px;" /></KCell>
  <KCell>
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        
      <el-card header="您的个人信息" style="width: 1200px; height: 400px;">
        
            
  
      

    
<KRow>
  
  
  
<KText>姓名</KText></KRow><KText>性别</KText><KRow>
  
  
  
<KRow>
  
  
  
<KText>年龄</KText></KRow></KRow><KRow>
  <KCell>
        
            <KText>科室</KText></KCell>
  
  
</KRow><KRow>
  
  
  
<KText>联系电话</KText></KRow><KRow>
  <KCell>
        
            <KText>紧急联系人</KText></KCell>
  
  
</KRow>
    
<KRow>
  <KCell>
        
            <KText>身份证号</KText></KCell>
  
  
</KRow>
    

    </el-card>
        
      </KRow>
    </el-form>
  </KCell>
  

              </KRow>

    </KSection><KSection>
        
<KBlock><KCell>
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        <KCell>
      
   
<KRow>
  
  
  <KCell>
      <el-tooltip
        class="box-item"
        effect="dark"
        content="Top Left prompts info"
        placement="top-start"
      >
        
      </el-tooltip></KCell>
</KRow>
    </KCell>
      </KRow>
    </el-form>
  </KCell>
              <KRow>
                <KCell>
      
      
  <KCol>
    <KCell>
      
      <el-tabs type="border-card">
        <el-tab-pane label="病人一览"></el-tab-pane>
      
<el-tab-pane label="病历一览"></el-tab-pane>


</el-tabs>
    
    </KCell>
    
    
  </KCol>
      </KCell>
                
              </KRow></KBlock></KSection></KPage>
</template>
<script setup>
import { reactive } from 'vue'
const form = reactive({})



const form_1 = reactive({})

import { request, access } from '@kesplus/kesplus'
import { ref, toRef } from "vue";
import { useSelect, useDialogForm } from "@@/plugin-platform/utils/hooks";
const formRef = ref();
const { form:vwfrForm, reset:vwfrReset, submit:vwfrSubmit, closeDialog: vwfrCloseDialog } = useDialogForm({
  // 待编辑数据的id
  id: ref(),
  // 表单模型的Ref, 用于表单校验
  formRef: formRef,
  // 表单默认值
  default: {},
  fetchById: (id) => {
    return request.get('/kes/IMIS/MSDATA/getPatientPastHistory',{ params: { id } });
  },
  save: async (model) => {
    if (model.id) {
      await Promise.resolve({});
    } else {
      await Promise.resolve({});
    }
    vwfrCloseDialog?.()
  },
});

const form_1_1 = reactive({})

const form_1_1_1 = reactive({})

const form_1_1_1_1 = reactive({})
</script>