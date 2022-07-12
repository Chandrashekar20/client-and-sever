import socket
def server_program():
    host=socket.gethostname()
    port=5000
    server_socket=socket.socket()
    server_socket.bind((host,port))
    server_socket.listen(2)
    con,address=server_socket.accept()
    print("connection from "+str(address))
    while(True):
        data=con.recv(1024).decode()
        if not data:
            break
        print("from connected user:"+str(data))
        data=str(data).upper()
        con.send(data.encode())
    con.close()
server_program()
