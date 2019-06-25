import socket
import threading
# i=input("serverip")

addr=("10.98.33.158",3333)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
s.sendto("it is me".encode(encoding='utf-8'),addr)
def recv():
    while 1:
        print("按回车发送消息")
        msg,add=s.recvfrom(2048)
        if msg=="q":
            break
        print("recve:%s"%(msg.decode(encoding='utf-8')))

trd = threading.Thread(target=recv,)
trd.start()
while 1:
    dat=input("send:")
    if dat=="q":
        break
    s.sendto(dat.encode(encoding='utf-8'),addr)

s.close()