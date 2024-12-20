<template>
  <KPage> </KPage>
</template>
<script setup>
import { reactive } from 'vue'
const form = reactive({})

import { request, access } from '@kesplus/kesplus'
import { ref, toRef } from "vue";
import { useSelect, useDialogForm } from "@@/plugin-platform/utils/hooks";
const formRef = ref();
const { form:vfdeForm, reset:vfdeReset, submit:vfdeSubmit, closeDialog: vfdeCloseDialog } = useDialogForm({
  // 待编辑数据的id
  id: ref(),
  // 表单模型的Ref, 用于表单校验
  formRef: formRef,
  // 表单默认值
  default: {},
  fetchById: (id) => {
    return request.get('/kes/IMIS/MSDATA/patientInfo/detail',{ params: { id } });
  },
  save: async (model) => {
    if (model.id) {
      await request.put('/kes/IMIS/MSDATA/patientInfo/update', model);
    } else {
      await request.post('/kes/IMIS/MSDATA/patientInfo/add', model);
    }
    vfdeCloseDialog?.()
  },
});

const formRef_1 = ref();
const { form:vehgForm, reset:vehgReset, submit:vehgSubmit, closeDialog: vehgCloseDialog } = useDialogForm({
  // 待编辑数据的id
  id: ref(),
  // 表单模型的Ref, 用于表单校验
  formRef: formRef_1,
  // 表单默认值
  default: {},
  fetchById: (id) => {
    return request.get('/kes/IMIS/MSDATA/patientInfo/detail',{ params: { id } });
  },
  save: async (model) => {
    if (model.id) {
      await request.put('/kes/IMIS/MSDATA/patientInfo/update', model);
    } else {
      await request.post('/kes/IMIS/MSDATA/patientInfo/add', model);
    }
    vehgCloseDialog?.()
  },
});

const form_1 = reactive({})

const formRef_1_1 = ref();
const { form:v88tForm, reset:v88tReset, submit:v88tSubmit, closeDialog: v88tCloseDialog } = useDialogForm({
  // 待编辑数据的id
  id: ref(),
  // 表单模型的Ref, 用于表单校验
  formRef: formRef_1_1,
  // 表单默认值
  default: {},
  fetchById: (id) => {
    return request.get('/kes/IMIS/MSDATA/patientInfo/detail',{ params: { id } });
  },
  save: async (model) => {
    if (model.id) {
      await request.put('/kes/IMIS/MSDATA/patientInfo/update', model);
    } else {
      await request.post('/kes/IMIS/MSDATA/patientInfo/add', model);
    }
    v88tCloseDialog?.()
  },
});

import { usePageModel } from '@@/plugin-platform/utils/hooks';
const {
  loading:vk1mLoading,
  queryForm:vk1mQueryForm,
  resetForm:vk1mResetForm,
  pagination:vk1mPagination,
  listData:vk1mListData,
  fetchData:vk1mFetchData,
  resetPage:vk1mResetPage,
  handlePageSizeChange: handleVk1mPageSizeChange,
  handleCurrentPageChange:handleVk1mPageChange,
  handelSortChange:handleVk1mSortChange,
  selectedRows:vk1mSelectedRows,
  handleSelectionChange:handleVk1mSelectionChange,
} = usePageModel({
  // 查询条件
  queryForm: {
    name: '',
    gender: ''
  },
  // 每页个数
  pageSize: 10,
  fetch: async (_pager) => {
    const callback = await request.get('/kes/IMIS/MSDATA/patientInfo/page', {
      params: {
        ...vk1mQueryForm,
        pageIndex: _pager.currentPage,
        pageSize: _pager.pageSize,
      }
    });
    return {
      totalElements: callback?.totalElements ?? callback?.length ?? 0,
      content: callback?.content || callback || [],
    };
  },
  hasPermission: () => true
});
vk1mFetchData()
</script>
