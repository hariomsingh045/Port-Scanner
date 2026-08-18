#!/usr/bin/env python3
import socket, argparse, time, threading
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

CYAN="\033[96m"; GREEN="\033[92m"; YELLOW="\033[93m"
RED="\033[91m"; WHITE="\033[97m"; RESET="\033[0m"
start=time.time()

GREEN = "\033[92m"

print(GREEN + r"""
__     __  ___   ____   _____  _____  __  __  ____    ____    _      _   _ 
\ \   / / / _ \ |  _ \ |_   _|| ____| \ \/ / / ___|  / ___|  / \    | \ | |
 \ \ / / | | | || |_) |  | |  |  _|    \  /  \___ \ | |     / _ \   |  \| |
  \ V /  | |_| ||  _ <   | |  | |___   /  \\   ___) || |___ / ___ \ | |\  |
   \_/    \___/ |_| \_\  |_|  |_____| /_/\_\|____/  \____|/_/   \_\_|_| \_|

*****************************************************************
*  NEXUSSCAN - Network Port Scanner                             *
*  Developed By - Hariom Singh                                  *
*  Email-id - hariomsingh28453@gmail.com                        *
*  GitHub Profile - github.com/hariomsingh045                   *
*  LinkedIn Profile - linkedin.com/in/hariomsingh045            *
*  Features - TCP Port Scanning, Service Detection,             *
*             Host Resolution & URL Target Support              *
*****************************************************************
""" + RESET)

p=argparse.ArgumentParser(description="NEXUSSCAN - Network Port Scanner")
p.add_argument("-t","--target",required=True,help="IP, domain or URL")
p.add_argument("-p","--ports",default="1-1000",help="Example: 80,443 or 1-1000")
p.add_argument("-v","--verbose",action="store_true")
a=p.parse_args()

target=a.target.strip()
port_from_url=None

if "://" in target:
    u=urlparse(target)
    target=u.hostname
    port_from_url=u.port
elif target.count(":")==1:
    h,x=target.rsplit(":",1)
    if x.isdigit():
        target,port_from_url=h,int(x)

try:
    ip=socket.gethostbyname(target)
except socket.gaierror:
    print(RED+"[-] Unable to resolve target."+RESET); exit()

try:
    ports=set()
    for x in a.ports.split(","):
        if "-" in x:
            s,e=map(int,x.split("-",1)); ports.update(range(s,e+1))
        else:
            ports.add(int(x))
    ports=sorted(x for x in ports if 1<=x<=65535)
except ValueError:
    print(RED+"[-] Invalid port input."+RESET); exit()

if port_from_url: ports=[port_from_url]

print(YELLOW+f"\n[*] Target: {target}"+RESET)
print(YELLOW+f"[*] Scanning {len(ports)} ports...\n"+RESET)
print(WHITE+"PORT     STATE      SERVICE"+RESET)
print("-"*45)

opened=[]; lock=threading.Lock()

def scan(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.settimeout(.2)
    try:
        if s.connect_ex((ip,port))==0:
            try: service=socket.getservbyport(port,"tcp").upper()
            except OSError: service="UNKNOWN"
            with lock:
                opened.append(port)
                print(GREEN+f"{port:<9}OPEN       {service}"+RESET)
    except OSError: pass
    finally: s.close()

with ThreadPoolExecutor(max_workers=200) as pool:
    list(pool.map(scan,ports))

print()
if opened:
    print(GREEN+f"[+] Open ports: {len(opened)}"+RESET)
else:
    print(RED+"[-] No open ports found."+RESET)

if a.verbose:
    print(CYAN+f"[*] Resolved IP: {ip}"+RESET)
    print(CYAN+f"[*] Ports scanned: {len(ports)}"+RESET)

print(YELLOW+f"[*] Time: {time.time()-start:.2f}s"+RESET)
