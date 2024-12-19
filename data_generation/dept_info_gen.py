import random
import csv

def generate_random_data(file_path, num_rows=7):    
    with open(file_path, mode="w", encoding="utf-8") as file:
        file.truncate(0)

    # 定义数据列名和对应的随机数据生成规则
    columns = [
        "id",  # varchar 类型
        "module_code",  # varchar 类型
        "dept_id",  # varchar 类型
        "department_name",  # varchar 类型
        "doctor_count",  # integer 类型
        "model_use_count",  # integer 类型
        "adoption_rate",  # numeric 类型
        "total_visits"  # integer 类型
    ]

    # 假设生成数据的规则
    department_names = ["内科", "外科", "儿科", "妇产科", "眼科", "耳鼻喉科", "皮肤科"]

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")

        # 写入列名
        writer.writerow(columns)

        for ind, _ in enumerate(range(num_rows)):
            row = [
                f"ID{1000+ind}",  # id 随机字符串
                f"MSDATA",  # module_code
                f"0000",  # dept_id
                department_names[ind],  # department_name 随机科室名称
                random.randint(1, 50),  # doctor_count 随机医生人数
                random.randint(0, 1000),  # model_use_count 随机使用次数
                round(random.uniform(0.0, 1.0), 2),  # adoption_rate 随机采纳率
                random.randint(1, 10000)  # total_visits 随机累计就诊次数
            ]
            writer.writerow(row)

# 生成数据文件
file_path = "E:/C_codes/IMIS/IMIS/data_generation/data/dept_info_data.data"
generate_random_data(file_path)
print(f"随机数据已生成并保存至 {file_path}")
