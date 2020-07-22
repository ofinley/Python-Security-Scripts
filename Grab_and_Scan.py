from port_scanner import Scanner
from grabber import Grabber
from utils import timefunc

@timefunc
def main():
    ip = '127.0.0.1'
    portrange = (1,1001)
    scanner = Scanner(ip)
    scanner.scan(*portrange)
    for port in scanner.open_ports:
        try:
            grabber = Grabber(ip,port)
            print(grabber.read())
            grabber.close()
        except Exception:
            print("Error", e)


if __name__ == '__main__':
    main()
