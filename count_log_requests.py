#!/usr/bin/env python3

from argparse import ArgumentParser
from collections import Counter

"""
3. Create a script that reads the access log from a file. The name of the file is 
provided as an argument. An output of the script should provide the total number 
of different User Agents and then provide statistics with the number of requests 
from each of them.
"""

parser = ArgumentParser(description='Read access log and count requests from different User Agents')
parser.add_argument('filename', help='The name of the access log file')
args = parser.parse_args()

hosts = Counter()

with open(args.filename, "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        fields = line.split()
        if fields:
            host = fields[0]
            hosts[host] += 1

print(f"Total number of hosts: {len(hosts)}\n")
print(f"HOST: REQUESTS")
for host, requests in hosts.most_common():
    print(f"{host}: {requests}")