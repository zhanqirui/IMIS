import { request } from "@kesplus/kesplus";

const crudRoot = "/MSDATA/medicalRecordInfo";
/**
 * 
 * @param {import('./types').IMedicalRecordInfoForm} params 
 * @returns 
 */
export const addApi = (params) => {
  return request.post(crudRoot.concat("/add"), params, { appPrefix:true })
}
/**
 * 
 * @param {import('./types').IMedicalRecordInfoForm} params 
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
export const medicalRecordPatientInfoApi = (params) => {
  return request.get(crudRoot.concat("/medicalRecordPatientInfoView"), { params, appPrefix: true})
}
export const medicalRecordDoctorInfoApi = (params) => {
  return request.get(crudRoot.concat("/medicalRecordDoctorInfoView"), { params, appPrefix: true})
}
/**
 * 
 * @param {import('./types').IMedicalRecordInfoQueryform & { pageIndex: number, pageSize: number }} params 
 * @returns 
 */
export const pageApi = (params) => {
  return request.get(crudRoot.concat("/page"), { params, appPrefix: true })
}
  
/**
 * 
 * @param {import('./types').IMedicalRecordInfoQueryform } params 
 * @returns 
 */
export const listApi = (params) => {
  return request.get(crudRoot.concat("/list"), { params, appPrefix: true })
}
  