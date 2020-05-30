import socket                
  

s = socket.socket() #Create stream     
print("Socket established")

port = 8000                
  
s.bind(('', port)) #Bind stream to port    
print("socket binded to port %s" %(port))
  
s.listen(5) #Listen for incoming connections
print("Socket is listening...")         
  
def send(sock, data, pcode=None): #Send data to client function (data packing)
   extras = ""
   if pcode:
      extras = f"{pcode}//;;[[" #Formats data with pcode if supplied
   newdata = f"{extras}{data}"
   sock.send(newdata.encode()) #Actually sends the data over to the recipient
def sendData(sock,data):
   send(c, str(len(data)), "nbSNDS") #Basically just specifies the length of the next message so the client can sew the packets together.
   send(c, data) #Sends the data to the client
while True: 
   c, addr = s.accept()      
   print('Established connection with', addr)
   sendData(c, "You've been eyeing me all day and waiting for your move like a lion stalking a gazelle in a savannah.") #Sends a pre-randomly-generated sentence
   sendData(c, "They say that dogs are man's best friend, but this cat was setting out to sabotage that theory.") #Same as above

   c.close() 
