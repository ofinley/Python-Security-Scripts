import socket




def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    host = 'localhost' # Filler host address for example
    port = 8080
    forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    forward.connect((host,port))
    while True:
        data, addr = conn.recvfrom(65535)
        if data:
            foward.sendall(data)



if __name__ = '__main__':
    main()
