<template>
  <KPage> <KSection>
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        <KCell></KCell>
      </KRow>
    </el-form>
  </KSection></KPage>
</template>
<script setup>
import { reactive } from 'vue'
const form = reactive({})
</script>
