import socket
import threading

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn, address = server_socket.accept()
def handle_request(conn):
    with conn:
        data = conn.recv(4096)
        parsed_request = str(data.decode()).split()
        method, path, *_ = parsed_request
        
        if path =="/":
            conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
        elif path.startswith("/echo") or path.startswith("/user-agent"):
        if path.startswith("/echo"):
            body = path.split("/")[-1]
        else:
            body = parsed_request[parsed_request.index("User-Agent:") + 1]
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(body)}\r\n\r\n{body}"
        conn.sendall(response.encode())
    else:
        conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")
        
        
def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True) 
    
    while True:
        conn, address = server_socket.accept()
        thread = threading.Thread(target=lamda: handle_request(conn))
        thread.start()
        
        
if __name__ == "__main__":
    main()
    
    

                
                
           
        
   
