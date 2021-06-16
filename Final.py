import sys
import hashlib
import re
import socket
from datetime import datetime
import urllib.request
import json


#########-----------OPTION 1: COMPARE MD5()--------------###########
def hashfile(file):
    BUF_SIZE = 65536
    ### this will create md5 hash object using hashlib library 
    md5 = hashlib.md5()
    try:
        with open(file, 'rb') as f:
         
            while True:
                #reading the file from current location
                data = f.read(BUF_SIZE)
                if not data:
                    break
                md5.update(data)
    except IOError:
        print("Can't Read file ",file)
        return False
    
    return md5.hexdigest()
 
### this is the driver function for md5 hash and comparinng it to the use entered hash
def comparemd5File():
    ###File Entered  by User
    f1_hash=hashfile(input("Enter File Name: "))
    if f1_hash==False:
        return
    #hash entered by user
    f2_hash=input("Enter hash to compare with: ") 
    if f1_hash == f2_hash:
        print("Both are same")
        print(f"Hash: {f1_hash}")
 
    else:
        print("Both are different!")
        print(f"Hash of File 1: {f1_hash}")
        print(f"Given Hash: {f2_hash}")
        


regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

"""This method will check if the IPv4 Address is correct or not 
    """
def check(Ip):
    #verify if the given ip address is according to the pattern described in regex above
    if(re.search(regex, Ip)):
        return True
         
    else:
        return False
    
############------------------OPTION 2: REVERSE DNS LOOKUP-----------###########




def getHost(ip):
    """
    This method returns the 'True Host' name for a
    given IP address
    """
    try:
        data = socket.gethostbyaddr(ip)
        host = repr(data[0])
        return host
    except Exception:
        # fail gracefully
        return False
    
    
################--------OPTION 3: PORT SCANNER-------------#############

def portScanner(ip:str):
    
    target = socket.gethostbyname(ip)


    # Add Banner
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)
    
    #list of ports to be scanned defined in instructions
    portslist=[20,22,23,80,445]

    try:
    	#for loop to iterate ove the list of pots to scan
    	for port in portslist:
            #creating socket object to check make a connection with the target ip address
    		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    		socket.setdefaulttimeout(1)
    		#connect to the port on the target ip address.
    		# returns an error indicator
    		result = s.connect_ex((target,port))
    		if result ==0:
    			print("Port {} is open".format(port))
    		s.close()
    		
    except KeyboardInterrupt:
    		print("\n Exitting Program !!!!")
    		return
    except socket.gaierror:
    		print("\n Hostname Could Not Be Resolved !!!!")
    		return
    except socket.error:
    		print("\ Server not responding !!!!")
    		return

##########-------------OPTION 4: IP GEOLOCATION--------############

#this function uses API named ipgeolocation to get geolocation of given ip address
def ipgeo(ip:str):
    with urllib.request.urlopen("https://geolocation-db.com/jsonp/{}".format(ip)) as url:
        data = url.read().decode()
        data = data.split("(")[1].strip(")")
        data=json.loads(data)
        for key,value in data.items():
            print(key,": ",value)

    
    
###############---------EXECUTING BODY---------########

## Menu for options to perform different operations.
try:
    while True:
        print("\n1: MD5 HASH")
        print("\n2: Reverse DNS Lookup")
        print("\n3: Open Port Scan")
        print("\n4: IP Geolocation")
        print("\n5: Quit")
        choice=int(input("\nPlease enter your choice:"))
    
        if choice==1:
            comparemd5File()
            print("\nPress any key to continue....")
            input()
        elif choice==2:
            ip=input("Ente IPv4 Address: ")
            if check(ip)==True:
                print(getHost(ip))
                print("\nPress any key to continue....")
                input()
            else:
                print("\nIPv4 Address was not valid!! Try Again")
                print("\nPress any key to continue....")
                input()

        elif choice==3:
            ip=input("Ente IPv4 Address: ")
            if check(ip)==True:
                portScanner(ip)
                print("\nPress any key to continue....")
                input()
            else:
                print("\nIPv4 Address was not valid!! Try Again")
                print("\nPress any key to continue....")
                input()

        elif choice==4:
            ip=input("Ente IPv4 Address: ")
            if check(ip)==True:
                ipgeo(ip)
                print("\nPress any key to continue....")
                input()
            else:
                print("\nIPv4 Address was not valid!! Try Again")
                print("\nPress any key to continue....")
                input()

        elif choice==5:
            sys.exit()
        else:
            print("Invalid Choice please Enter a Valid choice\n")
            print("\nPress any key to continue....")
            input()

except KeyboardInterrupt:
    print("\nInturrpted by Keyboard")
    print("\nExiting Program!!!")
            