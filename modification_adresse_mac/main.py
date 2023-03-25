#!/usr/bin/python3

import subprocess


def set_adresse_mac(interface, new_adresse_mac):
    subprocess.call("sudo ifconfig "+interface+" up",shell=True)
    subprocess.call("sudo ifconfig " + interface + " lladdr " + new_adresse_mac,shell = True)
    #subprocess.call("sudo ifconfig " +interface+ " up",shell=True)

interface = input("quel interface")
new_adresse_mac = input("quel nouvelle adresse ?")

set_adresse_mac(interface,new_adresse_mac)



#3c:a6:f6:20:66:22 