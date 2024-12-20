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
     <el-button><el-text>确认</el-text></el-button> </KQueryForm>
    
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
import { useRenderIcon, defineRouteMeta, access, useUserInfo } from "@kesplus/kesplus";
import { handleEdit, handleView, handleDelete } from "./utils/hook";
import { deleteApi, pageApi, patientDetailApi} from "./utils/api";
import { usePageModel } from "@@/plugin-platform/utils/hooks";
import { getSortChangeStr } from "@@/plugin-platform/utils/tools";

defineOptions({ handleEdit, handleView })

defineRouteMeta({
  title: "病患信息"
})

//获得用户信息
const userInfo = useUserInfo();
//获得真实姓名
const userRealName = userInfo.value.realName;

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
      name: "",
      gender: "",
      idNumber: "",
    },
    pageSize: 10,
    fetch: async _pager => {
      // 检查用户是否有权限
      const hasDetailPermission = access.hasAccess("msdata:patientInfo:detail");

      if (hasDetailPermission) {
        // 有权限，调用 pageApi
        const callback = await pageApi({
          ...queryForm,
          pageIndex: _pager.currentPage,
          pageSize: _pager.pageSize,
        });
        return { totalElements: callback?.totalElements ?? 0, content: callback?.content || [] };
      } else {
        // 没有权限，调用 patientDetailApi
        const callback = await patientDetailApi({ username: userRealName });
        const content = callback ? [{
          id: callback[0].id,
          name: callback[0].name,
          gender: callback[0].gender,
          age: callback[0].age,
          idNumber: callback[0].id_number,
          phone: callback[0].phone,
          emergencyContact: callback[0].emergency_contact,
          moduleCode: 'MSDATA',
          deptId: '0000'
        }] : [];
        return { totalElements: callback ? 1 : 0, content };
      }
    },
    hasPermission: () => access.hasAccess("msdata:patientInfo:detail")
  });
// #endregion

fetchData()

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

</script>
