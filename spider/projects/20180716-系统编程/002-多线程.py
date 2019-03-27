# coding:utf-8
from threading import Thread
import time

def saySorry():
    print("亲爱的")
    time.sleep(1)

if __name__=="__main__":
    for i in range(5):
        t=Thread(target=saySorry)
        t.start()

