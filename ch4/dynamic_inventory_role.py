#!/usr/bin/env python3

import json

servers = {
    "192.168.0.77": "web"
}

inventory = {"_meta": {"hostvars": {}}}
for ip, role in servers.items():
    if role not in inventory:
        inventory[role] = {"hosts": []}
    inventory[role]["hosts"].append(ip)
    inventory["_meta"]["hostvars"][ip]= {
        "ansible_user": "test",
        "ansible_ssh_pass": "welcome1"
    }
print(json.dumps(inventory))