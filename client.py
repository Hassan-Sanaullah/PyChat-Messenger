import socket

def socketCall(message, loop):
    # Server IP and port
    server_ip = "127.0.0.1"
    server_port = 8080

    # Create a TCP client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_ip, server_port))
        print("Connected to the server.")

        
        if loop == True:
            # Send data to the server
            #message = input("Enter a message to send: ")
            client_socket.sendall(message.encode())

            # Receive data from the server
            data = client_socket.recv(1024).decode()
            print("Received from server:", data)

            
            # if message == "exit":
            #     break

    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Close the socket
        client_socket.close()

# if __name__ == '__main__':
#     main()
