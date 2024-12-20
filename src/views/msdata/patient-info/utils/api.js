import { request } from "@kesplus/kesplus";

const crudRoot = "/MSDATA/patientInfo";
/**
 * 
 * @param {import('./types').IPatientInfoForm} params 
 * @returns 
 */
export const addApi = (params) => {
  return request.post(crudRoot.concat("/add"), params, { appPrefix:true })
}
/**
 * 
 * @param {import('./types').IPatientInfoForm} params 
 * @returns 
 */
export const updateApi = (params) => {
  return request.put(crudRoot.concat("/update"), params,{ appPrefix: true })
}
/**
 * 
 * @param {Object} params 
 * @param {String} params.ids
 * @returns 
 */
export const deleteApi = (params) => {
  return request.delete(crudRoot.concat("/del"), { params, appPrefix: true })
}
/**
 * 
 * @param {Object} params 
 * @param {String} params.id
 * @returns 
 */
export const detailApi = (params) => {
  return request.get(crudRoot.concat("/detail"), { params, appPrefix: true})
}
/**
 * @param {Object} params 
 * @param {String} params.id
 * @returns 
 */
export const patientDetailApi = (params) => {
  return request.get(crudRoot.concat("/patientBasicView"), { params, appPrefix: true })
}
/**
 * 
 * @param {import('./types').IPatientInfoQueryform & { pageIndex: number, pageSize: number }} params 
 * @returns 
 */
export const pageApi = (params) => {
  return request.get(crudRoot.concat("/page"), { params, appPrefix: true })
}
  
/**
 * 
 * @param {import('./types').IPatientInfoQueryform } params 
 * @returns 
 */
export const listApi = (params) => {
  return request.get(crudRoot.concat("/list"), { params, appPrefix: true })
}


