import socket
from threading import Thread

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address="127.0.0.1"
port=8000

server.bind((ip_address,port))
server.listen()

list_of_clients=[]
questions=["When did Disney-Pixar merge and are they still together?\n a.2016,yes\n b.2006,yes \n c.2016,no \n d.2006,no",
"What was the first Disney-Pixar movie?\n a.Encanto\n b.Iron man \n c.Ratatoullie \n d.Toy story"]
print("server has started")

def clientThread(conn,nickname):
    conn.send("welcome to the chat room".encode('utf-8'))
    while True:
        try:
            message=conn.recv(2048).decode("utf-8")
            if message:
                print(message)
                # print("<"+addr[0]+">"+message)
                # message_to_send="<"+addr[0]+">"+message
                broadcast(message,conn)
            else:
                remove(conn)
                remove_nickname(nickname)
        except:
            continue

def broadcast(message,connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message.encode("utf-8"))
            except:
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

def remove_nickname(nickanme):
    if nickname in nicknames:
        nicknames.remove(nickname)
        

while True:
    conn,addr=server.accept()
    conn.send("NICKNAME".encode("utf-8"))
    nickname=conn.recv(2048).decode("utf-8")
    list_of_clients.append(conn)
    nicknames.append(nickname)
    message="{} joined".format(nickname)
    print(message)
    broadcast(message,conn)
    new_thread=Thread(target=clientThread,args=(conn,nickname))
    new_thread.start()
    
