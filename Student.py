# My Name: Sydney Dimarco My Partner: Aiyana Race
import socket
import random
import time


listenPort=3310
localhost= 'localhost'
socket.setdefaulttimeout(120)

print("Connecting...")

#Creating a TCP
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s1.connect((localhost,listenPort))
print("Now connected to Robot")

BlazerID = input("Enter your BlazerID: ")
s1.send(BlazerID.encode())
print("BlazeID succesfully sent!")

tcp = s1.recv(1024)
tcp = int(tcp.decode())
print("Creating new socket s2")
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s2.bind((localhost ,tcp))
s2.listen(1)
s2, addr = s2.accept()
print("TCP port %d accepted" %tcp)


data = s2.recv(1024)
ddata = data.decode()
print("UDP ports %s received!!" %ddata)
portnum = ddata.split(",")
udp_rob_port = int(portnum[0])
udp_stud_port = int(portnum[1])


s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s3.bind((localhost, udp_stud_port))
num = random.randint(6,9)
s3.sendto(str(num).encode(),(localhost,udp_rob_port))
print("Sending %d using port %d" % (num,udp_rob_port))


while True: # remove potentially duplicate msg
  tcp, (localhost,udp_rob_port)  = s3.recvfrom(int(num) * 10)
  tcp = tcp.decode()
  if int(tcp) != int(num):
  	break
     
print("Received %s from port %d" %(tcp,udp_stud_port))

print("Sending UDP packets: ")
for i in range(0,5):
    s3.sendto(tcp.encode(), (localhost ,udp_rob_port))
    time.sleep(1)
    print("Packet %d sent!" %(i+1))

print("Sent!")

s1.close()
s2.close()
s3.close()
exit()
