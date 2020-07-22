import socket




def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 65432
    #s.connect((host, port)) # Host will always be a string, port will usually be a number
    #print('Success!')
    result = s.connect_ex((host, port))
    print('Result is {}'.format(result))
    s.close()
    # Returns WinError 10061 - No Connection could be made because the target
    # machine actively refused it


if __name__ == '__main__':
    main()
