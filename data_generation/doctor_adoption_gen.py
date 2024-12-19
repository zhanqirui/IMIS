import csv
import random

def generate_doctor_adoption_info(output_file):
    # 定义列名
    adoption_columns = [
        "id",  # 主码
        "module_code",  # 模块代码，固定为 MSDATA
        "dept_id",  # 部门 ID，固定为 0000
        "positive_feedback",  # 正反馈意见
        "intelligent_decision_id"  # 智能决策 ID
    ]

    # 智能决策 ID 范围
    intelligent_decision_ids = [f"INTELLI{i:06d}" for i in range(1, 1501)]

    # 正反馈意见选项
    feedback_options = ["采纳", "未采纳"]

    # 写入医生采纳信息到输出文件
    with open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(adoption_columns)

        for i, decision_id in enumerate(intelligent_decision_ids):
            adoption_id = f"ADOPT{i + 1:06d}"
            positive_feedback = random.choice(feedback_options)

            row = [
                adoption_id,  # id
                "MSDATA",  # module_code
                "0000",  # dept_id
                positive_feedback,  # positive_feedback
                decision_id  # intelligent_decision_id
            ]
            writer.writerow(row)

# 文件路径
folder_path = 'E:/C_codes/IMIS/IMIS/data_generation/data/'
output_file = "doctor_adoption_info.data"

# 生成医生采纳信息数据
generate_doctor_adoption_info(folder_path+output_file)
print(f"医生采纳信息数据已生成并保存至 {output_file}")
