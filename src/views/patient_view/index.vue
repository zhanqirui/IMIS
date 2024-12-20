.page-margin {
  margin: 10px;
}

<template>
  <div v-access="'/patient_view'" >
    <!-- 整个页面的内容都在这个 div 下面 -->

    <KPage>
      
      <KSection>
        <KRow>
          <KCell><el-image src="/pictures/zqr.png" /></KCell>
          <KCell>
            <el-form ref="formRef" :model="form">
              <KRow>
                
                <el-card header="您的个人信息" style="width: 900px; height: 400px;">
                  
                  <KRow>
                    <KText>姓名</KText>
                  </KRow>
                  <KRow>
                    <KText>性别</KText>
                  </KRow>
                  <KRow>
                    <KText>年龄</KText>
                  </KRow>
                  <KRow>
                    <KCell>
                      <KText>身份证号</KText>
                    </KCell>
                  </KRow>
                  <KRow>
                    <KCell>
                      <KText>联系电话</KText>
                    </KCell>
                  </KRow>
                  <KRow>
                    <KCell>
                      <KText>紧急联系人</KText>
                    </KCell>
                  </KRow>
                  <KRow>
                    <KCell>
                      <KText>就诊次数</KText>
                    </KCell>
                  </KRow>
                </el-card>
              </KRow>
            </el-form>
          </KCell>
        </KRow>
      </KSection>
      <KSection>
        
        <KBlock>
          <KCell>
            <el-form ref="formRef" :model="form">
              <KRow>
                <KCell>
                
                  <KRow>
                    <KCell></KCell>
                  </KRow>
                </KCell>
              </KRow>
            </el-form>
          </KCell>
        </KBlock>
      </KSection>
    </KPage>
  
    <KCell></KCell>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
const form = reactive({})

const form_1 = reactive({})

import { request } from '@kesplus/kesplus'
import { ref, toRef } from "vue";
import { useSelect, useDialogForm } from "@@/plugin-platform/utils/hooks";
const formRef = ref();
const { form: vwfrForm, reset: vwfrReset, submit: vwfrSubmit, closeDialog: vwfrCloseDialog } = useDialogForm({
  // 待编辑数据的id
  id: ref(),
  // 表单模型的Ref, 用于表单校验
  formRef: formRef,
  // 表单默认值
  default: {},
  fetchById: (id) => {
    return request.get('/kes/IMIS/MSDATA/getPatientPastHistory', { params: { id } });
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