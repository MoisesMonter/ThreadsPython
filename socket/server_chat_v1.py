import socket
import sys
import threading


people ={}
class  sockeet():
    def __init__(self):
        self.people = {}
    
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
                #print("new_client",data,type(data),'\t',address,type(address))
                if str(address[0]) not in self.people:
                    self.people ={str(address[0]):None}
                    conn.send(self.hope())
                else:
                    print(str(data[:2]).lower())
                    if str(data[:2]).lower() == '-c':
                        if str(data[2:3]) == " ":
                            self.people[address[0]]= data[3:]
                        else:
                            self.people[address[0]]= data[2:]
                    elif str(data[:2]).lower() == '-l':
                        conn.send(self.hope())
                    else:
                        conn.send(str(self.people[address[0]])+"Estamos esperando seu comando...".encode())
                print(self.people)
                if not data:
                    # if data is not received break
                    break
                print("from connected" + str(address) + ": " + str(data))
                #conn.send(self.hope())  # send data to the client
                conn.send(str(self.people[address[0]])+"Estamos esperando seu comando...".encode())
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
#python server_chat_v1.py 3
