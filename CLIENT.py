import socket                

serverDS = 0 #Remaining bytes in data (Eventually going to be used to know when packets are fully sewn (When packet cutoff bug is fixed))
sewnPackets = ""
s = socket.socket()
port = 8000                
  
s.connect((socket.gethostbyname(socket.gethostname()), port)) 
  
while True:
    packet = s.recv(16).decode() #Set to 16 bytes to debug packet sewing
    if packet != "":
        isPCoded = True #a pcode is the code before the actual data (i.e: "nbSNDS//;;[[1036", this just tells us that the next chunk of data will contain 1036 bytes,
        try:            #if there is no pcode, a datachunk containing "//;;[[", the data will have no pcode and will be recognized as pure data sent from server)
            packetPrefix = packet[0:packet.index("//;;[[")] #Getting pcode from datachunk
        except ValueError:
            isPCoded = False #Declares packet(s) not pcoded, did not find "//;;[["
        if isPCoded:
            if packetPrefix == "nbSNDS": #[nobyte] STATE NEXT DATA SIZE
                serverDS = int(packet[packet.find("//;;[[")+1:])
                print(packet)
        else:
            if not serverDS == 0:
                sewnPackets += packet #Sew packets together
            serverDS -= len(packet)
            print(sewnPackets) #Print final result as building for debugging

s.close()
