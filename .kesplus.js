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
        path: '/treatment_view',
        component: () => import('@/views/treatment_view/index.vue'),
        meta: {
          title: 'Patient Page',
          anoymous: true
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
