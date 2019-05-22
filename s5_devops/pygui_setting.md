# python gui开发

pycharm和pyqt5
>https://blog.csdn.net/zhangziju/article/details/80243858

## 环境配置
pip install PyQt5 -i https://pypi.douban.com/simple
pip install PyQt5-tools -i https://pypi.douban.com/simple

在pycharm，然后在设置里面点击external tools，点击“+”，需要添加Qt Designer 和pyuic 两个选项。


 ### Qt Designer
 
    Name：可自己定义
    program：Qt Designer的安装路径
    parameter：不填
    directory： $FileDir$

### pyuic

    Name：可自己定义
    program：pyuic的安装路径
    parameter：$FileName$ -o $FileNameWithoutExtension$.py

    directory： $FileDir $



## 教程


完成之后可以在pycharm中的外部工具打开qtdesigner
生成的ui文件必须是在工程文件的根目录中，然后使用pyuic生成Python文件
