#Just install

#pip install wakeonlan 

#then run a code like:

from wakeonlan import send_magic_packet

send_magic_packet('00.00.00.00.00.00')

#where 00.00.00.00.00.00 is the macaddress of the device you want to wake
#remember that WOL must be enabled in the target machine
#the network must be the same for the target and the sender device
#if you are in another subnet you may need to connect the 2 subnets 

#also when you name your py file remember to not name it with the package name!
#i.e. wakeonlan.py cannot be the name of your file (circular import error!)
