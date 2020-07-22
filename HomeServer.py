import socket
from Packet_Sniffer_TCP.nettypes import EthernetFrame
from Packet_Sniffer_TCP.capture import pcap

def main():
    server = socket.socket(socket.AF_INET, socket.SOCKSTREAM)
    server.bind(('',8080))
    server.listen(1)
    conn, addr = server.accept()
    pcapfile = pcap('remote.pcap')
    with conn:
        while True:
            data = conn.recv(1024)
            if data:
               pcap.write(data)
    pcapfile.close()




if __name__ == '__main__':
    main()
