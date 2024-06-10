import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        client_socket.sendall(data)
        
def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    while True:
        conn, address = server_socket.accept()
        print(f"Connected by {address}")
        
        client_thread = threading.Thread(target=handle_client, args=(conn,))
        client_thread.start()
        
if __name__ == "__main__":
    main()
    
    

                
                
           
        
   
