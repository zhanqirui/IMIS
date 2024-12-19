<template>
  <KPage> <KSection>
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        <KCell>
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        <KCell>
        
       
      
   <el-form-item  :rules="[{required:false,message:'必填',},]" >
<KRow>
  <KCell>
        <KText>病情描述</KText>
            </KCell>
  
  <KCell> </KCell>
</KRow>
    <k-form-input    class="width：500"  :autosize="true"  type="textarea"   :rows="20" style="width: 100%; height: 300px;"/>
        
       </el-form-item>
   
       


        
        
            
      </KCell><el-button     type="flex" justify="end" style="width: 120px; height: 40px;"><el-text>确认</el-text></el-button>
      </KRow>
    </el-form>
  </KCell>
      </KRow>
    </el-form>
  </KSection><KSection>
    <KCell>
        
            
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        
  <KCol>
    <KCell><el-form-item label="模型建议">
        <el-input  />
      </el-form-item></KCell>
    <KCell><el-form-item label="采纳意见">
        
  <el-radio-group v-model="radio">
    <el-radio label="1"><span>是</span></el-radio>
    <el-radio label="2"><span>否</span></el-radio>
    
  </el-radio-group>
  
      </el-form-item></KCell>
    <KCell><el-button  size="samll">提交</el-button></KCell>
  </KCol>
       
      </KRow>
    </el-form>
  </KCell>
        </KSection>
              <KPageHeader>
                <KCell align="center">
                  <KText>大模型诊治界面</KText>
                </KCell>
              </KPageHeader></KPage>
</template>
<script setup>
import { reactive } from 'vue'
const form = reactive({})

const form_1 = reactive({})

const form_1_1 = reactive({})
</script>
