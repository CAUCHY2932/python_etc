import re



def readCSV2List(filePath):
    try:
        file = open(filePath, 'r', encoding="gbk")
        context = file.read()
        list_result = context.split("\n")
        length = len(list_result)
        for i in range(length):
            list_result[i] = list_result[i].split(",")
        return list_result
    except Exception:
        print("文件读取转换失败，请检查文件路径及文件编码是否正确")
    finally:
        file.close()  # 操作完成一定要关闭

def make_dict():
    li=readCSV2List('3.csv')
    try:
        cnt=0
        dictOject={}
        for item in li:
            # print(cnt)
            dictOject[cnt]=str(item[2])
            # print(item[2])
            cnt+=1
    except Exception as e:
        print('error',e)

    finally:
        return dictOject


def match():
    pass

def main():
    dict=make_dict()
    print(dict)

if __name__ == '__main__':
    main()