# import socket module
from socket import *
# In order to terminate the program
import sys
from datetime import datetime
# import os

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM) #TCP socket
  #-------------------------------------------SOCK_DGRAM:  indicates it is a UDP socket
  #-------------------------------------------SOCK_STREAM: indicates it is a TCP socket
  
  #Prepare a server socket
  #serverSocket - the welcoming door; TCP socket object
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)
  print('The server is ready to recieve')
  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    #connectionSocket - new socket dedicated to client making the connection
    connectionSocket, addr = serverSocket.accept()
    
    try:
      message = connectionSocket.recvfrom(1024)[0].decode()
      print("PRINTING MESSAGE FROM CLIENT")
      print(message)
      print() 
      filename = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], "rb")  #fill in start #fill in end)
      #fill in end
      

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 
              
      #Content-Type is an example on how to send a header as bytes. There are more!
      time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
      time = time.encode('utf-8')
      # print(time)
      # file_size = os.path.getsize(filename[1:]).encode()

      response = b"HTTP/1.1 200 OK\r\n"
      access_control_allow_origin = b"Access-Control-Allow-Origin: *\r\n"
      connection = b"Connection: keep-alive\r\n"
      date_time = b"Date: " + time + b"\r\n"
      server = b"Server: Apache HTTPD on OpenShift\r\n" 
      content_type = b"Content-Type: text/html; charset=UTF-8\r\n"
      content_length = b"Content-Length: 151\r\n"
      blank_line = b"\r\n"

      http_response = response + access_control_allow_origin + connection + date_time + server + content_type + content_length + blank_line

      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
 
      #Fill in end
               
      for i in f: #for line in file
        http_response = http_response + i
      
      print("PRINT RESPONSE FROM SERVER")
      print(http_response)
      print()
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!

      # Fill in start
      connectionSocket.send(http_response)
      # connectionSocket.send(http_response.encode())
      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
      time = time.encode('utf-8')

      response = b"HTTP/1.1 404 Not Found\r\n"
      connection = b"Connection: close\r\n"
      date_time = b"Date: " + time + b"\r\n"
      server = b"Server: Apache HTTPD on OpenShift\r\n" 
      content_type = b"Content-Type: text/html; charset=UTF-8\r\n"
      content_length = b"Content-Length: 0\r\n"
      blank_line = b"\r\n"

      http_response = response + connection + date_time + server + content_type + content_length + blank_line
      print("PRINT RESPONSE FROM SERVER")
      print(http_response)
      print()
      
      connectionSocket.send(http_response)
      # connectionSocket.send(http_response.encode())
      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
