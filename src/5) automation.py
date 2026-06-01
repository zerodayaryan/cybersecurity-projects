#This is the python script that automates the reconnaissance phase of bug bounty. It automates the 
# subfinder, puredns tools

import subprocess

domain = str(input("Enter domain name: "))

subfinder = subprocess.run(
    ["subfinder", "-d", domain, "-o", "subdomain.txt"],
     capture_output=True, text=True)

puredns = subprocess.run(
    ["puredns","resolve","subdomain.txt","-w","final.txt"],
    capture_output=True, text=True
)
print("reconnaissance process in progess...")