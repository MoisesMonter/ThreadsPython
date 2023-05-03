import socket
import sys
import threading


class ServerInfo():
    def __init__(self,localhost,port,num_clients,users):
        self.host = localhost
        self.port = port
        self.n_cli = num_clients
        self.user = users

    def hope(self):
        # informação formato str + encode()
        return str('''\n> "-c<space>" comand to (create or alter) name\nex: -c Demétrios
                "-G<space>" send mensage for all user\nex: -all Hello World
                "-u:<name_user><space> to send msg an user\nex: -u:Demetrios Olá mundo" "-L or -l" to listen users
                        "-I OR -i" informations to hope u\n''').encode()

    def new_client(self,conn,address):
        def thread_function(self):
            if str(address[0]) not in self.user:
                self.user[str(address[0])] ='noob'
                conn.send(self.hope())
            while True:
                data =conn.recv(1024).decode()
                comands= str(data[:1]).lower().strip()
                if comands == '-c' or comands == '-g' or comands == '-u' or comands == '-l' or comands == -'i':
                    pass
                    conn.send(str('seu nome é - '+data[1:]).encode())
            conn.close()
        return threading.Thread(target=thread_function, args=())

    def server_program(self):
        port = 8090
        host = 'localhost'
        server_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
        server_socket.bind((self.host,self.port))

        while self.n_cli> 0:
            print('Serveidor Escutando... Cliente N'+ str(self.n_cli))
            server_socket.listen(self.n_cli)
            #conn é a msg formato socket.socket esperando ser decodado
            # address é os endereços do cliente
            conn,address = server_socket.accept()
            print("sever_program",conn,type(conn),'\t',address[0],type(address))
            thread_client = self.new_client(conn,address)
            thread_client.start()
            #definir termino da thread o programa encerrar fora do while
            self.n_cli = self.n_cli-1


if __name__ == '__main__':
    host='localhost'
    port= 8090
    users_n = int(sys.argv[1])
    users = {}
    ServerInfo(host,port,users_n,users).server_program()