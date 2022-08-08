from time import sleep
from pyfiglet import figlet_format

from dinosay import dinoprint, DINO_TYPE

r = figlet_format("Yes", font= "slant")
s = figlet_format("no", font= "digital")
k = dinoprint('Welcome! \nThis program \nwill show you top 5 high-performance \nDNS public resolvers \nand their IPv4 DNS addresses', DINO_TYPE['tyrannosaurus'])
h= figlet_format("Bye..", font= "digital")

dns = []

with open("dns.csv") as f:
    for line in f:
        name, address = line.strip().split(":")
        dns.append(f"{name}'s dns address is {address.lstrip()}")


inp = input("Do you want me to sort them out? Y/n ")

if inp == "Y":
    print(r)
    for line in sorted(dns):
        print(line)
        sleep(1)
    sleep(1)
    dinoprint('Bye.. I need to sleep', DINO_TYPE["maiasaur"])
else:
    print(f"\n{s}")
    for line in dns:
        print(line)
        sleep(1)
    print(h)
        
    
    
    


