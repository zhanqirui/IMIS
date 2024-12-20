import csv

def generate_medical_knowledge(output_file):
    # 定义列名
    knowledge_columns = [
        "id",  # 主码
        "module_code",  # 模块代码，固定为 MSDATA
        "dept_id",  # 部门 ID，固定为 0000
        "medical_knowledge_content"  # 医疗知识内容
    ]

    # 医学知识描述库扩展到100条
    knowledge_pool = [
        "中医认为，穴位按摩能够改善血液循环，促进人体自愈能力。",
        "西医临床实践表明，抗生素的正确使用可以有效治疗细菌感染。",
        "胃镜检查是消化系统疾病的重要诊断工具，用于观察胃部病变。",
        "中药调理对慢性支气管炎患者具有良好的疗效，能够改善咳嗽症状。",
        "根管治疗是牙髓疾病的一种常见治疗方法，能够保存天然牙齿。",
        "CT 检查在肿瘤早期筛查中具有重要价值，能够清晰显示病灶位置。",
        "针灸治疗偏头痛在中医中被广泛应用，具有缓解疼痛的效果。",
        "胃溃疡患者在饮食中应避免刺激性食物，以减少胃黏膜损伤。",
        "核磁共振成像是诊断神经系统疾病的重要工具，特别适用于脑部检查。",
        "口腔溃疡反复发作可能与免疫系统功能失调有关，应注重补充维生素。",
        "高血压患者需要长期监测血压，并遵医嘱服用降压药物。",
        "中药汤剂对改善失眠症状具有较好的作用，常用于神经衰弱患者。",
        "心电图是诊断心律失常的基础检查，能够提供心脏功能的关键信息。",
        "艾灸治疗在中医中常用于改善寒性体质，特别适合腰背疼痛患者。",
        "现代医学证明，合理的运动有助于预防骨质疏松和提高骨密度。",
        "牙周炎治疗需要结合洁治和药物控制，以改善牙龈健康。",
        "肝功能检查是评估肝脏健康状况的重要指标，适用于多种肝病筛查。",
        "推拿治疗颈椎病在中医中被广泛应用，具有缓解肌肉紧张的效果。",
        "心血管疾病患者应控制饮食中的盐分摄入量，以降低心脏负担。",
        "消化道内窥镜检查在诊断胃癌早期病变中具有重要作用。",
        "胃食管反流病患者可以通过调整生活方式来减轻症状。",
        "中药外敷在治疗跌打损伤方面具有显著疗效。",
        "产后康复训练可以帮助新妈妈恢复盆底肌功能。",
        "糖尿病足的护理需避免足部受伤，并保持清洁干燥。",
        "人工关节置换术是治疗严重关节炎的一种有效方法。",
        "中医拔罐疗法被认为可以疏通经络，缓解肌肉酸痛。",
        "牙齿矫正治疗需要长期坚持，以达到最佳效果。",
        "肺功能检查是评估慢性阻塞性肺疾病的常用手段。",
        "中药熏蒸对治疗关节炎具有一定的辅助作用。",
        "视网膜脱离需要尽早手术治疗，以防止视力永久丧失。",
        "孕期营养摄入需要平衡，避免体重增长过快。",
        "针灸治疗过敏性鼻炎具有缓解鼻塞和打喷嚏的效果。",
        "肾结石患者应增加饮水量，减少草酸盐摄入。",
        "乳腺癌早期筛查建议定期进行乳腺超声检查。",
        "脑卒中康复治疗包括物理治疗和语言训练。",
        "脊柱侧弯的矫正需要根据病情选择支具或手术。",
        "慢性肾病患者应注意低蛋白饮食，以减轻肾脏负担。",
        "中药足浴对改善睡眠和缓解疲劳具有一定作用。",
        "耳鸣的治疗可以结合药物和心理干预。",
        "骨折愈合期间需要补充足够的钙质和维生素D。",
        "老年人应定期进行骨密度检测，预防骨质疏松。",
        "心脏起搏器植入术适用于严重心律失常患者。",
        "慢性胃炎患者应避免过冷过热食物刺激胃黏膜。",
        "冠心病患者应控制胆固醇摄入，并定期复查。",
        "儿童龋齿可以通过涂氟和窝沟封闭预防。",
        "高尿酸血症患者应限制嘌呤摄入，减少痛风发作。",
        "肝硬化患者应避免饮酒，并定期进行超声检查。",
        "老年痴呆患者的护理应注重安全和心理健康。",
        "咽炎的治疗可以采用含漱液和抗炎药物。",
        "骨关节炎患者的日常锻炼应避免过度负重。",
        "肠镜检查是诊断结直肠癌的重要手段。",
        "孕期糖尿病需要通过饮食控制和血糖监测进行管理。",
        "中药贴敷疗法对治疗颈肩疼痛有一定效果。",
        "急性阑尾炎通常需要手术切除治疗。",
        "甲状腺功能异常可以通过药物进行调节。",
        "婴幼儿湿疹护理应避免使用刺激性清洁产品。",
        "高脂血症患者应减少饱和脂肪酸摄入，增加膳食纤维。",
        "骨髓移植是治疗某些血液病的根本方法。",
        "慢性咽炎患者应避免长期使用嗓子和接触烟雾。",
        "黄斑病变患者应注意保护视力，避免强光刺激。",
        "腱鞘炎的治疗包括休息、理疗和药物治疗。",
        "心理咨询对缓解焦虑和抑郁具有重要作用。",
        "胆结石患者应避免油腻食物，增加膳食纤维摄入。",
        "鼻窦炎的治疗包括抗生素和鼻腔冲洗。",
        "风湿性关节炎患者应定期复查关节功能。",
        "皮肤癌的早期发现可以通过定期体检和皮肤镜检查。",
        "支气管哮喘的控制需要长期使用吸入激素。",
        "艾滋病的预防需避免高危行为，并进行必要的筛查。",
        "癫痫患者应遵医嘱规律服药，避免诱发因素。",
        "脂肪肝的治疗包括减重和调整饮食结构。",
        "老年白内障的手术治疗可以显著改善视力。",
        "胃肠功能紊乱患者应注意饮食规律，避免过饱过饿。",
        "偏头痛的治疗包括药物干预和生活方式调整。",
        "中药热敷疗法在缓解腰肌劳损方面具有一定作用。",
        "卵巢囊肿患者需要定期超声检查，以监测囊肿变化。",
        "甲型流感的预防建议接种流感疫苗。",
        "尿路感染患者应多饮水，促进排尿。",
        "肛裂的治疗包括温水坐浴和外用药物。",
        "冠状动脉支架植入术是治疗冠心病的重要手段。",
        "血液透析是治疗终末期肾病的重要方法。",
        "腰椎间盘突出症的治疗包括牵引和物理治疗。",
        "直肠癌手术后需要定期复查肿瘤标志物。",
        "脂肪瘤一般无需治疗，但需定期观察是否增大。",
        "慢性咳嗽患者需排除结核、哮喘等病因。",
        "梅毒的治疗应尽早进行青霉素注射。",
        "儿童多动症的干预包括行为治疗和药物治疗。",
        "肿瘤标志物检测在癌症筛查中具有重要作用。",
        "中药止咳糖浆对缓解感冒引起的咳嗽具有一定效果。",
        "老年人应定期进行眼压检查，预防青光眼。",
        "盆腔炎的治疗包括抗生素和物理治疗。",
        "慢性鼻炎患者应避免接触过敏原，改善环境卫生。",
        "腰肌劳损患者需注意休息，避免长时间弯腰。",
        "红斑狼疮患者的日常护理需注重防晒和感染预防。",
        "痛风性关节炎的急性发作可用非甾体抗炎药缓解疼痛。",
        "骨肉瘤患者的治疗包括手术切除和化疗。",
        "更年期综合征患者可以通过中药调理和心理支持缓解症状。",
        "肺癌患者的治疗包括手术、放疗和化疗。",
        "腹股沟疝的治疗一般需要进行手术修补。",
        "慢性疲劳综合征患者需注意均衡营养和适度运动。"
    ]

    # 写入医疗知识到输出文件
    with open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(knowledge_columns)

        for i, knowledge in enumerate(knowledge_pool):
            knowledge_id = f"KNOW{i + 1:06d}"
            row = [
                knowledge_id,  # id
                "MSDATA",  # module_code
                "0000",  # dept_id
                knowledge  # medical_knowledge_content
            ]
            writer.writerow(row)

# 文件路径
folder_path = 'E:/C_codes/IMIS/IMIS/data_generation/data/'
output_file = "medical_knowledge.data"

# 生成医疗知识数据
generate_medical_knowledge(folder_path+output_file)
print(f"医疗知识数据已生成并保存至 {output_file}")