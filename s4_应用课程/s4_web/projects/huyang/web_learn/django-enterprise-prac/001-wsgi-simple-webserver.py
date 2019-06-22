# -*-coding:utf-8-*-
__author__='yang'


# encode()
# decode()

import socket




def handle_connection(conn, addr):
    request=''

    EOL1='\n\n'
    EOL2='\n\r\n'
    body='''hello world,<h1>created by yang</h1>'''
    response_params=[
        'HTTP/1.0 200 OK',
        'Date: Sat, 10 jun 2017 01:01:01 GMT',
        'Content-Type: text/plain; charset=utf-8',
        'Content-Length: {}\r\n'.format(len(body)),
        body,
    ]
    response='\r\n'.join(response_params)
    while EOL1 not in request and EOL2 not in request:
        # request +=conn.recv(1024)
        request +=str(conn.recv(1024).decode())

    print(request)
    # conn.send(response)
    conn.send(response.encode())

    conn.close()







def main():
    serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    serverSocket.bind(('127.0.0.1',9000))

    serverSocket.listen(1)

    print('http://127.0.0.1:9000')


    try:
        while True:
            conn, address = serverSocket.accept()
            handle_connection(conn, address)

    finally:
        serverSocket.close()


if __name__=='__main__':
    main()