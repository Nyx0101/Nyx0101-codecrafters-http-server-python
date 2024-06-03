import socket

def main():
    print("Logs from your program will appear here!")
    
    try:
        # Create the server socket
        server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
        print("Server started on localhost:4221")
        
        while True:
            try:      
                # Wait for client a client connection
                conn, addr = server_socket.accept()
                print(f"Connection from {addr[0]} port {addr[1]}")
        
                # Receive data
                data = comm.recv(1024).decode("utf-8")
                print(f"Received data: {data}")
        
                # Extract the path from the HTTP request
                path = data.split(" ")[1]
        
                # Determine response based on the path
                if path == "/":
                    response = b"HTTP/1.1 200 OK\r\n\r\n"
                else:
                    response = b"HTTP/1.1 404 Not Found\rn\r\n"
            
                # Send the response
                comm.sendall(response)
                print(f"Sent response: {response}")
             
        except Exception as e:
            print(f"An error occured while handling the connection: {e}")
        finally:
            # Ensure the client socket is closed
            comm.close()
            print("Client connection closed")
        
     except Exception as e:
        print(f"An error occurred: {e}")
         
    finally:
        # Ensure the server socket is closed
        server_socket.close()
        print("Server socket closed")
     
if __name__ == "__main__":
    main()
