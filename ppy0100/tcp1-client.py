import socket
import threading


def sends(client):
    while 1:
        dat = input("我:")
        if 'q' == dat:
            break
        client.send(dat.encode(encoding='utf-8'))
    client.close()


def recvs(client):
    while 1:
        dat = client.recv(1024)
        dat = dat.decode(encoding='utf-8')

        if not dat:
            break
        print("\nserver:%s\n" % (dat,))
    client.close()


if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    serveraddr = ("10.98.33.158", 8888)
    client.connect(serveraddr)

    s = threading.Thread(target=sends, args=(client,))
    r = threading.Thread(target=recvs, args=(client,))
    s.start()
    r.start()
    s.join()
    r.join()

    client.close()
