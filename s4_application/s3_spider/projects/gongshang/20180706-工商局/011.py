import re
# f=open(r'C:\Users\lenovo\Desktop\1.txt','r',encoding='utf8')
f=open(r'2.txt','r',encoding='utf8')

m= re.compile(u"[\u4e00-\u9fa5]+")
p=open(r'3.txt','w',encoding='utf8')
for line in f.readlines():
    list=re.findall(m,line)
    for i in list:
        if i!='宋体':
            p.write(i)
    p.write('\n')
p.close()
f.close()