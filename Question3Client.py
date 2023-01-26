import socket 
def main(): 

host = "10.0.2.5 " 
port = 8888 

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sockfd.connect((host, port)) 
quote = sockfd.recv(1024) 
print("Quotes for today is -> %s" % quote.decode('utf-8')) 
sockfd.close() 
main()
