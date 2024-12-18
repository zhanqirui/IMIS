
<template>
  <KDialogForm :read-pretty="readPretty">
    <el-form ref="formRef" :model="form" label-width="auto">
      <KPage min-height="100" mode="transparent" :no-padding="true">
        <KSection :no-padding="true">
          <KBlock :no-padding="true">
            <KCol>

                      
              <KCell>
                <el-form-item label="医院名称" prop="hospitalName" :rules="[required]" data-grid-span="1">
                  <el-input v-model="form.hospitalName" placeholder="请输入医院名称" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="全院科室数量" prop="departmentCount" :rules="[required]" data-grid-span="1">
                  <el-input-number v-model="form.departmentCount" placeholder="请输入全院科室数量" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="全院医生数量" prop="doctorCount" :rules="[required]" data-grid-span="1">
                  <el-input-number v-model="form.doctorCount" placeholder="请输入全院医生数量" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="全院接待病人数量（人次）" prop="patientVisits" :rules="[required]" data-grid-span="1">
                  <el-input-number v-model="form.patientVisits" placeholder="请输入全院接待病人数量（人次）" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="智能决策模型被采用率" prop="modelAdoptionRate" :rules="[required]" data-grid-span="1">
                  <el-input v-model="form.modelAdoptionRate" placeholder="请输入智能决策模型被采用率" clearable/>
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
    hospitalName: "",
    departmentCount: "",
    doctorCount: "",
    patientVisits: "",
    modelAdoptionRate: "",
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
