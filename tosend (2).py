	
		
import socket  
import sys



TOSENDSERVER = socket.socket() 
host = socket.gethostname()
port = 113                

TOSENDSERVER.connect((host, port))
try:
	tosend_file = open('6.mp4','rb')
	print ('File opened')
except Exception as fileerror:
	print ('Cannot open this file check this error: %s ' % str(fileerror))
Filetosend = tosend_file.read(4069)
while (Filetosend):
    print ('Sending your file...')
    TOSENDSERVER.send(Filetosend)
    Filetosend = tosend_file.read(4096)
tosend_file.close()
print ("File sended sucessfully\n clossing...")
TOSENDSERVER.close()
sys.exit('Closed by system')
