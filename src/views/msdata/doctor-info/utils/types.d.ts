export type IDoctorInfo = {
  id?: string
 
      
        /* 科室ID */
        departmentId?: string
      
        /* 姓名 */
        name?: string
      
        /* 性别 */
        gender?: string
      
        /* 年龄 */
        age?: string
      
        /* 身份证号 */
        idNumber?: string
      
        /* 联系电话 */
        phone?: string
      
   
} & Record<string, any>;

export type IDoctorInfoQueryform = {
  id?: string
  orderColumns?: string
  
      
        /* 科室ID */
        departmentId?: string
      
        /* 姓名 */
        name?: string
      
        /* 身份证号 */
        idNumber?: string
      
  
} & Record<string, any>;

export type IDoctorInfoForm = {
  id?: string
 
      
        /* 科室ID */
        departmentId?: string
      
        /* 姓名 */
        name?: string
      
        /* 性别 */
        gender?: string
      
        /* 年龄 */
        age?: string
      
        /* 身份证号 */
        idNumber?: string
      
        /* 联系电话 */
        phone?: string
      
   
} & Record<string, any>;