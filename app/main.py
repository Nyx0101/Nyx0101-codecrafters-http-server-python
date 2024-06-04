import socket


def handle_client(client_socket):
    message = client_socket.recv(1024).decode()
    response = "HTTP/1.1 404 Not Found\r\n\r\n"
    url_path = message.split("\r\n")[0].split(" ")[1]
    print(url_path)
    if url_path == "/"  or url_path == "/index.html":
        response = "HTTP/1.1 200 OK\r\n\r\n"
    elif: url_path.split("/")[1] == "echo":
        content = url_path.split("/")[2]
        content_length = len(content)
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {0}\r\n\r\n{1}".format(
            content_length, content
        )
        
    client_socket.sendall(response.encode())
    
    
def main():
    print("Logs from your program will appear here!")
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    try:
        while True:
            client_socket, address = server_socket.accept()
            
            handle_client(client_socket)
            
            client_socket.close()
    except Exception as e:
        print(e)
    finally:
        server_socket_close()
        
if __name__ == "__main__":
    main()    
        
         
