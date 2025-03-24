#!/usr/bin/env python3

import json
import subprocess

hosts = ["192.168.0.77", "192.168.0.78"]

reachable_hosts = []
for ip in hosts:
    result = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        reachable_hosts.append(ip)
        
inventory = {
    "all": {
        "hosts": reachable_hosts,
        "vars": {
            "ansible_user": "test",
            "ansible_ssh_pass": "welcome1"
        }
    }
}

print(json.dumps(inventory))