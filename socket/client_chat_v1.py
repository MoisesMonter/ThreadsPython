import socket
import threading


def main():

    port = 8090  # socket server port number
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)  # instantiate
    client_socket.connect(('localhost', port))

    t1 = threading.Thread(target=send, args=(client_socket,port), name="Thread#1")
    t1.start()

    t2 = threading.Thread(target=recive, args=(client_socket,port), name="Thread#2")
    t2.start()


def send(client_socket,port):
    #host = socket.gethostname()  # as both code is running on same pc
      # connect to the server
    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message


        message = input(" -> ")  # again take input
    client_socket.close()  # close the connection

def recive(client_socket,port):
    print('chegamos em recive')
    data=''
    while data != 'bye':

        data = client_socket.recv(1024).decode()  # receive response
        if len(data)>1:
            print(data)
            data =''
    client_socket.close()  # close the connection

def client_program(client_socket):
    #host = socket.gethostname()  # as both code is running on same pc
    
    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    main()
    #cd sistemas_distribuidos/socket
    #python client_chat_v1.py