import os, sys

print ("")
print ("██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗  ██╗██╗     ██╗  ██╗")
print ("██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║  ██║██║     ╚██╗██╔╝")
print ("███████║███████║██║     █████╔╝ ███████║██║      ╚███╔╝ ")
print ("██╔══██║██╔══██║██║     ██╔═██╗ ╚════██║██║      ██╔██╗ ")
print ("██║  ██║██║  ██║╚██████╗██║  ██╗     ██║███████╗██╔╝ ██╗")
print ("╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝")
print ("")

print('Pakages Installing Started')
os.system('pip install telethon==1.16.4')
os.system('pip install colorama==0.4.3')
os.system('pip install requests==2.25.1')
os.system("cls" if os.name=='nt' else 'clear')
print ('All Pakages Installed Successfully')