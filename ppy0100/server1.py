import socket
import threading
from time import  sleep
import sys
# i=input("主机ip")
print("等待连接中：")
address=("10.98.33.158",3333)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
s.bind(address)
data,addr=s.recvfrom(2048)
def send():
    while 1:
        sys.stdout.flush()
        msg=input("send:")
        if msg=="q":
            break
        s.sendto(msg.encode('utf8'),addr)

def recv():


    while 1:




        dat,addr1=s.recvfrom(2048)
        if not data:
            break
        print("\nclient:%s %s"%(addr1,dat.decode(encoding='utf-8')))
        print("按回车发送消息;")
trdr=threading.Thread(target=recv,)

trds = threading.Thread(target=send,)
trdr.start()
trds.start()
trdr.join()
trds.join()
s.close()

