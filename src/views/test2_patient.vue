<template>
  <KPage>
    <KSection>
      <KBlock>
        <KCell> 
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        <KCell>
<KRow>
  
              <KCol>
                <KCell>
      <el-form-item label="表单项">
        <el-input  />
      </el-form-item>
   </KCell>
                <KCell>
      <el-form-item label="表单项">
        <el-input  />
      </el-form-item>
   </KCell><KCell>
      <el-form-item label="表单项">
        <el-input  />
      </el-form-item>
   </KCell>
              </KCol>
  
              <KCol>
                <KCell>
      <el-form-item label="表单项">
        <el-input  />
      </el-form-item>
   </KCell>
                <KCell>
      <el-form-item label="表单项">
        <el-input  />
      </el-form-item>
   </KCell><KCell>
      <el-form-item label="表单项">
        <el-input  />
      </el-form-item>
   </KCell>
              </KCol>
  
              <KCol>
                <KCell>
      <el-form-item label="表单项">
        <el-input  />
      </el-form-item>
   </KCell>
                <KCell>
      <el-form-item label="表单项">
        <el-input  />
      </el-form-item>
   </KCell><KCell>
      <el-form-item label="表单项">
        <el-input  />
      </el-form-item>
   </KCell><KCell></KCell>
              </KCol>
</KRow>
    </KCell>
      </KRow>
    </el-form>
  </KCell>
      </KBlock>
      <KBlock>
        <KCell> </KCell>
      </KBlock>
    </KSection>
  </KPage>
</template>
<script setup>
import { reactive } from 'vue'
const form = reactive({})


</script>