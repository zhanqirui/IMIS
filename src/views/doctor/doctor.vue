.page-margin {
  margin: 20px;
}

<template>
  <KPage>
 <el-image src="/pictures/yetou.png" class="page-margin"/>   
  <KSection>
<KCell>
<!-- 主页面 -->
      <el-tabs type="border-card">
      <el-tab-pane label="病情诊断">
       <KCol>
    <KCell>
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        <KText>请您填写当前病人的具体信息，以便于我们为您提供更好的诊断。</KText>
      </KRow>
    </el-form>
    </KCell>
      <KRow>
    <KCell>
      <el-form-item label="表单项">
        <k-form-input />
      </el-form-item>

      <el-form-item label="表单项">
        <k-form-input />
      </el-form-item>
     </KCell>
        <KCell>
      <el-form-item label="表单项">
        <k-form-input />
      </el-form-item>
      <el-form-item label="表单项">
      <k-form-input />
      </el-form-item>
        </KCell>
                <KCell><KCell>
      <el-form-item label="表单项">
        <k-form-input />
      </el-form-item><el-form-item label="表单项">
        <k-form-input />
      </el-form-item>
   </KCell></KCell>
              </KRow>

<!-- <兵力信息> -->
    <KCell>
  <KCol>
    
    <KCell>
  <KCol>
    <KCell>
  <KCol><KCell>  <el-divider /></KCell>
    
    <KCell>
        <KText>病历具体信息</KText>
<KRow>
  <KCell> 
    <el-form ref="formRef" label-width="auto" :model="form">
      
    
        <k-form-input />
      </el-form>
  </KCell>
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        <KCell></KCell>
      </KRow>
    </el-form>
  
  
  
</KRow>
    
            </KCell>
    
              <KRow>
                <KCell></KCell>
                <KCell></KCell><KCell></KCell><KCell></KCell><KCell><el-button><el-text>确认</el-text></el-button> </KCell>
              </KRow>
  
  <KCol>
    <KCell>
        <KText>大模型生成内容</KText>
            </KCell>
    <KCell>
    <KCell>
      
      <el-input  type="textarea" /> </KCell>
        </KCell>
    <KCell>
  <el-radio-group v-model="radio">
    <el-radio label="1"><span>Option 1</span></el-radio>
    <el-radio label="2"><span>Option 2</span></el-radio>
  </el-radio-group>
  </KCell>
  </KCol>
      </KCol>
      </KCell>
    
              <KRow>
                <KCell>
        <KText>医生诊断结果</KText>
            </KCell>
                
              </KRow>
    <KCell><el-input  type="textarea" /> </KCell>
  </KCol>
      </KCell>
    
              <KRow>
                <KCell></KCell><KCell></KCell>
                <KCell></KCell><KCell></KCell><KCell><el-button><el-text>确认</el-text></el-button></KCell>
              </KRow>
  </KCol>
      </KCell>
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

const form_1_1_1_1_1 = reactive({})

const form_1_1_1_1_1_1 = reactive({})

const form_1_1_1_1_1_1_1 = reactive({})

const form_1_1_1_1_1_1_1_1 = reactive({})

const form_1_1_1_1_1_1_1_1_1 = reactive({})

const form_1_1_1_1_1_1_1_1_1_1 = reactive({})

const form_1_1_1_1_1_1_1_1_1_1_1 = reactive({})

const form_1_1_1_1_1_1_1_1_1_1_1_1 = reactive({})
</script>