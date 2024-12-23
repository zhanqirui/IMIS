export type ITreatmentView = {
  id?: string
 
      
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
      
        /* 紧急联系人 */
        emergencyContact?: string
      
   
} & Record<string, any>;

export type ITreatmentViewQueryform = {
  id?: string
  orderColumns?: string
  
      
        /* 姓名 */
        name?: string
      
        /* 性别 */
        gender?: string
      
        /* 身份证号 */
        idNumber?: string
      
  
} & Record<string, any>;

export type ITreatmentViewForm = {
  id?: string
 
      
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
      
        /* 紧急联系人 */
        emergencyContact?: string
      
   
} & Record<string, any>;