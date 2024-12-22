<template>
  <KQueryList>
    <!-- <KQueryNav></KQueryNav> -->
    
    <KQueryForm >
      
      <el-form-item v-if="hasNotPatientBasicViewPermission" label="姓名">
        <el-input v-model="queryForm.name" placeholder="请输入" clearable />
      </el-form-item> 
      <el-form-item v-if="hasNotPatientBasicViewPermission" label="性别">
        <el-input v-model="queryForm.gender" placeholder="请输入" clearable />
      </el-form-item> 
      <el-form-item v-if="hasDetailPermission" label="身份证号">
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
import { useRenderIcon, defineRouteMeta, access, useUserInfo } from "@kesplus/kesplus";
import { handleEdit, handleView, handleDelete } from "./utils/hook";
import { deleteApi, pageApi, doctor_view_Api, patient_view_Api} from "./utils/api";
import { usePageModel } from "@@/plugin-platform/utils/hooks";
import { getSortChangeStr } from "@@/plugin-platform/utils/tools";
// import { useRouter } from 'vue-router';

defineOptions({ handleEdit, handleView })

defineRouteMeta({
  title: "病患信息"
})


  // const router = useRouter();
  // function navigateTo(where_to_go) {
  //   router.push({ path: where_to_go });
  // }

//获得用户信息
const userInfo = useUserInfo();
//获得真实姓名heID
const userRealID = userInfo.value.username;

// 检查用户是否有权限
const hasDetailPermission = access.hasAccess("msdata:patientInfo:detail");
const hasPartInfoPermission = access.hasAccess("part_info");
const hasNotPatientBasicViewPermission = ! access.hasAccess("patient_basic_view");


// const is_patient = userRealID.startsWith("PAT");

// is_patient && navigateTo("/avatar")

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
      if (hasDetailPermission) {
        // 有权限，调用 pageApi
        const callback = await pageApi({
          ...queryForm,
          pageIndex: _pager.currentPage,
          pageSize: _pager.pageSize,
        });
        return { totalElements: callback?.totalElements ?? 0, content: callback?.content || [] };
        //没有查看权限就只可以查看部分信息，所以如果有查看部分信息的权限就调用查看部分信息的接口
      } 
      else if(hasPartInfoPermission)
      {
        if (userRealID.startsWith("DOC")) {
          const callback = await doctor_view_Api(userRealID, { ...queryForm});
          const content = callback.map(item => ({
            name: item.name,
            gender: item.gender,
            age: item.age,
            idNumber: item.idNumber,
            phone: item.phone,
            emergencyContact: item.emergencyContact,
            moduleCode: 'MSDATA',
            deptId: '0000'
          }));
          return { totalElements: callback.length, content };
        }
        else if (userRealID.startsWith("PAT")) {
          const callback = await patient_view_Api(userRealID, { ...queryForm});
          const content = callback.map(item => ({
            name: item.name,
            gender: item.gender,
            age: item.age,
            idNumber: item.idNumber,
            phone: item.phone,
            emergencyContact: item.emergencyContact,
            moduleCode: 'MSDATA',
            deptId: '0000'
          }));
          return { totalElements: callback.length, content };
        } 
      }
    },
    hasPermission: () => (hasDetailPermission | hasPartInfoPermission) && hasNotPatientBasicViewPermission
    
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
