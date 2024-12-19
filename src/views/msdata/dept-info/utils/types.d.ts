export type IDeptInfo = {
  id?: string
 
      
        /* 科室名称 */
        departmentName?: string
      
        /* 医生人数 */
        doctorCount?: string
      
        /* 大模型使用次数 */
        modelUseCount?: string
      
        /* 采纳率 */
        adoptionRate?: string
      
        /* 累计就诊次数 */
        totalVisits?: string
      
   
} & Record<string, any>;

export type IDeptInfoQueryform = {
  id?: string
  orderColumns?: string
  
      
        /* 科室名称 */
        departmentName?: string
      
  
} & Record<string, any>;

export type IDeptInfoForm = {
  id?: string
 
      
        /* 科室名称 */
        departmentName?: string
      
        /* 医生人数 */
        doctorCount?: string
      
        /* 大模型使用次数 */
        modelUseCount?: string
      
        /* 采纳率 */
        adoptionRate?: string
      
        /* 累计就诊次数 */
        totalVisits?: string
      
   
} & Record<string, any>;