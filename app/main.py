import socket


def main():
    print("Logs from your program will appear here!")
    
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
        
    conn, addr = server_socket.accept()
    print(f"Connection from {addr[0]} port {addr[1]}")
        
    data = conn.recv(1024).decode("utf-8")
    print(data)
        
    path = data.split(" ")[1]
        
    if path == "/":
        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    else:
        conn.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
        print(f"Sent response: {response}")
     
if __name__ == "__main__":
    main()
