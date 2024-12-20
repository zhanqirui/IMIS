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
        path: '/patient_view',
        component: () => import('@/views/patient_view/index.vue'),
        meta: {
          title: 'Patient Page',
          access: '/patient_view', 
        },
      },
    ],
    mode: "history",
  },
  access: {
    roles: {
      admin: ["*", '/patient_view']
    },
  },
};

export default defineBuildConfig(buildConfig);
