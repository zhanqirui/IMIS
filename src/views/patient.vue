<template>
  <KPage>
    
  <KSection>
<KPage>
  <KSection>
    <KBlock>
      <KCell>
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        <KCell>
<KRow>
  <KCell>
<KRow>
  
  
  

<KRow>
  <KCell>
<KRow>
  <KCell>
      <el-form-item label="表单项">
        <el-input  />
      </el-form-item>
   </KCell>
  <KCell></KCell>
  
</KRow>
    </KCell>
  
  <KCell>
<KRow>
  <KCell></KCell>
  <KCell></KCell>
  <KCell></KCell>
</KRow>
    </KCell>
</KRow>
    </KRow>
    </KCell>
  
  
</KRow>
    </KCell>
      </KRow>
    </el-form>
  </KCell>
    </KBlock>
  </KSection>

              </KPage>
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
</script>