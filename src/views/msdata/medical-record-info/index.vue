<template>
  <KQueryList>
    <!-- <KQueryNav></KQueryNav> -->
    
    <KQueryForm>
      
      <el-form-item v-if="isNotPatient" label="病人ID">
        <el-input v-model="queryForm.patientId" placeholder="请输入" clearable />
      </el-form-item> 
      <el-form-item v-if="isNotDoctor" label="医生ID">
        <el-input v-model="queryForm.doctorId" placeholder="请输入" clearable />
      </el-form-item> 
      <el-form-item label="诊断类别">
        <el-input v-model="queryForm.diagnosisCategory" placeholder="请输入" clearable />
      </el-form-item> 
      <el-form-item label="就诊日期">
        <el-date-picker v-model="queryForm.visitDate" placeholder="请输入" clearable />
      </el-form-item> 
      <el-form-item label="科室ID">
        <el-input v-model="queryForm.departmentId" placeholder="请输入" clearable />
      </el-form-item> 
    </KQueryForm>
    
    <KQueryTable>
      <KTableBar title="病历信息" :columns="columns" @refresh="fetchData">
        <template #buttons>
          <el-button
            v-access="'msdata:medicalRecordInfo:add'"
            type="primary"
            :icon="useRenderIcon('Plus')"
            @click="() => handleEdit({ title: '新增病历信息', effect: fetchData })"
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
                v-access="'msdata:medicalRecordInfo:edit'"
                class="!m-0"

             link
                type="primary"
                :size="size"
                :icon="useRenderIcon('EditPen')"
                @click="
                  () =>
                    handleEdit({
                      id: row.id,
                      title: '编辑病历信息',
                      row,
                      effect: fetchData
                    })
                "
              >
                编辑
              </el-button>
              <el-button
                v-access="'msdata:medicalRecordInfo:del'"
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
import { useRenderIcon, defineRouteMeta, access,useUserInfo } from "@kesplus/kesplus";
import { handleEdit, handleView, handleDelete } from "./utils/hook";
import { deleteApi, pageApi,patient_view_Api,doctor_view_Api } from "./utils/api";
import { usePageModel } from "@@/plugin-platform/utils/hooks";
import { getSortChangeStr } from "@@/plugin-platform/utils/tools";
import { patientDetailApi } from "../patient-info/utils/api";

defineOptions({ handleEdit, handleView })

defineRouteMeta({
  title: "病历信息"
})

const userInfo = useUserInfo();
//获得真实姓名heID
// const userRealName = userInfo.value.realName;
const userRealID = userInfo.value.username;

const isNotPatient = ! userRealID.startsWith("PAT");
const isNotDoctor  = ! userRealID.startsWith("DOC");
const hasDetailPermission = access.hasAccess("msdata:medicalRecordInfo:detail");
const hasPartInfoPermission = access.hasAccess("part_record_info");

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
                patientId:"",
                doctorId:"",
                diagnosisCategory:"",
                visitDate:"",
                departmentId:"",
                  },
    pageSize: 10,
    fetch: async _pager => {
      
      if (hasDetailPermission) 
      {
         const callback = await pageApi({
        ...queryForm,
        pageIndex: _pager.currentPage,
        pageSize: _pager.pageSize,
      });
      return { totalElements: callback?.totalElements ?? 0, content: callback?.content || [] };
      }

      else if(hasPartInfoPermission)
      {
          if (userRealID.startsWith("DOC")) {
          const callback = await doctor_view_Api(userRealID, { ...queryForm});
          const content = callback.map(item => ({
              patientId: item.patientId,
              doctorId: item.doctorId,
              diagnosisCategory: item.diagnosisCategory,
              visitDate: item.visitDate,
              departmentId: item.departmentId,
              selfReportedPastMedicalHistory: item.selfReportedPastMedicalHistory,
              patientCondition: item.patientCondition,
              moduleCode: 'MSDATA',
              deptId: '0000'
            }));
            return { totalElements: callback.length, content };
          }
          else if (userRealID.startsWith("PAT")) {
          const callback = await patient_view_Api(userRealID, { ...queryForm});
          const content = callback.map(item => ({
              patientId: item.patientId,
              doctorId: item.doctorId,
              diagnosisCategory: item.diagnosisCategory,
              visitDate: item.visitDate,
              departmentId: item.departmentId,
              selfReportedPastMedicalHistory: item.selfReportedPastMedicalHistory,
              patientCondition: item.patientCondition,
              moduleCode: 'MSDATA',
              deptId: '0000'
            }));
            return { totalElements: callback.length, content };
          } 
      }
      
     
      
    },
    hasPermission: () => access.hasAccess("msdata:medicalRecordInfo:detail") | access.hasAccess("part_record_info")
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
          label: "病人ID",
          prop: "patientId",
          align: "center",
          formatter: void 0,
          cellRenderer: void 0,
          sortable: "custom"
        },
                {
          label: "医生ID",
          prop: "doctorId",
          align: "center",
          formatter: void 0,
          cellRenderer: void 0,
          sortable: "custom"
        },
                {
          label: "诊断类别",
          prop: "diagnosisCategory",
          align: "center",
          formatter: void 0,
          cellRenderer: void 0,
          sortable: "custom"
        },
                {
          label: "就诊日期",
          prop: "visitDate",
          align: "center",
          formatter: void 0,
          cellRenderer: void 0,
          sortable: "custom"
        },
                {
          label: "科室ID",
          prop: "departmentId",
          align: "center",
          formatter: void 0,
          cellRenderer: void 0,
          sortable: "custom"
        },
                {
          label: "自述既往史",
          prop: "selfReportedPastMedicalHistory",
          align: "center",
          formatter: void 0,
          cellRenderer: void 0,
          sortable: "custom"
        },
                {
          label: "患者情况",
          prop: "patientCondition",
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
