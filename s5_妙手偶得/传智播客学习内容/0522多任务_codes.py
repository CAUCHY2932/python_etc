#-*-coding:utf-8-*-

from time import sleep

def sing():
	for i in range(3):
		print("正在唱歌...%d"%i)
		sleep(1)

def dance():
	for i in range(3):
		print("正在跳舞...%d"%i)
		sleep(1)

if __name__ == '__main__':
	sing()#唱歌
	dance()#跳舞
# 想要实现唱歌和跳舞，就必须实现多任务
# 进程的创建-fork

import os

#注意，fork函数，只在 linux上运行，Windows上不可以
pid=os.fork()
if pid ==0:
	print('哈哈1')

else:
	print('哈哈2')

执行到os.fork时会创建一个新进程，再复制父进程的所有信息到子进程中
然后父进程和子进程都会从 fork() 中得到一个返回值，在子进程中这个值一定是0，而父进程是子进程的id号
在Unix/linux操作系统中，提供了一个 fork()函数，它非常特殊
与普通函数不同， fork() 调用一次，分别向子进程和父进程返回，返回了两次
子进程永远返回0，而父进程返回子进程的ID
因为父进程可以fork出很多子进程，所以父进程要记下每个子进程的ID，而子进程只需要调用 getid() 就可以拿到父进程的ID
getid(),getppid()
import os

rpid=os.fork()
if rpid<0:
	print('fork 调用失败')
elif rpid==0:
	print('我是子进程(%s),我是父进程(%s)'%s(os.getpid(),os.get()))
	x+=1
else:
	print('我是父进程(%s),我的子进程是(%s)'%(os.getpid(),rpid))
print('父子进程都可以执行这里的代码')

