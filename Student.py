# IERG3310 Project
import socket
import random
import time
import robot

listenPort=3310
localhost=''

print("Connecting...")

#Creating a TCP
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s1.connect((localhost,listenPort))
print("Now connected to Robot")

BlazerID = input("Enter your BlazerID")
s1.send(BlazerID.encode())
print("BlazeID succesfully sent!")

tcp = s1.recv(1024)
print("Creating new socket s2")
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.accept(tcp)
print("TCP port %d accepted" %tcp)


data = s2.recv(1024)
ddata = data.decode()
print("UDP ports %s received!!" %ddata)
portnum = ddata.split(",")
udp_rob_port = int(portnum[0])
udp_stud_port = int(portnum[1])

s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
num = random.randint(1,4)
s3.sendto(str(num).encode(),(localhost,udp_rob_port))
print("Sending %d using port %d" % (num,udp_rob_port))

receiveddata, addr = s3.recvfrom(1024)
recieveddata = recieveddata.decode()
print("Received %d from port %d" %(receiveddata,udp_stud_port))

print("\nSending UDP packets: ")
for i in range(0,5):
    s3.sendto(recieveddata,(localhost,udp_rob_port))
    time.sleep(1)
    print("Packet %d sent!" %(i+1))

print("Sent!")

s1.close()
s2.close()
s3.close()
exit()




