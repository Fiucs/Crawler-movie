import threading
import socket
def newclient(client,addr):
    s=threading.Thread(target=send1,args=(client,))
    r=threading.Thread(target=receve,args=(client,))
    s.start()
    r.start()
    s.join()
    r.join()
    client.close()

def send1(client):
    while 1:
        dat = input("我:")
        client.send(dat.encode(encoding='gbk'))


def receve(client):
    while 1:
        dat=client.recv(1024)
        dat=dat.decode(encoding='gbk')
        print("\nclient:%s\n"%dat)


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    addrin = ("10.98.33.158", 8888)
    server.bind(addrin)
    server.listen(10)
    while 1:
        print("等待连接：：：：\n")
        client,addr = server.accept()
        th=threading.Thread(target=newclient,args=(client,addr))
        th.start()

