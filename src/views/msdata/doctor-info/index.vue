<template>
  <!-- <el-button  class="fixed-button" type="success"  @click="navigateTo">跳转到详情页</el-button> -->
    <KQueryList>
      <!-- <KQueryNav></KQueryNav> -->
      <!-- 查询组件 -->
      <KQueryForm>
        
        <el-form-item label="科室ID">
          <el-input v-model="queryForm.departmentId" placeholder="请输入" clearable />
        </el-form-item> 
        <el-form-item label="姓名">
          <el-input v-model="queryForm.name" placeholder="请输入" clearable />
        </el-form-item> 
        <el-form-item label="身份证号">
          <el-input v-model="queryForm.idNumber" placeholder="请输入" clearable />
        </el-form-item> 
         </KQueryForm>
      <!-- 查询结果-列表组件 --> <KQueryTable>
         <el-divider /><KTableBar    :data="[  {    column: '序号',  },]" title="医生信息" :columns="columns" @refresh="fetchData">
          <template #buttons>
            <el-button
              v-access="'msdata:doctorInfo:add'"
              type="primary"
              :icon="useRenderIcon('Plus')"
              @click="() => handleEdit({ title: '新增医生信息=', effect: fetchData })"
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
                  v-access="'msdata:doctorInfo:edit'"
                  class="!m-0"

               link
                  type="primary"
                  :size="size"
                  :icon="useRenderIcon('EditPen')"
                  @click="
                    () =>
                      handleEdit({
                        id: row.id,
                        title: '编辑医生信息',
                        row,
                        effect: fetchData
                      })
                  "
                >
                  编辑
                </el-button>
                <el-button
                  v-access="'msdata:doctorInfo:del'"
                  class="!m-0"
                  link
                  type="danger"
                  :size="size"
                  :icon="useRenderIcon('Delete')"
                  @click="() => handleDelete(row.id, fetchData)"
                >
                  删除
                </el-button>
                <!-- 新增跳转到主页的按钮 -->
  <el-button
    class="!m-0"
    link
    type="success"
    :size="size"
    :icon="useRenderIcon('Home')"
    @click="goToHomePage"
  >
    主页
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
  import { deleteApi, pageApi,doctorDetailApi } from "./utils/api";
  import { usePageModel } from "@@/plugin-platform/utils/hooks";
  import { getSortChangeStr } from "@@/plugin-platform/utils/tools";
  import { useRouter } from 'vue-router';

  defineOptions({ handleEdit, handleView })

  defineRouteMeta({
    title: "医生信息"
  })

  const userInfo = useUserInfo();
  const userRealID= userInfo.value.username;
  
  // #region 列表数据
  const {
    queryForm,
    resetForm,
    loading,
    listData,
    pagination,
    handlePageSizeChange,
    handleCurrentPageChange,
    fetchData,// 刷新列表数据
    selectedRows,
    handleSelectionChange,
    handelSortChange,
  } = usePageModel({
      queryForm: {
        orderColumns: "",
                        departmentId:"",
                  name:"",
                  idNumber:"",
                    },
      pageSize: 10,
      fetch: async _pager => {
        // 检查用户是否有权限
      const hasDetailPermission = access.hasAccess("msdata:doctorInfo:detail");
        //判断是否有权限
      if (hasDetailPermission) {
        // 有权限，调用 pageApi 正常显示
        const callback = await pageApi({
          ...queryForm,
          pageIndex: _pager.currentPage,
          pageSize: _pager.pageSize,
        });
        return { totalElements: callback?.totalElements ?? 0, content: callback?.content || [] };
      } else {
        // 没有权限，调用 doctorDetailApi
        const callback = await doctorDetailApi({ username: userRealID }); // TODO: 写user_id
        const content = callback ? [{
          id: callback[0].id,
          name: callback[0].name,
          gender: callback[0].gender,
          age: callback[0].age,
          idNumber: callback[0].id_number,
          phone: callback[0].phone,
          departmentId: callback[0].departmentId,
          moduleCode: 'MSDATA',
          deptId: '0000'
        }] : [];
        return { totalElements: callback ? 1 : 0, content };
        //no answer-?all elements?
      }
      },
      hasPermission: () => access.hasAccess("msdata:doctorInfo:detail")
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
            label: "科室ID",
            prop: "departmentId",
            align: "center",
            formatter: void 0,
            cellRenderer: void 0,
            sortable: "custom"
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
        label: "操作",
        width: 230,
        align: "center",
        fixed: "right",
        slot: "operation",
        showOverflowTooltip: false
      }
  ];
  // #endregion


  // const router = useRouter();
  // function navigateTo() {
  //   router.push({ path: "/patient_view" });
  // }
</script>


<style scoped>
.fixed-button {
  position: fixed;
  bottom: 0px;
  right: 0px;
}
</style>
