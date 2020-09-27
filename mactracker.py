from datetime import datetime
from getmac import getmac

def main():
    while True:
        target_mac = 'ff:ff:ff:ff:ff:ff'
        mac_addresses = []
        for i in range(21):
            #add whatever ip you like and use the range of i to iterate through all local ip's
            ip = '127.0.0.'
            ip = str(ip)+str(i)
            mac = getmac.get_mac_address(ip=ip)
            if mac != None:
                mac_addresses.append('[ip]: '+str(ip)+' [mac_addr]: '+str(mac))

        online = notify(target_mac, mac_addresses)
        if online == True:
            break
    print("All addresses on the network: ")
    for addr in mac_addresses:
        print(addr)

def notify(target_mac, mac_addresses):
    timestamp = datetime.now(tz=None)
    for mac in mac_addresses:
        if target_mac in mac:
            print(f"target [{target_mac}] was online: {timestamp}")
            return True

main()

