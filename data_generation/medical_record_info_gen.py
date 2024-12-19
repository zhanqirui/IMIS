import random
import csv

def generate_medical_records(patient_file, doctor_file, output_file, num_records=1500):
    # 读取病人数据
    with open(patient_file, mode="r", encoding="utf-8") as pfile:
        patient_reader = csv.DictReader(pfile)
        patients = list(patient_reader)

    # 读取医生数据
    with open(doctor_file, mode="r", encoding="utf-8") as dfile:
        doctor_reader = csv.DictReader(dfile)
        doctors = list(doctor_reader)

    # 定义列名
    record_columns = [
        "id",  # 病历号
        "module_code",  # 固定为 MSDATA
        "dept_id",  # 固定为 0000
        "patient_id",  # 病人 ID
        "doctor_id",  # 医生 ID
        "diagnosis_category",  # 诊断类别
        "visit_date",  # 就诊日期
        "department_id",  # 科室 ID
        "self_reported_past_medical_history",  # 自述既往史
        "patient_condition"  # 患者情况
    ]

    # 随机生成病历信息
    def random_diagnosis_category():
        categories = ["感冒", "高血压", "糖尿病", "胃炎", "过敏", "骨折", "贫血", "心脏病", "支气管炎", "皮疹"]
        return random.choice(categories)

    def random_date():
        year = random.randint(2020, 2023)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year:04d}-{month:02d}-{day:02d}"

    def random_medical_history():
        histories = ["无既往史", "高血压史", "糖尿病史", "过敏史", "手术史", "骨折史"]
        return random.choice(histories)

    def random_condition():
        conditions = ["稳定", "急性", "慢性", "恢复期", "危重"]
        return random.choice(conditions)

    # 写入病历信息到输出文件
    with open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(record_columns)

        record_id = 1
        for _ in range(num_records):
            patient = random.choice(patients)
            doctor = random.choice(doctors)

            row = [
                f"REC{record_id:06d}",  # 病历号
                "MSDATA",  # module_code
                "0000",  # dept_id
                patient["id"],  # patient_id
                doctor["id"],  # doctor_id
                random_diagnosis_category(),  # diagnosis_category
                random_date(),  # visit_date
                doctor["department_id"],  # department_id
                random_medical_history(),  # self_reported_past_medical_history
                random_condition()  # patient_condition
            ]
            writer.writerow(row)
            record_id += 1

# 文件路径
folder_path = 'E:/C_codes/IMIS/IMIS/data_generation/data/'
patient_file = "patient_info_data.data"
doctor_file = "doctor_info_data.data"
output_file = "medical_records.data"

# 生成病历信息
generate_medical_records(folder_path+patient_file, folder_path+doctor_file, folder_path+output_file)
print(f"病历信息已生成并保存至 {output_file}")
