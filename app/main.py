import socket

def main():
    try:
        # Create the server socket
        server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
        print("Server started on localhost:4221")
        
        # Wait for client a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        # Send HTTP response with correct escape sequences
        response = b"HTTP/1.1 200 OK\r\n\r\n"
        client_socket.sendall(response)
        print("Response sent")
        
        # Close the client socket
        client_socket.close()
        print("Client connection closed")
        
    except Exception as e:
        print(f"An error occured: {e}")
        
    finally:
        # Close the server socket
        server_socket.close()
        print("Server socket closed")
     
if __name__ == "__main__":
    main()
