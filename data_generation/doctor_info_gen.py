import random
import csv

def generate_doctor_data(input_file, output_file):
    # 读取科室信息
    with open(input_file, mode="r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        department_data = [row for row in reader]
    with open(output_file, mode="w", encoding="utf-8") as file:
        file.truncate(0)

    # 定义列名
    doctor_columns = [
        "id",  # varchar 类型，医生工号
        "module_code",  # varchar 类型，固定为 MSDATA
        "dept_id",  # varchar 类型，固定为 0000
        "department_id",  # varchar 类型，对应科室 id
        "name",  # varchar 类型，随机生成姓名
        "gender",  # varchar 类型，随机生成性别
        "age",  # integer 类型，随机生成年龄
        "id_number",  # varchar 类型，随机生成身份证号
        "phone"  # varchar 类型，随机生成联系电话
    ]

    # 随机生成医生信息
    def random_name():
        first_names = ["张", "李", "王", "赵", "刘", "陈", "杨", "黄", "周", "吴", "郑", "冯", "朱", "沈", "韩", "马", "郭", "唐", "高", "徐"]
        last_names = [
            "伟", "芳", "娜", "敏", "静", "秀英", "丽", "强", "磊", "洋", "艳", "勇", "军", "杰", "娟", "涛", "明", "超", "秀兰", "霞", "平", "刚", "桂英", "慧", "丹", "梅", "琳", "亮", "艳丽", "旭", "玉华", "彬", "坤", "艳红", "鹏", "建华", "志强", "宇", "丽丽", "俊", "利", "峰", "飞", "艳芳", "红", "浩", "丽娟", "江", "建国"]
        return random.choice(first_names) + random.choice(last_names)

    def random_gender():
        return random.choice(["男", "女"])

    def random_age():
        return random.randint(25, 60)

    def random_id_number():
        return f"{random.randint(100000, 999999)}{random.randint(10000000, 99999999)}"

    def random_phone():
        return f"1{random.randint(3, 9)}{random.randint(100000000, 999999999)}"

    # 写入医生信息到输出文件
    with open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(doctor_columns)

        for dept in department_data:
            department_id = dept["id"]
            doctor_count = int(dept["doctor_count"])

            for i in range(doctor_count):
                doctor_id = f"DOC{department_id[2:]}{str(i + 1).zfill(4)}"
                row = [
                    doctor_id,  # id
                    "MSDATA",  # module_code
                    "0000",  # dept_id
                    department_id,  # department_id
                    random_name(),  # name
                    random_gender(),  # gender
                    random_age(),  # age
                    random_id_number(),  # id_number
                    random_phone()  # phone
                ]
                writer.writerow(row)

# 文件路径
folder_path = 'E:/C_codes/IMIS/IMIS/data_generation/data/'
input_file = "dept_info_data.data"
output_file = "doctor_info_data.data"

# 生成医生信息
generate_doctor_data(folder_path+input_file, folder_path+output_file)
print(f"医生信息已生成并保存至 {output_file}")