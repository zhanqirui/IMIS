<template>
  <KPage> <KSection>
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        <KCell>
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        <KCell>
   <el-form-item :rows="4" label="病历内容" size="large">
    <k-form-input  style="width: 100%; height: 200px;" />
  
        
      </el-form-item>
</KCell>
      </KRow>
    </el-form>
  </KCell>
      </KRow>
    </el-form>
  <el-button><el-text>确认</el-text></el-button></KSection><KSection>
    <KCell>
        
            
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        <KCell>
      <el-form-item label="模型建议">
        <el-input  />
      </el-form-item>
   
      <el-form-item label="采纳意见">
        
  <el-radio-group v-model="radio">
    <el-radio label="1"><span>是</span></el-radio>
    <el-radio label="2"><span>否</span></el-radio>
    
  </el-radio-group>
  
      </el-form-item>
   </KCell>
      </KRow>
    </el-form>
  </KCell>
        </KSection>
              <KPageHeader>
                <KCell align="center">
                  <KText>页头</KText>
                </KCell>
              </KPageHeader></KPage>
</template>
<script setup>
import { reactive } from 'vue'
const form = reactive({})

const form_1 = reactive({})

const form_1_1 = reactive({})
</script>
