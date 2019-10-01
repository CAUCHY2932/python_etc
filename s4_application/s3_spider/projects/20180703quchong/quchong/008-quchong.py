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
    li=readCSV2List('5.csv')
    try:
        cnt=0
        dictOject={}
        for item in li:
            # print(cnt)
            dictOject[cnt]=str(item[2])
            # print(item[2])
            cnt+=1
            print(cnt)
    except Exception as e:
        print('error',e)

    finally:
        return dictOject

def find_lcsubstr(s1, s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一列
    mmax = 0  # 最长匹配的长度
    p = 0  # 最长匹配对应在s1中的最后一位
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > mmax:
                    mmax = m[i + 1][j + 1]
                    p = i + 1
    return s1[p - mmax:p], mmax  # 返回最长子串及其长度

def match():
    pass

def main():
    dict=make_dict()
    print(dict)
    print(dict[1])
    print(type(dict[1]))
    match_dict=find_lcsubstr(dict[3],dict[1])
    print(match_dict)
    print(find_lcsubstr('中国长城','长城酒业'))
if __name__ == '__main__':
    main()