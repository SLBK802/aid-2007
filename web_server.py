import re
from socket import *
from select import select
import os



class WebServer:
    def __init__(self,host="0.0.0.0",port=8200,html=None):
        self.host=host
        self.port=port
        self.html=html
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sock=socket()

        self.sock.setblocking(False)

    def bind(self):
        self.address = (self.host, self.port)
        self.sock.bind(self.address)

    def start(self):
        self.sock.listen(5)
        print("Listen the port %d"%self.port)
        self.rlist.append(self.sock)
        while True:
            rs,ws,xs=select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sock:
                    connfd, addr = self.sock.accept()
                    connfd.setblocking(False)
                    # self.home()
                    self.rlist.append(connfd)
                else:
                    try:
                        self.handle(r)
                    except:
                        r.close()
                        self.rlist.remove(r)

    def handle(self,connfd):
        data = connfd.recv(1024).decode()
        print(data)
        pattern=r"[A-Z]+\s+(?P<info>/\S*)"
        result=re.match(pattern,data)
        # request = data.split(" ")[1]
        if result:
            request=result.group("info")
            print("请求内容:",request)
            self.send_response(connfd,request)

        else:
            self.rlist.remove(connfd)
            connfd.close()
            return

    def send_response(self,connfd,request):
        if request=="/":
            filename=self.html+"/index.html"
        else:
            filename=self.html+request

        try:
            file=open(filename,"rb")
        except:
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>Sorry.....</h1>"
            response = response.encode()
        else:
            data = file.read()
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "Content-Length:%d\r\n" % (len(data))
            response += "\r\n"
            response = response.encode() + data
        finally:
            connfd.send(response)

if __name__ == '__main__':
    ws=WebServer(host="0.0.0.0",port=8200,html="./static")
    ws.start()