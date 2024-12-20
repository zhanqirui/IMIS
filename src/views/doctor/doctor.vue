.page-margin {
  margin: px;
}

<template>
  <KPage>
    
  <KSection>
<KCell>
<!-- 主页面信息-病人画像 -->
<el-image src="/pictures/yetou.png" class="page-margin"/>
      <el-tabs type="border-card">
        <el-tab-pane label="医生画像">
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        <KCell></KCell>
      </KRow>
    </el-form>
  <KRow>

              <KCol>
                <KCell><el-image          fit="none"   src="/pictures/zqr.png" style="width: 300px; height: 400px;" /></KCell>
                <KCell><KCell><KText style="text-align: center; font-family: 'DengXian', sans-serif;;font-size: 20px;">病人图片</KText></KCell></KCell>
              </KCol><KCell><el-card header="您的个人信息" style="font-size: 24px;width:800px; height: 500px;">
</el-card></KCell>
<KCell><el-calendar /></KCell>
</KRow>
  <KCol>
              <KRow>
                
              <KCol>
                
                <KCell></KCell>
              </KCol>
                <KCell></KCell>
              </KRow>
    <KCell>
    <el-carousel style="width:100%;" :autoplay="false">
      <el-carousel-item >
        <el-empty />
      </el-carousel-item>
      <el-carousel-item >
        <el-empty />
      </el-carousel-item>
    </el-carousel>
        </KCell>
    
  </KCol>
      </el-tab-pane>
      
<el-tab-pane label="病人一览">
    
  <KCol>
    <KCell>
  <KCol>
    
              
    
    
  
        
    <KText>请您进行病人和病历的管理与查看。</KText></KCol>
      </KCell>
    <KCell>
        <KTableBar title="您的病人"/>
      </KCell>
    <KCell>
    
        
    <KCell>
    
        
      
      
        
            </KCell>
        </KCell>
  </KCol>
      <el-timeline>
        

        
    </el-timeline>
    </el-tab-pane>

<el-tab-pane label="病情诊断">
  <KCol>
    <KCell>
    <KCell>
    <el-form ref="formRef" label-width="auto" :model="form"><KRow>
        
      
        <KText>请您填写当前病人的具体信息，以便于我们为您提供更好的诊断。</KText>
            </KRow>
       <el-divider />
    </el-form>
  </KCell>
        </KCell>
    
              <KRow>
                <KCell><KCell>
      
   
      <el-form-item label="表单项">
        
      
        <k-form-input />
      </el-form-item><el-form-item label="表单项">
        
      
        <k-form-input />
      </el-form-item>
   </KCell></KCell><KCell><KCell>
      <el-form-item label="表单项">
        
      
        <k-form-input />
      </el-form-item><el-form-item label="表单项">
        
      
        <k-form-input />
      </el-form-item>
   </KCell></KCell>
                <KCell><KCell>
      <el-form-item label="表单项">
        
      
        <k-form-input />
      </el-form-item><el-form-item label="表单项">
        
      
        <k-form-input />
      </el-form-item>
   </KCell></KCell>
              </KRow>
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