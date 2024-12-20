<template>
    <KQueryList>
      <!-- <KQueryNav></KQueryNav> -->
      
      <KQueryForm>
        
        <el-form-item label="姓名">
          <el-input v-model="queryForm.name" placeholder="请输入" clearable />
        </el-form-item> 
        <el-form-item label="性别">
          <el-input v-model="queryForm.gender" placeholder="请输入" clearable />
        </el-form-item> 
        <el-form-item label="身份证号">
          <el-input v-model="queryForm.idNumber" placeholder="请输入" clearable />
        </el-form-item> 
      </KQueryForm>
      
      <KQueryTable>
        <KTableBar title="病患信息" :columns="columns" @refresh="fetchData">
          <template #buttons>
            <el-button
              v-access="'msdata:patientInfo:add'"
              type="primary"
              :icon="useRenderIcon('Plus')"
              @click="() => handleEdit({ title: '新增病患信息', effect: fetchData })"
            >
              新增
            </el-button>
          </template>
          <template #default="{ size, dynamicColumns }">
            <KTable
              border
              row-key="id"
              align-whole="center"
              show-overflow-tooltip
              table-layout="auto"
              :loading="loading"
              :size="size"
              height="100%"
              :data="listData"
              :columns="dynamicColumns"
              :pagination="pagination"
              :paginationSmall="size === 'small' ? true : false"
              :header-cell-style="{
                background: 'var(--el-table-row-hover-bg-color)',
                color: 'var(--el-text-color-primary)'
              }"
              @sort-change="handelSortChange"
              @selection-change="handleSelectionChange"
              @page-size-change="handlePageSizeChange"
              @page-current-change="handleCurrentPageChange"
            >
              <template #operation="{ row }">
                <el-button
                  v-access="'msdata:patientInfo:edit'"
                  class="!m-0"

               link
                  type="primary"
                  :size="size"
                  :icon="useRenderIcon('EditPen')"
                  @click="
                    () =>
                      handleEdit({
                        id: row.id,
                        title: '编辑病患信息',
                        row,
                        effect: fetchData
                      })
                  "
                >
                  编辑
                </el-button>
                <el-button
                  v-access="'msdata:patientInfo:del'"
                  class="!m-0"
                  link
                  type="danger"
                  :size="size"
                  :icon="useRenderIcon('Delete')"
                  @click="() => handleDelete(row.id, fetchData)"
                >
                  删除
                </el-button>
              </template>
            </KTable>
          </template>
        </KTableBar>
      </KQueryTable>
    </KQueryList>
  </template>

  <script setup>
  import { useRenderIcon, defineRouteMeta, access } from "@kesplus/kesplus";
  import { handleEdit, handleView, handleDelete } from "./utils/hook";
  import { deleteApi, pageApi } from "./utils/api";
  import { usePageModel } from "@@/plugin-platform/utils/hooks";
  import { getSortChangeStr } from "@@/plugin-platform/utils/tools";

  import { useUserInfo } from "@kesplus/kesplus"
  const userInfo = useUserInfo();
  const user_realname = userInfo?.value.realname || "";

  defineOptions({ handleEdit, handleView })

  defineRouteMeta({
    title: "病患信息"
  })
  // #region 列表数据
  const {
    queryForm,
    resetForm,
    loading,
    listData,
    pagination,
    handlePageSizeChange,
    handleCurrentPageChange,
    fetchData,
    selectedRows,
    handleSelectionChange,
    handelSortChange,
  } = usePageModel({
      queryForm: {
        orderColumns: "",
                        name:"",
                  gender:"",
                  idNumber:"",
                    },
      pageSize: 10,
      fetch: async _pager => {
        const callback = await pageApi({
          ...queryForm,
          pageIndex: _pager.currentPage,
          pageSize: _pager.pageSize,
        });
        return { totalElements: callback?.totalElements ?? 0, content: callback?.content || [] };
      },
      hasPermission: () => access.hasAccess("msdata:patientInfo:detail")
    });
  // #endregion

  access.hasAccess("msdata:patientInfo:detail") && fetchData()

  // #region 列表字段
  /** @type {TableColumnList} */
  const columns = [
      {
        label: "",
        type: "selection",
        showOverflowTooltip: false,
        selectable: (row, index) => {
          return true
        }
      },
      {
        label: "序号",
        type: "index",
        width: 60,
        showOverflowTooltip: false
      },
                        {
            label: "姓名",
            prop: "name",
            align: "center",
            formatter: void 0,
            cellRenderer: void 0,
            sortable: "custom"
          },
                  {
            label: "性别",
            prop: "gender",
            align: "center",
            formatter: void 0,
            cellRenderer: void 0,
            sortable: "custom"
          },
                  {
            label: "年龄",
            prop: "age",
            align: "center",
            formatter: void 0,
            cellRenderer: void 0,
            sortable: "custom"
          },
                  {
            label: "身份证号",
            prop: "idNumber",
            align: "center",
            formatter: void 0,
            cellRenderer: void 0,
            sortable: "custom"
          },
                  {
            label: "联系电话",
            prop: "phone",
            align: "center",
            formatter: void 0,
            cellRenderer: void 0,
            sortable: "custom"
          },
                  {
            label: "紧急联系人",
            prop: "emergencyContact",
            align: "center",
            formatter: void 0,
            cellRenderer: void 0,
            sortable: "custom"
          },
                    {
        label: "操作",
        width: 230,
        align: "center",
        fixed: "right",
        slot: "operation",
        showOverflowTooltip: false
      }
  ];
  // #endregion
  
  const user_params = {
    username: "病人",

  }
  import { request } from '@kesplus/kesplus'
  const {
    loading:v17rLoading,
    queryForm:v17rQueryForm,
    resetForm:v17rResetForm,
    pagination:v17rPagination,
    listData:v17rListData,
    fetchData:v17rFetchData,
    resetPage:v17rResetPage,
    handlePageSizeChange: handleV17rPageSizeChange,
    handleCurrentPageChange:handleV17rPageChange,
    handelSortChange:handleV17rSortChange,
    selectedRows:v17rSelectedRows,
    handleSelectionChange:handleV17rSelectionChange,
  } = usePageModel({
    // 查询条件
    queryForm: {
      orderColumns: "",
    },
    // 每页个数
    pageSize: 10,
    fetch: async (_pager) => {
      const callback = await request.get('/MSDATA/patientInfo/patientBasicView', {user_params});
      return {
        totalElements: callback?.totalElements ?? callback?.length ?? 0,
        content: callback?.content || callback || [],
      };
    },
    hasPermission: () => access.hasAccess("patient_basic_view")
  });
  access.hasAccess("patient_basic_view") && v17rFetchData();

</script>
