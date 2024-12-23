
<template>
  <KDialogForm :read-pretty="readPretty">
    <el-form ref="formRef" :model="form" label-width="auto">
      <KPage min-height="100" mode="transparent" :no-padding="true">
        <KSection :no-padding="true">
          <KBlock :no-padding="true">
            <KCol>

              <KCell>
                
              <el-form-item label="ID" prop="id" :rules="[]" data-grid-span="1">
                  <el-input v-model="form.id" placeholder="请输入ID"  clearable/>
                </el-form-item></KCell>
              <KCell>
                <el-form-item label="病人ID" prop="patientId" :rules="[]" data-grid-span="1">
                  <el-input v-model="form.patientId" placeholder="请输入病人ID" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="医生ID" prop="doctorId" :rules="[]" data-grid-span="1">
                  <el-input v-model="form.doctorId" placeholder="请输入医生ID" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="诊断类别" prop="diagnosisCategory" :rules="[]" data-grid-span="1">
                  <el-input v-model="form.diagnosisCategory" placeholder="请输入诊断类别" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="就诊日期" prop="visitDate" :rules="[]" data-grid-span="1">
                  <el-date-picker v-model="form.visitDate" placeholder="请输入就诊日期" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="科室ID" prop="departmentId" :rules="[]" data-grid-span="1">
                  <el-input v-model="form.departmentId" placeholder="请输入科室ID" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="自述既往史" prop="selfReportedPastMedicalHistory" :rules="[]" data-grid-span="1">
                  <el-input v-model="form.selfReportedPastMedicalHistory" placeholder="请输入自述既往史" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="患者情况" prop="patientCondition" :rules="[]" data-grid-span="1">
                  <el-input v-model="form.patientCondition" placeholder="请输入患者情况" clearable/>
                </el-form-item>
              </KCell>
              <div>

    
  </div>
  <KCol>
    <KCell>
<KRow>
  <KCell></KCell>
  <KCell><ElButton  type="primary" @click="goToHome">跳转到首页</ElButton></KCell>
  <KCell></KCell>
</KRow>
    </KCell>
    <!-- <KCell><el-card   header="大模型辅助诊断信息"><div>
      {{ displayText }}
    </div></el-card></KCell> -->
    <KCell></KCell>
  </KCol>
      
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
    patientId: "",
    doctorId: "",
    diagnosisCategory: "",
    visitDate: "",
    departmentId: "",
    selfReportedPastMedicalHistory: "",
    patientCondition: "",
    ...props.row
  },
  fetchById: id => {
    return detailApi({id});
  },
  save: model => {
    if (model.id) {
      return addApi(model);
    }
    return addApi(model);
  }
});

defineExpose({ submit, reset, closeDialog });
</script>

<script>
export default {      
  methods: {
    goToHome() {
      this.$router.push('/treatment_view');
  
    }
  }
};
</script>