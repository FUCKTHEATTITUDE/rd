#!/usr/bin/python3.9+
# -*- coding: utf-8 -*-
# 📌️ M4nifest0 Black Hat Hacking Team™💪
# 📌️ 𝕿𝖍𝖎𝖘 𝕴𝖘 𝕿𝖍𝖊 𝓜4𝓷𝓲𝓯𝓮𝓼𝓽0 𝕿𝖊𝖆𝖒™
# 📌️ Author hack4lx 👊 
# 📌 💪 Site : https://m4nifest0.com 👊
# 📌 💪 Site : https://m4nifest0.group 👊
# 📌 💪 Site : https://m4nifest0.shop 👊
# 📌 💪 Channel Telegram : https://t.me/M4nifest0 👊
# 📌 2021-2022 💪
# 📌 Version 1.1.4 💪


from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    
    b = [    
    '                                                        ',   
    '██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗  ██╗██╗     ██╗  ██╗',
    '██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║  ██║██║     ╚██╗██╔╝',
    '███████║███████║██║     █████╔╝ ███████║██║      ╚███╔╝ ',
    '██╔══██║██╔══██║██║     ██╔═██╗ ╚════██║██║      ██╔██╗',
    '██║  ██║██║  ██║╚██████╗██║  ██╗     ██║███████╗██╔╝ ██╗ ',
    '╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝',
                
    ' ========================================================',
    ' 👽 M4nifest0 Black Hat Hacking Team™💪',
    ' 🌐 Site 1 :www.m4nifest0.group👊',
    ' 🌐 Site 2 :www.m4nifest0.shop 👊',
    ' 🌐 Site 3 :www.m4nifest0.com 👊',
    ' 💀 Telegram Channel  :https://t.me/M4nifest0 👊',
    ' ⚙️ version :1.2.4',
    ' 📝 Author  :hack4lx 👊',
    ' 📝 python_version:3.9.0',
    ' ========================================================', 
    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
        
    
    print(f'   📌  Please select one {n}\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(lg+'[1] ☎️ Add phone number'+n)
    print(lg+'[2] 👣 Check the forbidden account'+n)
    print(lg+'[3] ✂️ Delete accounts'+n)
    print(lg+'[4] ❌ Quit'+n)
    a = int(input('\n✍️Please select an item: '))
    if a == 1:
        new_accs = []
        with open('OTP.txt', 'ab') as g:
            number_to_add = int(input(f'\n{lg}  [📌] Please enter the number of accounts to add: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{lg}[📌] Please enter the relevant phone numbers: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{lg} [📌] Saved all accounts in OTP.txt')
            clr()
            print(f'\n{lg} [📌] Checking accounts, please wait ...\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 19286603 , '3f459e22ac139db64f0ddcd2c70ab1ba')
                c.start(number)
                print(f'{lg}[📌] Successfully entered')
                c.disconnect()
            input(f'\n 🔐 Return to previous menu (press Enter)')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('OTP.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[📌] There are no accounts! Please add some and retry')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}',19286603  , '3f459e22ac139db64f0ddcd2c70ab1ba')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Enter the code: '))
                        print(f'{lg}[+] {phone} ❌ is not banned{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' ⛔️ is banned!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'⭕️ There is no banned account.')
                input('\n🔐 Return to previous menu (press Enter)')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('OTP.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[📌] All banned accounts removed'+n)
                input('\n🔐 Return to previous menu (press Enter)')

    elif a == 3:
        accs = []
        f = open('OTP.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{lg}[📌] Choose an account to delete\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[📌] Enter a choice: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('OTP.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[📌] Account Deleted{n}')
        input(f'\n🔐 Return to previous menu (press Enter)')
        f.close()
    elif a == 4:
         
       
 
        clr()
        banner()
        exit()
