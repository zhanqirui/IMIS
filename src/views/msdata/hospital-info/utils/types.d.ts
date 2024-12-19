export type IHospitalInfo = {
  id?: string
 
      
        /* 医院名称 */
        hospitalName?: string
      
        /* 全院科室数量 */
        departmentCount?: string
      
        /* 全院医生数量 */
        doctorCount?: string
      
        /* 全院接待病人数量（人次） */
        patientVisits?: string
      
        /* 智能决策模型被采用率 */
        modelAdoptionRate?: string
      
   
} & Record<string, any>;

export type IHospitalInfoQueryform = {
  id?: string
  orderColumns?: string
  
      
        /* 医院名称 */
        hospitalName?: string
      
  
} & Record<string, any>;

export type IHospitalInfoForm = {
  id?: string
 
      
        /* 医院名称 */
        hospitalName?: string
      
        /* 全院科室数量 */
        departmentCount?: string
      
        /* 全院医生数量 */
        doctorCount?: string
      
        /* 全院接待病人数量（人次） */
        patientVisits?: string
      
        /* 智能决策模型被采用率 */
        modelAdoptionRate?: string
      
   
} & Record<string, any>;