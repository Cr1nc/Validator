import requests
import time
from colorama import Fore
from requests.exceptions import Timeout
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

Print("Usage: This script expects a Sublist3r domains.txt output file in the same directory as the script")

cleanTargets = []
# o = open("Targets.txt", "a")
for line in open("domains.txt"):
    line = line.replace('\n', '')
    lines = line.split("<BR>")
    for l in lines:
      newLine = "http://" + l + '\n'
      newLine2 = "https://" + l + '\n'
      cleanTargets.append(newLine)
      cleanTargets.append(newLine2)
o = open("Targets.txt", "a")
o.writelines(cleanTargets)
o.close()

print(Fore.GREEN + "\n[*] File cleaned up.")
time.sleep(0.5)
print(Fore.GREEN + "\n[*] Processing target file data:\n")
time.sleep(0.2)
#print('')
for line in open('Targets.txt', 'r'):
    lines = line.split()
    try:
        for l in lines:
            response = requests.get(l, timeout=1, verify=False) #uses a get request due to head results differing.
    except (Timeout, requests.exceptions.ConnectionError):
            print(Fore.LIGHTBLUE_EX + "[+]", response, l)

#            nl = open("List.txt" 'w')
#            ls = l.writelines
    else:
#           print(Fore.RED + '[-] No Response', l) #remove comment if you want to see failed requests
        pass

def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    exit(0)
