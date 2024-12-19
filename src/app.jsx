import { defineRuntimeConfig} from "@kesplus/kesplus";
// import './icons/icons'
// const initialState = useModel("@@initialState");
// 在此处匹配，如果getrole返回的字符串包含admin则把一个变量赋值成1， 包含patient则把一个变量赋值成2， 包含doctor则把变量赋值成3，包含researcher则把变量赋值成4

// const role = access.getRole();
// let roleValue;

// if (role.includes('admin')) {
//     console.log(access.getAccess());
// } else if (role.includes('patient')) {
//     access.setRole('patient');
// } else if (role.includes('d')) {
//     roleValue = 3;
// } else if (role.includes('r')) {
//     roleValue = 4;
// }

export default defineRuntimeConfig({});

export function onAppCreated({ app }) {}
