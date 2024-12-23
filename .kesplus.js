import { defineBuildConfig } from "@kesplus/kesplus";
/**
 * 定义KES Plus 配置
 * @type { import "@kesplus/kesplus".PluginBuildConfig }
 */
const buildConfig = {
  define: {
    __DEV__: true,
  },
  title: "kesplus",
  router: {
    routes : [
      {
        path: '/msdata/doctor-info/jump',
        component: () => import('@/views/msdata/doctor-info/j.vue'),
        meta: {
          title: 'Patient Page',
          anonymous: true
        },
      },
      {
        path: '/patient_view1',
        component: () => import('@/views/patient_view/index.vue'),
        meta: {
          title: 'Patient Page',
          anonymous: true
        },
      },
    ],
    mode: "history",
  },
  access: {
    roles: {
      admin: ["*"]
    },
  },
};

export default defineBuildConfig(buildConfig);
