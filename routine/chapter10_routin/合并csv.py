import os
import pandas as pd
 
Path = r'/home/data/csvfiles/'          #要拼接的文件夹及其完整路径，注意不要包含中文
SaveFile_Path = r'/home/data/CompanyName/'       #拼接后要保存的文件路径
SaveFile_Name = r'all.csv'              #合并后要保存的文件名
 
 
# 修改当前工作目录
os.chdir(Path)
# 将该文件夹下的所有文件名存入一个列表
file_list = os.listdir()
# print(file_list)
 
# 读取第一个CSV文件并包含表头
df = pd.read_csv(Path + file_list[0]) 
 
# 将读取的第一个CSV文件写入合并后的文件保存
df.to_csv(SaveFile_Path + SaveFile_Name, encoding="utf_8", index=False, header=False)
 
 
# 循环遍历列表中各个CSV文件名，并追加到合并后的文件
try:
    for i in range(1, len(file_list)):
        path = Path + file_list[i]
        print(path, '    path is ok')
        df = pd.read_csv(path)
        df.to_csv(SaveFile_Path + SaveFile_Name, encoding="utf_8", index=False, header=False, mode='a+')
        
# 异常处理
except OverflowError:
    print('wrong', path)
