def readCSV2List(filePath):
    try:
        file = open(filePath, 'r', encoding="gbk")  # 读取以utf-8
        context = file.read()  # 读取成str
        list_result = context.split("\n")  # 以回车符\n分割成单独的行
        # 每一行的各个元素是以【,】分割的，因此可以
        length = len(list_result)
        for i in range(length):
            list_result[i] = list_result[i].split(",")
            # list_result[i].append(list_result[i].split(","))

        return list_result
    except Exception:
        print("文件读取转换失败，请检查文件路径及文件编码是否正确")
    finally:
        file.close()  # 操作完成一定要关闭

li=readCSV2List('2.csv')
# print(li)
print(len(li[0]))
print(len(li[1]))
print(len(li[2]))
print(li[0][3])