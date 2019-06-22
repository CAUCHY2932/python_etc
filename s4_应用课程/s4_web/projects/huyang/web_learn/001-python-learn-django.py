# -*-coding:utf-8 -*-
__author__='yang'

from wsgiref import simple_server

# 定义一个输出hello world和环境变量的简单web应用程序

def hello_app(environ, start_response):
    # 输出http头，text/plain 表示是纯文本
    start_response('200 OK',[('Context-type','text/plain')])
    # 准备输出的内容
    content=[]
    content.append('hello world')

    for key,value in environ.items():
        content.append('hello world')
    # 输出，根据wsgi协议，返回的需要一个迭代器，返回一个list即可

    return ['\n'.join(content)]

# 构造开发服务器对象，设置绑定的地址和端口，并把hello world应用程序传给他
server=simple_server.make_server('localhost',8080,hello_app)

server.server_forever()