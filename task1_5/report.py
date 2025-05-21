#!/usr/bin/env python3

"""
5. Write a script that gets system information like distro info, 
memory(total, used, free), CPU info (model, core numbers, speed), 
current user, system load average, and IP address. Use arguments 
for specifying resources. 

(For example, -d for distro -m for memory, -c for CPU, -u for user info, 
-l for load average, -i for IP address).
"""

import argparse
import platform
import getpass
import cpuinfo
import socket
import distro
import psutil
import os

parser = argparse.ArgumentParser(description='Get system information')
parser.add_argument('-d', '--distro', action='store_true', help='Get distro information')
parser.add_argument('-m', '--memory', action='store_true', help='Get memory information')
parser.add_argument('-c', '--cpu', action='store_true', help='Get CPU information')
parser.add_argument('-u', '--user', action='store_true', help='Get user information')
parser.add_argument('-l', '--load', action='store_true', help='Get system load average')
parser.add_argument('-i', '--ip', action='store_true', help='Get IP address')
args = parser.parse_args()

if platform.system().lower() != "linux":
    print("Error: This script can only be run on Linux systems :(")
    exit(1)

if not any(vars(args).values()):
    parser.print_help()
    exit(0)

if args.distro:
    distro_name = distro.name(pretty=True)
    print(f"Distro: {distro_name}")
    
if args.memory:
    mem = psutil.virtual_memory()
    print(f"Memory Total: {mem.total // 1024 // 1024} MB")
    print(f"Memory Used: {mem.used // 1024 // 1024} MB")
    print(f"Memory Free: {mem.available // 1024 // 1024} MB")

if args.cpu:
    cpu_info = cpuinfo.get_cpu_info()
    cpu_model = cpu_info.get('brand_raw', 'Unknown')
    print(f"CPU Model: {cpu_model}")

    core_count = psutil.cpu_count(logical=False)
    logical_count = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()
    print(f"CPU Cores (Physical): {core_count}")
    print(f"CPU Cores (Logical): {logical_count}")
    print(f"CPU Speed: {cpu_freq.current:.2f} MHz")

if args.user:
    user_info = getpass.getuser()
    print(f"Current User: {user_info}")

if args.load:
    load_avg = os.getloadavg()
    print(f"System Load Average: {load_avg}")

if args.ip:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"IP Address: {ip_address}")
