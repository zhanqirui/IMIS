<template class="background_style">
  
    
    <!-- <el-carousel style="width:1650px;height:650px;" :autoplay="true">
      <el-carousel-item>
        <div style="width:1650px;height:650px;">  
                <img src="/pictures/login_pic_1.png" alt="示例图片"></div>

      </el-carousel-item>
      <el-carousel-item >
        <div style="width:1650px;height:650px;">  
                <img src="/pictures/login_pic_1.png" alt="示例图片"></div>

      </el-carousel-item>
    </el-carousel> -->
   

  <KCol>
    <KCell></KCell>
    <KCell><div class="background_style1" style="height: 100px; width: 100%;text-align: center;display: flex; justify-content: center; align-items: center; color: white;">
  欢迎您来到IMIS系统
</div></KCell>
    <KCell><div class="background_style" style="height: 110px; width: 100%;"></div></KCell>
    <KCell><KRow class="background_style">
  <KCell>
    <el-carousel style="width:100%;" :autoplay="true">
      <el-carousel-item >
        <img src="/pictures/login_pic_1.png" alt="示例图片" style="width:1920px;height:650px;">
      </el-carousel-item>
      <el-carousel-item >
        <img src="/pictures/cm2.png" alt="示例图片" style="width:1500px;height:300px;">
      </el-carousel-item>
      <el-carousel-item >
        <img src="/pictures/R-C.png" alt="示例图片" style="width:1500px;height:300px;">
      </el-carousel-item>
      <el-carousel-item >
        <img src="/pictures/rc2.png" alt="示例图片" style="width:1500px;height:300px;">
      </el-carousel-item>
    </el-carousel>
        </KCell>
  <KCell class="card-container" width="450px"><el-card class=" el-card  w-100 <sm:w-83 !rounded-4% !border-none  bg-color" style="background-color: rgba(255, 255, 255, 0.5);"><h3 class=" mt-6 flex-x-center text-24px text-primary font-500" type="primary">
          {{ $t("login.login") }}
        
          
      </h3>
        
        
      <el-form ref="formRef" :model="baseForm" :show-message="false" :rules="formRules" class="mt-6" autocomplete="off" size="large" @validate="validate">
          <el-form-item prop="username">
            <el-input v-model="baseForm.username" :placeholder="$t('login.usernamePlaceholder')"/>
          </el-form-item>
          <el-form-item prop="password">
            <el-input v-model="baseForm.password" show-password="" autocomplete="new-password" :placeholder="$t('login.passwordPlaceholder')"/>
          </el-form-item>
          <el-form-item prop="captchaValue">
            <el-input v-model="baseForm.captchaValue" class="captcha" :placeholder="$t('login.verifyCode')">
              <template #append="">
                <Captcha ref="codeRef" v-model="baseForm.uuid" class="h-full w-full"/>
              </template>
            </el-input>
          </el-form-item>
          <div v-if="validErrmsg" class="el-alert el-alert--error is-light justify-center !mb-16px">
            {{ validErrmsg }}
          </div>
          <el-form-item>
            <el-button class="w-full" type="primary" :loading="loading" @click="doLogin(false)">
              {{ $t("login.login") }}
            </el-button>
          </el-form-item>
          <el-form-item v-if="ldap">
            <el-button :loading="loading" @click="doLogin(true)" class="w-full">
              {{ $t("login.ldap") }}</el-button>
          </el-form-item>
        </el-form></el-card></KCell>
  
</KRow></KCell>
<KCell><div class="background_style" style="height: 350px; width: 100%;"></div></KCell>
<KCell><div class="background_style1" style="position: fixed; bottom: 0; left: 0; width: 100%; height: 100px; text-align: center; display: flex; justify-content: center; align-items: center; color: white;">
  地址：陕西省西安市长安区西北工业大学计算机学院 邮编：xxxxxx <br>本项目使用素材均来源于网络，如有侵权请联系本人删除
</div></KCell>
  </KCol>
      
     

   
        
     <row>
   
     </row>
