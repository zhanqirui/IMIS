.page-margin {
  margin: px;
}

<template>
  <KPage>
    
  <KSection>
<KCell>
<!-- 主页面信息-病人画像 -->

      <el-tabs type="border-card">
        <el-tab-pane label="病人画像">
  
      </el-tab-pane>
      
<el-tab-pane label="过往病历">
    
  <KCol>
    <KCell>
  <KCol>
    
              <KRow>
                <KCell>
    <el-timeline>
        <el-timeline-item timestamp="2023-10-1">
            <el-text>内容</el-text>
        </el-timeline-item>
    </el-timeline>
    </KCell><KCell> <el-image  fit="none" src="/logo.svg" /></KCell>
                
              </KRow>
    
    
  </KCol>
      </KCell>
    <KCell>
        <KTableBar />
      </KCell>
    <KCell>
    <el-carousel style="width:100%;" :autoplay="false">
      <el-carousel-item >
        
      <el-empty /></el-carousel-item>
      <el-carousel-item >
        <el-empty />
      </el-carousel-item>
    </el-carousel>
        </KCell>
  </KCol>
      <el-timeline>
        

        
    </el-timeline>
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

const form_1_1_1_1_1 = reactive({})
</script>