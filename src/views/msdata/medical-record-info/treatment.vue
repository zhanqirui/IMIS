<template>
  <KPage> <KSection>
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        <KCell>
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        <KCell>
        
       
      
    
      
        
            
<KRow>
  <KCell>
    
            
        
      <el-card header="我是卡片"><el-input :value="['刃恒99', 
                            '我刃你恒久了',
                            '支持应枫99喵,这杆枪可是锐利得足够刺透龙鳞啊', 
                            '成双之物总会再度重逢', 
                            '我会奉陪到底的'][Math.floor(Math.random() * 5)]" readonly /></el-card></KCell>
  <KCell> 

  
   
  
        <KText>修改意见</KText>
            <el-input  type="textarea" v-model="feedbackContent.text"/> </KCell>
  
</KRow>
    </KCell>
      </KRow>
    </el-form>
  </KCell>
      </KRow>
    </el-form>
  </KSection><KSection>
    <KCell>
        
            
    <el-form ref="formRef" label-width="auto" :model="form">
      <KRow>
        
  <KCol>
    
    <KCell><el-form-item           :prop="form.option" :rules="[{required:false,message:'必填',},]" label="采纳意见">
        
      <el-radio-group v-model="radioValue.selected">
                    <el-radio label="1">是</el-radio>
                    <el-radio label="2">否</el-radio>
                  </el-radio-group>
  
      </el-form-item></KCell>
    <KCell><el-button  size="samll" type="primary" @click="navigateTo">提交</el-button></KCell>
  </KCol>
       
      </KRow>
    </el-form>
  </KCell>
        </KSection>
              <KPageHeader>
                <KCell align="center">
                  <KText>大模型诊治界面</KText>
                </KCell>
              </KPageHeader></KPage>
</template>




<script setup>
import { reactive, onMounted, ref } from 'vue';
import form_1 from './form.vue';
const radioValue = reactive({
  selected: null, // 存储采纳意见的选择结果
  display: computed(() => {
    return radioValue.selected === '1' ? '是' : '否';
  })
});
const form = reactive({ option:true});
const form_1_1 = reactive({});
const displayRadioValue = computed(() => {
  return radioValue.value === '1' ? '是' : '否';
});

// function goToRecord() {
//   const form_1_1 = reactive({});

//   this.$router.push('/msdata/hospital-info');
//   console.log('提交按钮被点击，跳转到首页');

// }
import { useRoute } from "@@/core/coreExports";
import { useRouter } from 'vue-router';
const router = useRouter();
function navigateTo() {
  router.push({ path: "/msdata/medical-record-info"});
}

const form_1_1_1 = reactive({})

const form_1_1_1_1 = reactive({})
const feedbackContent = reactive({
  text: '' // 初始为空字符串，用户可以在 textarea 中输入内容
});
</script>
