<template>
  <div class="dashboard">
    <el-row :gutter="20">
      <!-- 柱状图1: 全院科室数量 -->
      <el-col :span="8">
        <el-card>
          <div ref="barChart1" class="chart"></div>
        </el-card>
      </el-col>
      <!-- 柱状图2: 全院医生数量 -->
      <el-col :span="8">
        <el-card>
          <div ref="barChart2" class="chart"></div>
        </el-card>
      </el-col>
      <!-- 柱状图3: 全院接待病人数量 -->
      <el-col :span="8">
        <el-card>
          <div ref="barChart3" class="chart"></div>
        </el-card>
      </el-col>
      <!-- 饼状图: 智能决策模型被采用率 -->
      <el-col :span="24">
        <el-card>
          <div ref="pieChart" class="chart"></div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import * as echarts from 'echarts';
import { ElRow, ElCol, ElCard } from 'element-plus';
import { useRenderIcon, defineRouteMeta, access } from "@kesplus/kesplus";
import { handleEdit, handleView, handleDelete } from "./utils/hook";
import { deleteApi, pageApi } from "./utils/api";
import { usePageModel } from "@@/plugin-platform/utils/hooks";
import { getSortChangeStr } from "@@/plugin-platform/utils/tools";

// 假设的单个医院统计数据
const hospitalStat = ref({
  name: "Test",
  departmentCount: 7,
  doctorCount: 208,
  patientVisits: 1506,
  modelAdoptionRate: 0.9,
});

// 柱状图1: 全院科室数量
const barChart1 = ref(null);
// 柱状图2: 全院医生数量
const barChart2 = ref(null);
// 柱状图3: 全院接待病人数量
const barChart3 = ref(null);
// 饼状图: 智能决策模型被采用率
const pieChart = ref(null);

// 颜色数组
const colors = ['#FFA41C', '#2F3037', '#9FE080', '#5C7BD9', '#7ED3F4', '#EE6666', '#c7c7c7', '#FFDC60'];

onMounted(() => {
  // 初始化柱状图1
  const chart1 = echarts.init(barChart1.value);
  chart1.setOption({
    title: { text: '全院科室数量' },
    xAxis: { type: 'category', data: [hospitalStat.value.name] },
    yAxis: { type: 'value' },
    series: [{
      name: '科室数量',
      type: 'bar',
      data: [hospitalStat.value.departmentCount],
      itemStyle: { color: colors[0] },
      label: { show: true, position: 'top', formatter: '{c}' }
    }]
  });

  // 初始化柱状图2
  const chart2 = echarts.init(barChart2.value);
  chart2.setOption({
    title: { text: '全院医生数量' },
    xAxis: { type: 'category', data: [hospitalStat.value.name] },
    yAxis: { type: 'value' },
    series: [{
      name: '医生数量',
      type: 'bar',
      data: [hospitalStat.value.doctorCount],
      itemStyle: { color: colors[1] },
      label: { show: true, position: 'top', formatter: '{c}' }
    }]
  });

  // 初始化柱状图3
  const chart3 = echarts.init(barChart3.value);
  chart3.setOption({
    title: { text: '全院接待病人数量' },
    xAxis: { type: 'category', data: [hospitalStat.value.name] },
    yAxis: { type: 'value' },
    series: [{
      name: '接待病人数量',
      type: 'bar',
      data: [hospitalStat.value.patientVisits],
      itemStyle: { color: colors[2] },
      label: { show: true, position: 'top', formatter: '{c}' }
    }]
  });

  // 初始化饼状图
  const pieChartInstance = echarts.init(pieChart.value);
  pieChartInstance.setOption({
    title: { text: '智能决策模型被采用率' },
    series: [{
      name: '被采用率',
      type: 'pie',
      radius: '55%',
      data: [
        { value: hospitalStat.value.modelAdoptionRate * 100, name: '被采用', itemStyle: { color: colors[3] } },
        { value: (1 - hospitalStat.value.modelAdoptionRate) * 100, name: '未被采用', itemStyle: { color: colors[4] } }
      ],
      label: {
        show: true,
        formatter: '{b}: {c}%',
        position: 'outside'
      }
    }]
  });
});

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



</script>

<style scoped>
.dashboard {
  padding: 20px;
}
.chart {
  height: 400px;
}
</style>