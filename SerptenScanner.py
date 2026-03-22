import socket
import os
def ProgramText():
    print(r"""
 _____                 __                _____                                 
 / ___/___  _________  / /____  ____     / ___/_________ _____  ____  ___  _____
 \__ \/ _ \/ ___/ __ \/ __/ _ \/ __ \    \__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 ___/ /  __/ /  / /_/ / /_/  __/ / / /   ___/ / /__/ /_/ / / / / / / /  __/ /    
 /____/\___/_/  / .___/\__/\___/_/ /_/   /____/\___/\__,_/_/ /_/_/ /_/\___/_/     
             /_/                                                                 """)
def WarningText():
    print("""
⚠️ Disclaimer
This software is intended solely for educational purposes and security testing
on systems you own or have explicit permission to test.
Unauthorized use may be illegal. The developer is not responsible for misuse.
""")


ProgramText()
WarningText()

hostname=socket.gethostname()
hip=socket.gethostbyname(hostname)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    Target=input("Give Me Target ip: ")
    Process=int(input("""
    1-Advenced Scan
    2-Normal scan
    3-Basic scan
                  """))
    isWant=input("You want scan results save the from file(yes/no) : ")

    if(Process == 1):
        for port in range(1, 65536):
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(5.0)

            try:
                s.connect((Target,port))
                banner=s.recv(1024)
                print(f"[+] Port {port} open - Banner: {banner.decode(errors='ignore')}")
            except ConnectionRefusedError:
                pass
            except Exception as e:
                pass
            finally:
                s.close()
            if isWant.lower().lstrip() == "yes":
                with open("SerptenScan_results","w") as file:
                    file.write(f"[+] Port {port} open - Banner: {banner.decode(errors='ignore')}") 
        print("All port scanned")
    elif (Process == 2):
        for port in range(1, 1024):
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(5.0)

            try:
                s.connect((Target,port))
                banner=s.recv(1024)
                print(f"[+] Port {port} open - Banner: {banner.decode(errors='ignore')}")
            except ConnectionRefusedError:
                pass
            except Exception as e:
                pass
            finally:
                s.close()
            if isWant.lower().lstrip() == "yes":
                with open("SerptenScan_results","w") as file:
                    file.write(f"[+] Port {port} open - Banner: {banner.decode(errors='ignore')}") 
        print("All port scanned")
    elif (Process == 3):
        for port in range(1, 256):
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(5.0)

            try:
                s.connect((Target,port))
                banner=s.recv(1024)
                print(f"[+] Port {port} open - Banner: {banner.decode(errors='ignore')}")
            except ConnectionRefusedError:
                pass
            except Exception as e:
                pass
            finally:
                s.close()
            if isWant.lower().lstrip() == "yes":
                with open("SerptenScan_results","w") as file:
                    file.write(f"[+] Port {port} open - Banner: {banner.decode(errors='ignore')}")
        print("All port scanned")   
except ValueError :
    print("You Entered wrong type ")




