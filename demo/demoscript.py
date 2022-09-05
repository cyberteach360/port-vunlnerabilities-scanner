import pyfiglet 
import sys 
import socket 
from datetime import datetime 
   
ascii_banner = pyfiglet.figlet_format("PORT SCANNER") 
print(ascii_banner) 
   
if len(sys.argv) == 2: 
      
    target = socket.gethostbyname(sys.argv[1])  
else: 
    print("Invalid ammount of Argument you must enter the IP") 
  

print("-" * 50) 
print("Scanning Target: " + target) 
print("Scanning started at:" + str(datetime.now())) 
print("-" * 50) 

try: 
      
    for port in range(1,100): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(1) 
          
        result = s.connect_ex((target,port)) 
        if result ==0: 
            print("Port {} is open".format(port)) 
        s.close() 
          
except KeyboardInterrupt: 
        print("\n Exitting Program !!!!") 
        sys.exit() 
except socket.gaierror: 
        print("\n Hostname Could Not Be Resolved !!!!") 
        sys.exit() 
except socket.error: 
        print("\ Server not responding !!!!") 
        sys.exit() 
except NameError:
    print("Name error is happening in your python code :)") 
