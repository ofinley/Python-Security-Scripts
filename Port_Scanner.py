import socket
from utils import timefunc


class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = [];

    def __repr__(self): # Returns Target
        return 'Scanner: {}'.format(self.ip)

    def add_port(self, port): # Add open ports to array
        self.open_ports.append(port)

    def scan(self, lowerport, upperport): # Scan range of ports
        print('0---Starting Port Scan---0')
        for port in range(lowerport, upperport + 1):
            if self.is_open(port):
                self.add_port(port)

    def is_open(self, port): # Create socket and attempt to connect | return result
        s = socket.socket() # socket.socket(socket.AF_INET, socket.SOCK_STREAM)                    
        result = s.connect_ex((self.ip, port)) # Faster to bind to port but no error code available - s.bind((self.ip, port))
        print('Port {}:    {}'.format(port,result))
        s.close()
        return result == 0

    def write(self, filepath): # Write output to file
        openport = map(str, self.open_ports)
        with open(filepath, 'w') as f:
            f.write('\n'.join(self.open_ports))




@timefunc
def main():
    ip = '127.0.0.1' # Change to Target IP
    scanner = Scanner(ip)
    scanner.scan(1,100)
    print(scanner.open_ports)

    

if __name__ == '__main__':
    main()
