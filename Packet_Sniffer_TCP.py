# ofinley
import socket
from pcap import PCAPFile
from Net_Types import EthernetFrame, IPHeader, UDPSegment
# Only tested with Linux!


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    #pcap = PCAP('packets.pcap')
    while True:
        raw_data, addr = conn.recvfrom(65535)
        ethframe = EthernetFrame(raw_data)
        #print(ethframe)
        if ethframe.protocol == 8:
            ipheader = IPHeader(ethframe.leftover_data)
            print(ipheader)
            if upheader.protocol == 6:
                tcp = TCPSegment(ipheader.leftover_data)
                if tcp.src_port == 80:
                    print(tcp)
                elif ipheader.protocol == 17:
                    udp = UDPSegment(ipheader.leftover_data)
                    print(udp)
        #pcap.write(raw_data)
    #pcap.close()


if __name__ == '__main__':
    main()
