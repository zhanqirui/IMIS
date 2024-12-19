.page-margin {
  margin: px;
}

<template>
  <KPage>
    
  <KSection>
<KCell>
          
<el-image src="/pictures/yetou.png" class="page-margin"/>
      <el-tabs type="border-card">
        <el-tab-pane label="User"><KRow>
  <KCell>
  <KCol>
    <KCell><el-image src="/pictures/zqr.png" /></KCell>
    <KCell>
      <KText style="text-align: center; font-family: 'DengXian', sans-serif;;font-size: 20px;">医生画像</KText>
            </KCell>
    
  </KCol>
      </KCell>
  <KCell>
    <el-form ref="formRef" label-width="auto" :model="form" class="page-margin">
      <KRow>
        
      <el-card header="您的个人信息" style="font-size: 24px;width: 1600px; height: 400px;">
        
            
  
      

    

        
      
    

    

    </el-card>
        
      </KRow>
    </el-form>
  </KCell>
  

              </KRow></el-tab-pane>
      
<el-tab-pane label="标签项1">
  <KCol>
    <KCell>
        <KTableBar />
      </KCell>
    <KCell></KCell>
    <KCell></KCell>
  </KCol>
      </el-tab-pane>

<el-tab-pane label="标签项2">
  <KCol>
    <KCell></KCell>
    <KCell></KCell>
    <KCell></KCell>
  </KCol>
      </el-tab-pane>
</el-tabs>
    </KCell>
    

    </KSection></KPage>
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