import socket

def soc():
	msgFromClient       = "Hello UDP Server"
	bytesToSend         = str.encode(msgFromClient)
	serverAddressPort   = ("192.168.4.1", 989)
	bufferSize          = 1024
	# Create a UDP socket at client side
	UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	# Send to server using created UDP socket
	UDPClientSocket.sendto(bytesToSend, serverAddressPort)
	while 1:
		msgFromServer = UDPClientSocket.recvfrom(bufferSize)
		msg = "Message from Server {}".format(msgFromServer[0])
		print(msg)