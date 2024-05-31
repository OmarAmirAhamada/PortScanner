import socket
import termcolor


def scan(targets , ports):
      print('\n' + ' Starting Scan For ' + str(target))
      for port in range(1,ports):
            scan_port(targets,port)

def scan_port(ipadress,port):
       try:
              
           sock= socket.socket()
           sock.connect((ipaddress,port))
           print('[+] Port Opened' + str(port))
           sock.close()

       except:

             print('[-] Port Closed' + str(port))
             # you can delet3 and replace the code here by -> pass , just to avoid outputting the closed ports


targets = int(input ('[*] Enter TargetS To Scan(split them by ,): ')  )
ports = input ('[*] Enter How Many Ports You Want To Scan:') 
if ',' in targets:
          print (termcolor.colored((' [*]Scanning Multiple targets'), 'green'))
          for ip_addr in targets.split(','):
                 scan(ip_addr.strip(' '),ports )
else:
       scan(targets,ports)
       
