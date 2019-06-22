import re
import csv

with open('2.csv','r')as f:
    # f.readline()
    cont=0
    for line in f.readlines():
        # li=list(line)
        # print(li)
        cont+=1
        print(line)
    print(cont)
    # print(f.readlines()[0])
    # print(f.readlines()[2])