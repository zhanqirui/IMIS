<!-- eslint-disable vue/no-v-html -->


<script setup>
import { computed } from "vue";
import { useModel } from "@kesplus/kesplus";
defineOptions({
  name: "LoginBottom",
});
const model = useModel("@@initialState");
const copyRight = computed(() => {
  return model.copyright || "Copy Right @ 西北工业大学IMIS开发团队";
});
</script>
