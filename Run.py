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
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, PhoneNumberBannedError, ChatAdminRequiredError
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError, UserBannedInChannelError, UserAlreadyParticipantError, FloodWaitError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
from telethon.tl.functions.messages import ImportChatInviteRequest, AddChatUserRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import UserStatusRecently
import time
import random
from colorama import init, Fore
import os
import pickle


init()


r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
grey = '\033[97m'
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '[' + w + 'i' + lg + ']' + rs
error = lg + '[' + r + '!' + lg + ']' + rs
success = w + '[' + lg + '*' + w + ']' + rs
INPUT = lg + '[' + cy + '~' + lg + ']' + rs
plus = w + '[' + lg + '+' + w + ']' + rs
minus = w + '[' + lg + '-' + w + ']' + rs

def banner():
     
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
        print(f'{random.choice(colors)}{char}{rs}')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

accounts = []
f = open('OTP.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

# TODO:  
print('\n' + info + lg + '🔍 Checking for banned accounts...' + rs)
for a in accounts:
    phn = a[0]
    print(f'{plus}{grey} Checking {lg}{phn}')
    clnt = TelegramClient(f'sessions/{phn}',  19286603, '3f459e22ac139db64f0ddcd2c70ab1ba')
    clnt.connect()
    banned = []
    if not clnt.is_user_authorized():
        try:
            clnt.send_code_request(phn)
            print('OK')
        except PhoneNumberBannedError:
            print(f'{error} {w}{phn} {r}⛔️ is banned!{rs}')
            banned.append(a)
    for z in banned:
        accounts.remove(z)
        print(info+lg+'❌ Banned account removed[Remove permanently using Config.py]'+rs)
    time.sleep(0.5)
    clnt.disconnect()


print(info+' Sessions created!')
clr()
banner()
 
def log_status(scraped, index):
    with open('status.dat', 'wb') as f:
        pickle.dump([scraped, int(index)], f)
        f.close()
    print(f'{info}{lg} Session stored in {w}status.dat{lg}')
    

def exit_window():
    input(f'\n{cy} 📍 Press enter to exit...')
    clr()
    banner()
    sys.exit()

 
try:
    
    with open('status.dat', 'rb') as f:
        status = pickle.load(f)
        f.close()
        lol = input(f'{INPUT}{cy} ✍️ Resume scraping members from {w}{status[0]}{lg}? [y/n]: {r}')
        if 'y' in lol:
            scraped_grp = status[0] ; index = int(status[1])
        else:
            if os.name == 'nt': 
                os.system('del status.dat')
            else: 
                os.system('rm status.dat')
            scraped_grp = input(f'{INPUT}{cy} ⚙️ Please enter public / private group links to scrape members: {r}')
            index = 0
except:
    scraped_grp = input(f'{INPUT}{cy} ⚙️ Please enter public / private group links to scrape members: {r}')
    index = 0
 
accounts = []
f = open('OTP.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

print(f'{info}{lg} ✂️ Total accounts: {w}{len(accounts)}')
number_of_accs = int(input(f'{INPUT}{cy} ✍️ Enter number of accounts to use: {r}'))
print(f'{info}{cy} 📍 Choose an option{lg}')
print(f'{cy}[0]{lg}📍 Add to public group')
print(f'{cy}[1]{lg}📍 Add to private group')
choice = int(input(f'{INPUT}{cy} 📍 Enter choice: {r}'))
if choice == 0:
    target = str(input(f'{INPUT}{cy} 📍 Enter public group link: {r}'))
else:
    target = str(input(f'{INPUT}{cy} 📍 Enter private group link: {r}'))
print(f'{grey}_'*50)
 
to_use = [x for x in accounts[:number_of_accs]]
for l in to_use: accounts.remove(l)
with open('OTP.txt', 'wb') as f:
    for a in accounts:
        pickle.dump(a, f)
    for ab in to_use:
        pickle.dump(ab, f)
    f.close()
sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request{w}[{lg}0 for None{w}]: {r}'))
 
print(f'{success}{lg} 📌 Adding members from {w}{len(to_use)}{lg} account(s) --')
adding_status = 0
approx_members_count = 0
for acc in to_use:
    stop = index + 60
    c = TelegramClient(f'sessions/{acc[0]}', 19286603 , '3f459e22ac139db64f0ddcd2c70ab1ba')
    print(f'{plus}{grey} User: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
    c.start(acc[0])
    acc_name = c.get_me().first_name
    try:
        if '/joinchat/' in scraped_grp:
            g_hash = scraped_grp.split('/joinchat/')[1]
            try:
                c(ImportChatInviteRequest(g_hash))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} 📌 Joined group to scrape')
            except UserAlreadyParticipantError:
                pass 
        else:
            c(JoinChannelRequest(scraped_grp))
            print(f'{plus}{grey} User: {cy}{acc_name}{lg} 📌 Joined group to scrape')
        scraped_grp_entity = c.get_entity(scraped_grp)
        if choice == 0:
            c(JoinChannelRequest(target))
            print(f'{plus}{grey} User: {cy}{acc_name}{lg} 📌 Joined group to add')
            target_entity = c.get_entity(target)
            target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
        else:
            try:
                grp_hash = target.split('/joinchat/')[1]
                c(ImportChatInviteRequest(grp_hash))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} 📌 Joined group to add')
            except UserAlreadyParticipantError:
                pass
            target_entity = c.get_entity(target)
            target_details = target_entity
    except Exception as e:
        print(f'{error}{r} User: {cy}{acc_name}{lg}📌 Failed to join group')
        print(f'{error} {r}{e}')
        continue
    print(f'{plus}{grey} User: {cy}{acc_name}{lg} 📌 {cy}Retrieving entities...')
   
    try:
        members = []
        members = c.get_participants(scraped_grp_entity, aggressive=True)
    except Exception as e:
        print(f'{error}{r} Couldn\'t scrape members')
        print(f'{error}{r} {e}')
        continue
    approx_members_count = len(members)
    assert approx_members_count != 0
    if index >= approx_members_count:
        print(f'{error}{lg} No members to add!')
        continue
    print(f'{info}{lg} Start: {w}{index}')
   
    peer_flood_status = 0
    for user in members[index:stop]:
        index += 1
        if peer_flood_status == 10:
            print(f'{error}{r} 📌 There are so many mistakes! Final session ...')
            break
        try:
            if choice == 0:
                c(InviteToChannelRequest(target_details, [user]))
            else:
                c(AddChatUserRequest(target_details.id, user, 42))
            user_id = user.first_name
            target_title = target_entity.title
            print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- {cy}{user_id} {lg}--> {cy}{target_title}')
           
            adding_status += 1
            print(f'{info}{grey} ❌ User: {cy}{acc_name}{lg} -- Sleep {w}{sleep_time} {lg}second(s)')
            time.sleep(sleep_time)
        except UserPrivacyRestrictedError:
            print(f'{minus}{grey} ❌ User: {cy}{acc_name}{lg} -- {r}📌 User Privacy Restricted Error')
            continue
        except PeerFloodError:
            print(f'{error}{grey} ❌ User: {cy}{acc_name}{lg} -- {r}📌 Peer Flood Error.')
            peer_flood_status += 1
            continue
        except ChatWriteForbiddenError:
            print(f'{error}{r} ❌ Can\'t add to group. Contact group admin to enable members adding')
            if index < approx_members_count:
                log_status(scraped_grp, index)
            exit_window()
        except UserBannedInChannelError:
            print(f'{error}{grey} User: {cy}{acc_name}{lg} -- {r}Banned from writing in groups')
            break
        except ChatAdminRequiredError:
            print(f'{error}{grey} User: {cy}{acc_name}{lg} -- {r}Chat Admin rights needed to add')
            break
        except UserAlreadyParticipantError:
            print(f'{minus}{grey} User: {cy}{acc_name}{lg} -- {r}User is already a participant')
            continue
        except FloodWaitError as e:
            print(f'{error}{r} {e}')
            break
        except ValueError:
            print(f'{error}{r} ❌ Error in Entity')
            continue
        except KeyboardInterrupt:
            print(f'{error}{r} ---- Adding Terminated ----')
            if index < len(members):
                log_status(scraped_grp, index)
            exit_window()
        except Exception as e:
            print(f'{error} {e}')
            continue
 
if adding_status != 0:
    print(f"\n{info}{lg} ❤️ Adding session ended")
try:
    if index < approx_members_count:
        log_status(scraped_grp, index)
        exit_window()
except:
    exit_window()
