
<template>
  <KDialogForm :read-pretty="readPretty">
    <el-form ref="formRef" :model="form" label-width="auto">
      <KPage min-height="100" mode="transparent" :no-padding="true">
        <KSection :no-padding="true">
          <KBlock :no-padding="true">
            <KCol>
              <KCell>
                <el-form-item label="账号" prop="id" :rules="[]" data-grid-span="1">
                  <el-input v-model="form.id" placeholder="请输入ID" clearable/>
                </el-form-item>
              </KCell>
                      
              <KCell>
                <el-form-item label="科室ID" prop="departmentId" :rules="[]" data-grid-span="1">
                  <el-input v-model="form.departmentId" placeholder="请输入科室ID" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="姓名" prop="name" :rules="[]" data-grid-span="1">
                  <el-input v-model="form.name" placeholder="请输入姓名" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="性别" prop="gender" :rules="[]" data-grid-span="1">
                  <el-input v-model="form.gender" placeholder="请输入性别" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="年龄" prop="age" :rules="[]" data-grid-span="1">
                  <el-input-number v-model="form.age" placeholder="请输入年龄" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="身份证号" prop="idNumber" :rules="[]" data-grid-span="1">
                  <el-input v-model="form.idNumber" placeholder="请输入身份证号" clearable/>
                </el-form-item>
              </KCell>
            
              <KCell>
                <el-form-item label="联系电话" prop="phone" :rules="[]" data-grid-span="1">
                  <el-input v-model="form.phone" placeholder="请输入联系电话" clearable/>
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

defineOptions({ inhseritAttrs: false })

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
    departmentId: "",
    name: "",
    gender: "",
    age: "",
    idNumber: "",
    phone: "",
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
