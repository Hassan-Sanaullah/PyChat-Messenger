import socket

#Creates socket and establishes connection
def Connect():
    server_ip = "127.0.0.1"
    server_port = 8080

    # Create a TCP client socket
    global client_socket 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_ip, server_port))
        print("Connected to the server.")

    except ConnectionRefusedError:
            print("Connection refused. Make sure the server is running.")
    except Exception as e:
        print("An error occurred:", str(e))

# Sending message to server
def communicate(message):

    # Send data to the server
    #message = input("Enter a message to send: ")
    if message is not None:
        client_socket.sendall(message.encode())

    # Receive data from the server
    data = client_socket.recv(1024).decode()
    print("Received from server:", data)

    return data
                    
    # if message == "exit":
    #     break

#Disconnects from server
def Disconnect():       
    # Close the socket
    client_socket.close()
