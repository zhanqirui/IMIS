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

              <KSection>
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        <KCell>
      <el-form-item label="表单项">
        <el-input  />
      </el-form-item>
   </KCell><KCell></KCell>
      </KRow>
    </el-form>
  
              <KRow>
                
                <KCell></KCell><KCell></KCell>
              </KRow>
              <KRow>
                
                <KCell></KCell><KCell></KCell>
              </KRow><KCell><el-button            @click="navigateTo_1"  :round="true"  type="primary">提交</el-button> </KCell></KSection></KPage>
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

import { h, defineAsyncComponent } from "vue";
import { addDialog } from "@@/plugin-platform/components/dialog/hook";
function openDialog() {
  addDialog({
    title: '标题',
    props: {},
    width: "40%",
    effect: () => {
      // 关闭弹窗后的副作用
    },
    footerRenderer: () => [],
    contentRenderer: () => h(defineAsyncComponent(() => import(/* 待打开文件地址 */ "@/views/home.vue")), {})
  });
}

function openDialog_1() {
  addDialog({
    title: '标题',
    props: {},
    width: "60%",
    effect: () => {
      // 关闭弹窗后的副作用
    },
    footerRenderer: () => [],
    contentRenderer: () => h(defineAsyncComponent(() => import(/* 待打开文件地址 */ "@/views/home.vue")), {})
  });
}

import { useRouter, useRoute } from "@@/core/coreExports";
const router = useRouter();
function navigateTo() {
  router.push({ path: "/patient" });
}

const router_1 = useRouter();
function navigateTo_1() {
  router_1.push({ path: "/zhenzhi" });
}
</script>