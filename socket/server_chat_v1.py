import socket
import sys
import threading


people ={}
class  sockeet():
    def __init__(self):
        self.people = {}
        self.conn = []
    
    def hope(self):
        # informação formato str + encode()
        return str('''\n> "-c<space>" comand to (create or alter) name\nex: -c Demétrios\n\n
                    "-G<space>" send mensage for all user\nex: -all Hello World\n\n
                    "-u:<name_user><space> to send msg an user\nex: -u:Demetrios Olá mundo"\n\n "-L or -l" to listen users\n\n
                            "-I OR -i" informations to hope u\n''').encode()


    def new_client(self,conn,address):
        
        def thread_function():
            #print("Connection from: " + str(address))
            while True:
                # receive data stream. it won't accept data packet greater than 1024 bytes
                data = conn.recv(1024).decode()
                datainfo=str(data[3:]).lower()
                
                command = str(data[:2]).lower()
                print(command)
                print(datainfo[2:])
        
                if conn not in self.conn:
                    self.conn.append(conn)
                    self.people[address[1]] = None
                    print(self.conn)
                    print(self.people)
                elif command == '-c':
                    self.people[address[1]]= datainfo
            
                elif command == '-l':
                        conn.send(self.hope())

                elif command == '-g':
                    print('chegou')
                    print(type(self.conn[0]))
                    for x in self.conn:
                        print(x)
                        x.send(datainfo.encode())
                
                elif command == '-u':
                    info_name = data.split()
                    name = str(info_name[1])
                    print(info_name)
                    for keys,values in self.people.items():
                        print(values)
                        if str(name) == str(values):
                            for x in self.conn:
                                if str(keys) in str(x):
                                    print("achou novamente")
                                    z=' '.join(info_name[2:])
                                    x.send(z.encode())
                else:
                    print(self.people)
                #print(self.people)
                if not data:
                    # if data is not received break
                    break
                #print("from connected" + str(address) + ": " + str(data))
                #conn.send(self.hope())  # send data to the client
                conn.send("Estamos esperando seu comando...".encode())
            conn.close()  # close the connection
            
        return threading.Thread(target=thread_function, args=())
        
    def server_program(self,num_clients):
        # get the hostname
        #host = socket.gethostname()
        people ={}
        port = 8090  # initiate port no above 1024

        server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) #SOCK_DGRAM for UDP # get instance
        # look closely. The bind() function takes tuple as argument
        server_socket.bind(('localhost', port))  # bind host address and port together
        
        while num_clients > 0:
            # configure how many client the server can listen simultaneously
            print('Server escutando... Cliente N ' + str(num_clients))
            server_socket.listen(num_clients)
            conn, address = server_socket.accept()  # accept new connection
            #print("sever_program",conn,type(conn),'\t',address[0],type(address))
            #criar nova thread para cada nova conexao
            thread_client = self.new_client(conn,address)
            thread_client.start()
            num_clients = num_clients - 1

if __name__ == '__main__':\
    
    sockeet().server_program(int(sys.argv[1]))
#cd sistemas_distribuidos/socket
#python server_chat_v1.py 1