</template>
<script setup>
import { ref, computed, unref } from "vue";
import { defineRouteMeta, useLogin, Captcha, useGet } from "@kesplus/kesplus";
// import Top from "./components/top.vue";
// import Bottom from "./components/bottom.vue";
const formRef = ref();
const errs = ref({});
const codeRef = ref();
defineRouteMeta({
  layout: {
    navigation: null,
  },
});
defineOptions({
  name: "CustomerLoginPage",
});
const { baseForm, formRules, loading, doLogin, ldap, error } = useLogin(
  formRef,
  codeRef
);
const validate = (prop, isValid, message) => {
  if (!isValid) {
    errs.value[prop] = message;
  } else {
    delete errs.value[prop];
  }
};
const validErrmsg = computed(() => {
  const keys = Object.keys(errs.value);
  if (keys.length) {
    return errs.value[keys.at(keys.length - 1)];
  }

  if (unref(error)) {
    return unref(error);
  }
  return false;
});
</script>

<!-- 可能会用的一些css格式 -->

<style>
.background_style{
background-color:#ffffff;
background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 56 28' width='56' height='28'%3E%3Cpath fill='%239ac7fc' fill-opacity='0.4' d='M56 26v2h-7.75c2.3-1.27 4.94-2 7.75-2zm-26 2a2 2 0 1 0-4 0h-4.09A25.98 25.98 0 0 0 0 16v-2c.67 0 1.34.02 2 .07V14a2 2 0 0 0-2-2v-2a4 4 0 0 1 3.98 3.6 28.09 28.09 0 0 1 2.8-3.86A8 8 0 0 0 0 6V4a9.99 9.99 0 0 1 8.17 4.23c.94-.95 1.96-1.83 3.03-2.63A13.98 13.98 0 0 0 0 0h7.75c2 1.1 3.73 2.63 5.1 4.45 1.12-.72 2.3-1.37 3.53-1.93A20.1 20.1 0 0 0 14.28 0h2.7c.45.56.88 1.14 1.29 1.74 1.3-.48 2.63-.87 4-1.15-.11-.2-.23-.4-.36-.59H26v.07a28.4 28.4 0 0 1 4 0V0h4.09l-.37.59c1.38.28 2.72.67 4.01 1.15.4-.6.84-1.18 1.3-1.74h2.69a20.1 20.1 0 0 0-2.1 2.52c1.23.56 2.41 1.2 3.54 1.93A16.08 16.08 0 0 1 48.25 0H56c-4.58 0-8.65 2.2-11.2 5.6 1.07.8 2.09 1.68 3.03 2.63A9.99 9.99 0 0 1 56 4v2a8 8 0 0 0-6.77 3.74c1.03 1.2 1.97 2.5 2.79 3.86A4 4 0 0 1 56 10v2a2 2 0 0 0-2 2.07 28.4 28.4 0 0 1 2-.07v2c-9.2 0-17.3 4.78-21.91 12H30zM7.75 28H0v-2c2.81 0 5.46.73 7.75 2zM56 20v2c-5.6 0-10.65 2.3-14.28 6h-2.7c4.04-4.89 10.15-8 16.98-8zm-39.03 8h-2.69C10.65 24.3 5.6 22 0 22v-2c6.83 0 12.94 3.11 16.97 8zm15.01-.4a28.09 28.09 0 0 1 2.8-3.86 8 8 0 0 0-13.55 0c1.03 1.2 1.97 2.5 2.79 3.86a4 4 0 0 1 7.96 0zm14.29-11.86c1.3-.48 2.63-.87 4-1.15a25.99 25.99 0 0 0-44.55 0c1.38.28 2.72.67 4.01 1.15a21.98 21.98 0 0 1 36.54 0zm-5.43 2.71c1.13-.72 2.3-1.37 3.54-1.93a19.98 19.98 0 0 0-32.76 0c1.23.56 2.41 1.2 3.54 1.93a15.98 15.98 0 0 1 25.68 0zm-4.67 3.78c.94-.95 1.96-1.83 3.03-2.63a13.98 13.98 0 0 0-22.4 0c1.07.8 2.09 1.68 3.03 2.63a9.99 9.99 0 0 1 16.34 0z'%3E%3C/path%3E%3C/svg%3E");
}
.background_style1{
background-color:#1a1b69;
background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 56 28' width='56' height='28'%3E%3Cpath fill='%239ac7fc' fill-opacity='0.4' d='M56 26v2h-7.75c2.3-1.27 4.94-2 7.75-2zm-26 2a2 2 0 1 0-4 0h-4.09A25.98 25.98 0 0 0 0 16v-2c.67 0 1.34.02 2 .07V14a2 2 0 0 0-2-2v-2a4 4 0 0 1 3.98 3.6 28.09 28.09 0 0 1 2.8-3.86A8 8 0 0 0 0 6V4a9.99 9.99 0 0 1 8.17 4.23c.94-.95 1.96-1.83 3.03-2.63A13.98 13.98 0 0 0 0 0h7.75c2 1.1 3.73 2.63 5.1 4.45 1.12-.72 2.3-1.37 3.53-1.93A20.1 20.1 0 0 0 14.28 0h2.7c.45.56.88 1.14 1.29 1.74 1.3-.48 2.63-.87 4-1.15-.11-.2-.23-.4-.36-.59H26v.07a28.4 28.4 0 0 1 4 0V0h4.09l-.37.59c1.38.28 2.72.67 4.01 1.15.4-.6.84-1.18 1.3-1.74h2.69a20.1 20.1 0 0 0-2.1 2.52c1.23.56 2.41 1.2 3.54 1.93A16.08 16.08 0 0 1 48.25 0H56c-4.58 0-8.65 2.2-11.2 5.6 1.07.8 2.09 1.68 3.03 2.63A9.99 9.99 0 0 1 56 4v2a8 8 0 0 0-6.77 3.74c1.03 1.2 1.97 2.5 2.79 3.86A4 4 0 0 1 56 10v2a2 2 0 0 0-2 2.07 28.4 28.4 0 0 1 2-.07v2c-9.2 0-17.3 4.78-21.91 12H30zM7.75 28H0v-2c2.81 0 5.46.73 7.75 2zM56 20v2c-5.6 0-10.65 2.3-14.28 6h-2.7c4.04-4.89 10.15-8 16.98-8zm-39.03 8h-2.69C10.65 24.3 5.6 22 0 22v-2c6.83 0 12.94 3.11 16.97 8zm15.01-.4a28.09 28.09 0 0 1 2.8-3.86 8 8 0 0 0-13.55 0c1.03 1.2 1.97 2.5 2.79 3.86a4 4 0 0 1 7.96 0zm14.29-11.86c1.3-.48 2.63-.87 4-1.15a25.99 25.99 0 0 0-44.55 0c1.38.28 2.72.67 4.01 1.15a21.98 21.98 0 0 1 36.54 0zm-5.43 2.71c1.13-.72 2.3-1.37 3.54-1.93a19.98 19.98 0 0 0-32.76 0c1.23.56 2.41 1.2 3.54 1.93a15.98 15.98 0 0 1 25.68 0zm-4.67 3.78c.94-.95 1.96-1.83 3.03-2.63a13.98 13.98 0 0 0-22.4 0c1.07.8 2.09 1.68 3.03 2.63a9.99 9.99 0 0 1 16.34 0z'%3E%3C/path%3E%3C/svg%3E");
}
</style>

<style lang="scss" scoped>
.image-container {
  display: grid;
  place-items: center; /* 同时水平和垂直居中 */
  height: 100vh; /* 根据需要调整高度 */
  margin-left: 0;
}
.card-container {
  display: flex;

  align-items: center; /* 垂直居中 */

}
.el-card {
  z-index: 1000; /* 设置一个高的数值确保卡片位于顶层 */
  position: relative; /* 确保 z-index 生效 */
}

</style>
