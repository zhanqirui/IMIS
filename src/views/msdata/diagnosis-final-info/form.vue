
<template>
  <KDialogForm :read-pretty="readPretty">
    <el-form ref="formRef" :model="form" label-width="auto">
      <KPage min-height="100" mode="transparent" :no-padding="true">
        <KSection :no-padding="true">
          <KBlock :no-padding="true">
            <KCol>

                      
              <KCell>
                <el-form-item label="最终诊疗方案" prop="finalDiagnosisPlan" :rules="[]" data-grid-span="1">
                  <el-input v-model="form.finalDiagnosisPlan" placeholder="请输入最终诊疗方案" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="医疗记录id" prop="medicalRecordId" :rules="[required]" data-grid-span="1">
                  <el-input v-model="form.medicalRecordId" placeholder="请输入医疗记录id" clearable/>
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
    finalDiagnosisPlan: "",
    medicalRecordId: "",
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
