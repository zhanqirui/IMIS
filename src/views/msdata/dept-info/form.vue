
<template>
  <KDialogForm :read-pretty="readPretty">
    <el-form ref="formRef" :model="form" label-width="auto">
      <KPage min-height="100" mode="transparent" :no-padding="true">
        <KSection :no-padding="true">
          <KBlock :no-padding="true">
            <KCol>

                      
              <KCell>
                <el-form-item label="科室名称" prop="departmentName" :rules="[]" data-grid-span="1">
                  <el-input v-model="form.departmentName" placeholder="请输入科室名称" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="医生人数" prop="doctorCount" :rules="[]" data-grid-span="1">
                  <el-input-number v-model="form.doctorCount" placeholder="请输入医生人数" clearable/>
                </el-form-item>
              </KCell>
            
              
            
              
            
              
                      
            </KCol>
          </KBlock>
        </KSection>
      </KPage>
    </el-form>
  </KDialogForm>
</template>

<script setup>
import { ref, toRef } from "vue";
import { useSelect, useDialogForm } from "@@/plugin-platform/utils/hooks";
import { required } from "@@/plugin-platform/utils/validators";
import { addApi, updateApi, detailApi } from './utils/api'

defineOptions({ inheritAttrs: false })

const props = defineProps({
  id: { type: String },
  row: { type: Object, default: () => ({}) },
  readPretty: { type: Boolean },
});

const formRef = ref();

const { form, reset, submit, closeDialog } = useDialogForm({
  id: toRef(props, "id"),
  formRef,
  default: {
    departmentName: "",
    doctorCount: "",
    modelUseCount: "",
    adoptionRate: "",
    totalVisits: "",
    ...props.row
  },
  fetchById: id => {
    return detailApi({id});
  },
  save: model => {
    if (model.id) {
      return updateApi(model);
    }
    return addApi(model);
  }
});

defineExpose({ submit, reset, closeDialog });
</script>
