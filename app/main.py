import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 4221))
server_socket.listen(5)

print("Server started. Waiting for connections...")

def handle_req(req):
    try:
        headers = req[0].decode().split("\r\n")
        user_agent = [header.split(": ")[1] for header in headers if "User-Agent" in header]
        if user_agent:
            user_agent = user_agent[0]
        else:
            user_agent = "Unknown"
        
        # Do something with the user_agent
        print(user_agent)
    except Exception as e:
        print(f"An error occurred: {e}")

def handle_client(client_socket):
    while True:
        req = client_socket.recv(1024)
        if not req:
            break
        handle_req(req)
        client_socket.sendall(b"HTTP/1.1 200 OK\r\n\r\n")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connected by {addr}")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

    
    

                
                
           
        
   
