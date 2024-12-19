import random
import csv

def generate_patient_data(output_file, num_rows=500):
    # 定义列名
    patient_columns = [
        "id",  # varchar 类型，病人号
        "module_code",  # varchar 类型，固定为 MSDATA
        "dept_id",  # varchar 类型，固定为 0000
        "name",  # varchar 类型，随机生成姓名
        "gender",  # varchar 类型，随机生成性别
        "age",  # integer 类型，随机生成年龄（1到120）
        "id_number",  # varchar 类型，随机生成身份证号
        "phone",  # varchar 类型，随机生成联系电话
        "emergency_contact"  # varchar 类型，紧急联系人联系方式
    ]

    # 随机生成病人信息
    def random_name():
        first_names = ["张", "李", "王", "赵", "刘", "陈", "杨", "黄", "周", "吴", "郑", "冯", "朱", "沈", "韩", "马", "郭", "唐", "高", "徐", "许", "何", "邓", "林", "胡", "罗", "梁", "宋", "郑", "曹"]
        last_names = [
            "伟", "芳", "娜", "敏", "静", "秀英", "丽", "强", "磊", "洋", "艳", "勇", "军", "杰", "娟", "涛", "明", "超", "秀兰", "霞", "平", "刚", "桂英", "慧", "丹", "梅", "琳", "亮", "艳丽", "旭", "玉华", "彬", "坤", "艳红", "鹏", "建华", "志强", "宇", "丽丽", "俊", "利", "峰", "飞", "艳芳", "红", "浩", "丽娟", "江", "建国", "博", "楠", "琪", "娴"]
        return random.choice(first_names) + random.choice(last_names)

    def random_gender():
        return random.choice(["男", "女"])

    def random_age():
        return random.randint(0, 120)

    def random_id_number():
        return f"{random.randint(100000, 999999)}{random.randint(10000000, 99999999)}"

    def random_phone():
        return f"1{random.randint(3, 9)}{random.randint(100000000, 999999999)}"

    def random_emergency_contact():
        return f"1{random.randint(3, 9)}{random.randint(100000000, 999999999)}"

    # 写入病人信息到输出文件
    with open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(patient_columns)

        for i in range(num_rows):
            patient_id = f"PAT{i + 1:06d}"
            row = [
                patient_id,  # id
                "MSDATA",  # module_code
                "0000",  # dept_id
                random_name(),  # name
                random_gender(),  # gender
                random_age(),  # age
                random_id_number(),  # id_number
                random_phone(),  # phone
                random_emergency_contact()  # emergency_contact
            ]
            writer.writerow(row)

# 文件路径
folder_path = 'E:/C_codes/IMIS/IMIS/data_generation/data/'
output_file = "patient_info_data.data"

# 生成病人信息
generate_patient_data(folder_path+output_file, num_rows=500)
print(f"病人信息已生成并保存至 {output_file}")
