<template>
  <KPage>
    <KSection >
      <KBlock>
        <KCell> </KCell>
      </KBlock>
      <KBlock :span="5">
        <KCell> </KCell>
      <KCell>
        
      
        <KTableBar :data="[  {    column: 'id',  },]" :columns="[  {    'type': 'selection'  },  {    'width': 80,    'type': 'index',    'label': '序号'  },  {    'prop': 'id',    'label': 'id'  },  {    'width': 120,    'slot': 'operation',    'label': '操作'  }]" title="qewqe">
    <template #operation="{row}">
        
    <el-button  @click="openDialog(row)" link="">编辑</el-button><el-button    @click="handleVsslDelete(row.id)" link="">删除</el-button></template>
  
    <template #buttons="">
        <el-button>新增</el-button>
    </template>
  </KTableBar>
      </KCell><KCell>
        <KTableBar></KTableBar>
      </KCell></KBlock>
      <KBlock :span="5">
        
              <KCol>
                <KCell> 
    <el-form     :scroll-to-error="true" ref="formRef" label-width="auto"   :model="vtsvQueryForm">
      <KRow>
        
              <KCol>
                <KCell>
      <el-form-item  :prop="vtsvQueryForm.name" :rules="[{required:true,message:'必填',},]"  label="name">
        <el-input  />
      </el-form-item>
   </KCell>
                <KCell></KCell><KCell></KCell><KCell></KCell>
              </KCol>
              <KCol>
                <KCell></KCell>
                <KCell></KCell><KCell></KCell><KCell></KCell>
              </KCol>
              <KCol>
                <KCell></KCell>
                <KCell></KCell><KCell><el-button  @click="vtsvQueryForm">查询</el-button> </KCell><KCell><el-button  @click="vtsvResetForm"><el-text>重置</el-text></el-button> </KCell>
              </KCol>
      </KRow>
    </el-form>
  </KCell>
                <KCell></KCell>
              </KCol>
      </KBlock>

    </KSection>
  </KPage>
</template>
<script setup>
import { reactive } from 'vue'
const form = reactive({})



import { request, access } from '@kesplus/kesplus'
import { usePageModel } from "@@/plugin-platform/utils/hooks";
const {
  loading:v6diLoading,
  queryForm:v6diQueryForm,
  resetForm:v6diResetForm,
  pagination:v6diPagination,
  listData:v6diListData,
  fetchData:v6diFetchData,
  resetPage:v6diResetPage,
  handlePageSizeChange: handleV6diPageSizeChange,
  handleCurrentPageChange:handleV6diPageChange,
  handelSortChange:handleV6diSortChange,
  selectedRows:v6diSelectedRows,
  handleSelectionChange:handleV6diSelectionChange,
} = usePageModel({
  // 查询条件
  queryForm: {
    name: "",
  },
  // 每页个数
  pageSize: 10,
  fetch: async (_pager) => {
    const callback = await request.get('/patientInfo/page', {
      params: {
        ...v6diQueryForm,
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
v6diFetchData()

const {
  loading:vtsvLoading,
  queryForm:vtsvQueryForm,
  resetForm:vtsvResetForm,
  pagination:vtsvPagination,
  listData:vtsvListData,
  fetchData:vtsvFetchData,
  resetPage:vtsvResetPage,
  handlePageSizeChange: handleVtsvPageSizeChange,
  handleCurrentPageChange:handleVtsvPageChange,
  handelSortChange:handleVtsvSortChange,
  selectedRows:vtsvSelectedRows,
  handleSelectionChange:handleVtsvSelectionChange,
} = usePageModel({
  // 查询条件
  queryForm: {
    name: "",
  },
  // 每页个数
  pageSize: 10,
  fetch: async (_pager) => {
    const callback = await request.get('/patientInfo/page', {
      params: {
        ...vtsvQueryForm,
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
vtsvFetchData() 

import { h, defineAsyncComponent } from "vue";
import { addDialog } from "@@/plugin-platform/components/dialog/hook";
function openDialog() {
  addDialog({
    title: '标题',
    props: {},
    width: "40%",
    effect: () => {
      // 关闭弹窗后的副作用
      vtsvFetchData()
    },
    footerRenderer: () => [],
    contentRenderer: () => h(defineAsyncComponent(() => import(/* 待打开文件地址 */ "@/views/home.vue")), {})
  });
}

import { ElMessageBox, ElMessage } from 'element-plus'
async function handleVxdxDelete(ids = '') {
  const callback = await ElMessageBox.confirm("确认删除？", "删除", { 
    showCancelButton: true
  });
  if (callback !== "confirm") return;
  const deleteId = Array.isArray(ids) ? ids.join(",") : ids;
  try {
    await await request
      .delete("/patientInfo/del", { params: { ids: deleteId } })
      .then(() => ElMessage.success("删除成功"))
      .catch(() => Promise.resolve());
  } catch (err) {
    ElMessage.error(err?.message ?? err);
  }
}

async function handleVsslDelete(ids = '') {
  const callback = await ElMessageBox.confirm("确认删除？", "删除", { 
    showCancelButton: true
  });
  if (callback !== "confirm") return;
  const deleteId = Array.isArray(ids) ? ids.join(",") : ids;
  try {
    await await request
      .delete("/patientInfo/del", { params: { ids: deleteId } })
      .then(() => ElMessage.success("删除成功"))
      .catch(() => Promise.resolve());
  } catch (err) {
    ElMessage.error(err?.message ?? err);
  }
}
</script>