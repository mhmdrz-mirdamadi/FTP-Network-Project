import socket


class Client():
    def __init__(self):
        self.cmd_list = [
            ('help', 'show this description'),
            ('list', 'folders and files list in current directory'),
            ('dwld {FILE_PATH}', 'download file from server'),
            ('pwd', 'show current directory path'),
            ('cd {DIRECTORY_NAME}', 'change the directory'),
            ('exit', 'close the FTP client')
        ]
        self.host = '127.0.0.1'
        self.port = 2121
        self.buffer_size = 2048
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def welcome(self):
        print('Welcome to the FTP client\n')
        self.help()

    def help(self):
        print('List of available commands:')
        for cmd, desc in self.cmd_list:
            print(f"{f'{cmd}':<23}{f': {desc}':<40}")

    def exit(self):
        self.socket.close()

    def main(self):
        self.welcome()
        while True:
            cmd = input('> ')
            if cmd.lower() == 'help':
                self.socket.send('help'.encode())
                self.help()
            elif cmd.lower() == 'list':
                pass
            elif cmd.lower().startswith('dwld '):
                pass
            elif cmd.lower() == 'pwd':
                pass
            elif cmd.lower().startswith('cd '):
                pass
            elif cmd.lower() == 'exit':
                self.socket.send('exit'.encode())
                self.exit()
                break
            else:
                self.socket.send(cmd.encode())
                print(
                    f"Invalid command '{cmd}'! See 'help' for list of available commands.")


myClient = Client()
myClient.main()
