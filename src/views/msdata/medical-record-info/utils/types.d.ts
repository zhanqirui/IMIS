export type IMedicalRecordInfo = {
  id?: string
 
      
        /* 病人ID */
        patientId?: string
      
        /* 医生ID */
        doctorId?: string
      
        /* 诊断类别 */
        diagnosisCategory?: string
      
        /* 就诊日期 */
        visitDate?: number
      
        /* 科室ID */
        departmentId?: string
      
        /* 自述既往史 */
        selfReportedPastMedicalHistory?: string
      
        /* 患者情况 */
        patientCondition?: string
      
   
} & Record<string, any>;

export type IMedicalRecordInfoQueryform = {
  id?: string
  orderColumns?: string
  
      
        /* 病人ID */
        patientId?: string
      
        /* 医生ID */
        doctorId?: string
      
        /* 诊断类别 */
        diagnosisCategory?: string
      
        /* 就诊日期 */
        visitDate?: number
      
        /* 科室ID */
        departmentId?: string
      
  
} & Record<string, any>;

export type IMedicalRecordInfoForm = {
  id?: string
 
      
        /* 病人ID */
        patientId?: string
      
        /* 医生ID */
        doctorId?: string
      
        /* 诊断类别 */
        diagnosisCategory?: string
      
        /* 就诊日期 */
        visitDate?: number
      
        /* 科室ID */
        departmentId?: string
      
        /* 自述既往史 */
        selfReportedPastMedicalHistory?: string
      
        /* 患者情况 */
        patientCondition?: string
      
   
} & Record<string, any>;