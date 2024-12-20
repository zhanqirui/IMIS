<template>
    <KQueryList>
      <!-- <KQueryNav></KQueryNav> -->
      
      <KQueryForm>
        
        <el-form-item label="医院名称">
          <el-input v-model="queryForm.hospitalName" placeholder="请输入" clearable />
        </el-form-item> 
      
    
        </KQueryForm>
      
      <KQueryTable>
        <KTableBar title="医院信息" :columns="columns" @refresh="fetchData">
          <template #buttons>
            <el-button
              v-access="'msdata:hospitalInfo:add'"
              type="primary"
              :icon="useRenderIcon('Plus')"
              @click="() => handleEdit({ title: '新增医院信息', effect: fetchData })"
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
                  v-access="'msdata:hospitalInfo:edit'"
                  class="!m-0"

               link
                  type="primary"
                  :size="size"
                  :icon="useRenderIcon('EditPen')"
                  @click="
                    () =>
                      handleEdit({
                        id: row.id,
                        title: '编辑医院信息',
                        row,
                        effect: fetchData
                      })
                  "
                >
                  编辑
                </el-button>
                <el-button
                  v-access="'msdata:hospitalInfo:del'"
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

  defineOptions({ handleEdit, handleView })

  defineRouteMeta({
    title: "医院信息"
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
    fetchData,//you can use this function to fetch data from server
    selectedRows,
    handleSelectionChange,
    handelSortChange,
  } = usePageModel({
      queryForm: {
        orderColumns: "",
                        hospitalName:"",
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
      hasPermission: () => access.hasAccess("msdata:hospitalInfo:detail")
    });
  // #endregion

  access.hasAccess("msdata:hospitalInfo:detail") && fetchData()

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
            label: "医院名称",
            prop: "hospitalName",
            align: "center",
            formatter: void 0,
            cellRenderer: void 0,
            sortable: "custom"
          },
                  {
            label: "全院科室数量",
            prop: "departmentCount",
            align: "center",
            formatter: void 0,
            cellRenderer: void 0,
            sortable: "custom"
          },
                  {
            label: "全院医生数量",
            prop: "doctorCount",
            align: "center",
            formatter: void 0,
            cellRenderer: void 0,
            sortable: "custom"
          },
                  {
            label: "全院接待病人数量（人次）",
            prop: "patientVisits",
            align: "center",
            formatter: void 0,
            cellRenderer: void 0,
            sortable: "custom"
          },
                  {
            label: "智能决策模型被采用率",
            prop: "modelAdoptionRate",
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

  </script>
