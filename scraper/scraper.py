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


from telethon import TelegramClient, events, sync,utils
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import (PeerFloodError, UserNotMutualContactError ,
                                          UserPrivacyRestrictedError, UserChannelsTooMuchError,
                                          UserBotError, InputUserDeactivatedError)
from telethon.tl.functions.channels import InviteToChannelRequest
import time,os,random,csv,sys

r= "\u001b[31;1m"
a= "\u001b[32m"
y = "\u001b[33;1m"
b="\u001b[34;1m"
m="\u001b[35;1m"
c="\u001b[36;1m"
clear = lambda:os.system('clear')

print ("")
print ("██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗  ██╗██╗     ██╗  ██╗")
print ("██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║  ██║██║     ╚██╗██╔╝")
print ("███████║███████║██║     █████╔╝ ███████║██║      ╚███╔╝ ")
print ("██╔══██║██╔══██║██║     ██╔═██╗ ╚════██║██║      ██╔██╗ ")
print ("██║  ██║██║  ██║╚██████╗██║  ██╗     ██║███████╗██╔╝ ██╗")
print ("╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝")
print ("")

el=0
def Sleep(timE):
    try:
        time.sleep(timE)
    except KeyboardInterrupt:
        print(r+" KeyboardInterrupt , ........")



def ospath():
    o=int(input(b+"❤️How many accounts do you enter?"))
    for po in range(o):
        if os.path.isfile('⚙️ sessions-LOG.txt'):
            with open('⚙️ sessions-LOG.txt', 'r') as f:
                data = f.readlines()
            v=int(len(data)/2)
            z=v
        else:
            z=0
        api_id= input(b+' ⚙️ Enter API_ID_{}: '.format(z+1))
        api_hash= input(' ⚙️ Enter API_HASH_{}: '.format(z+1))
        with open('⚙️ sessions-LOG.txt', 'a') as f:
            f.write(api_id+'\n'+api_hash+'\n')
        client = TelegramClient("hack4lx{}".format(z), api_id, api_hash)
        client.start()
        Sleep(1)
        clear()
       
        client.disconnect()
if os.path.isfile('⚙️ sessions-LOG.txt'):
    xc=input(b+" ❤️ Do u want to continue the last session "+a+" (y/n) ? ")
    if xc=='y':
        cy=input(" 👽 want to add more accounts "+a+" (y/n) ? ")
        if cy=='y':
            ospath()
        else:
            pass
    else:
        cv=input(" ❌ Do u want to remove the last session "+a+" (y/n) ? ")
        if cv=='y':
            with open('⚙️ sessions-LOG.txt', 'r') as f:
                data = f.readlines()
            v=int((len(data))/2)
            con=input(r+" ⛔️ Are you sure to permanently delete all files related to last session "+a+" (y/n) ? ")
            if con in ['', 'n']:
                print(m+" ❌ Now exiting..."+'\n'+a+"🚫 No files were deleted ! ")
                sys.exit(1)
            elif con=='y':
                print(r+ " ⛔️ Now deleting files related to last session")
                Sleep(1)
                for d in range(v-1):
                    os.remove("hack4lx{}.session".format(d))
                os.remove('⚙️ sessions-LOG.txt')          
            ospath()
        else:
            sys.exit()
else:
    ospath()


x=0
inh=2
t=0
with open('⚙️ sessions-LOG.txt', 'r') as f:
    data = f.readlines()
v=int(len(data)/2)
for s in range(v):
    api_id = data[t]
    api_hash = data[t+1]
    print(a+ ' \n❤️ Trying... to connect to the Account {} \n'.format(x+1)+y+ ' \n api {}= '.format(x+1) +m+ api_id +'\n' +y+ ' api hash {} = '.format(x+1) +m+ api_hash)
    Sleep(1)
    client = TelegramClient("hack4lx{}".format(x), api_id, api_hash)
    client.start()
    name=utils.get_display_name(client.get_me())
    print(a+" \n\n  ❤ Successfully connected as {}❤\n\n".format(name))
    t+=2
    lines=[]
    chats = []
    last_date = None
    chunk_size = 200
    groups=[]
    result = client(GetDialogsRequest(
                 offset_date=last_date,
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=chunk_size,
                 hash = 0
             ))
    chats.extend(result.chats)
    for chat in chats:
        try:
            if chat.megagroup==True:
                groups.append(chat)
        except:
            continue
    print(b+' 🔎 Please select the desired group:')
    i=0
    for g in groups:
        print(m+str(i) +y+ ' - '+a + g.title)
        i+=1
    g_index = input(b+' ✂️ Enter a number (or press ENTER to skip): ')
    if g_index == '' :
        info()
        print(m+" 📌 Ok. skipping...")
        Sleep(1)
    else:
        
        target_group=groups[int(g_index)]
        print(y+' ✂️ Fetching members. please wait a moment ...')
        all_participants = []
        all_participants = client.get_participants(target_group, aggressive=True)
        print(y+' ❤️ Saving In file...')
        with open("M4nifest0.csv","w",encoding='UTF-8') as f:
            writer=csv.writer(f,delimiter=",",lineterminator="\n")
            for user in all_participants:
                if user.username:
                    username= user.username
                else:
                    username= ""
                if user.first_name:
                    first_name= user.first_name
                else:
                    first_name= ""
                if user.last_name:
                    last_name= user.last_name
                else:
                    last_name= ""
                name= (first_name + ' ' + last_name).strip()
                writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])
        print(a+' 📌 Members scraped successfully.')
        Sleep(1)
    
    print(b+'🔍 Choose a group to add members:')
    i=0
    for group in groups:
        print(m+str(i) +y+ ' - ' +a+ group.title)
        i+=1
    g_index = input(b+' 📌 Enter a Number: ')
    if g_index=='':
        print(m+" \n ❌ exiting...")
        sys.exit()  
    users = []  
    with open('M4nifest0.csv', encoding='UTF-8') as f:
        rows = csv.reader(f,delimiter=",",lineterminator="\n")
        for row in rows:
            lines.append(row)
            user = {}
            user['username'] = row[0]
            user['id'] = int(row[1])
            user['name'] = row[3]
            users.append(user)
    my_participants = client.get_participants(groups[int(g_index)])
    target_group=groups[int(g_index)]

    target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)
    my_participants_id = []
    for my_participant in my_participants:
        my_participants_id.append(my_participant.id)
    info()
    n,q=0,0
    for user in users:
        usR=str(user['id'])
        n += 1
        if n % 20 == 0:
            
            print (y+' ⚙️ waiting for 10 seconds to avoid flooding....')
            Sleep(10)  
        elif q>= 9:
            client.disconnect()
            if x<v:             
                x+=1
                inh+=1
                break
            else:
                print(b+" ❌ exiting...")
                Sleep(1)
                sys.exit()
        if user['id'] in my_participants_id:
            print(a+' 👽 User already present,skipping...')
            n-=1
            with open('M4nifest0.csv', 'r',encoding='UTF-8') as f:
                dat = csv.reader(f,delimiter=",",lineterminator="\n")
                for tad in dat:
                    if usR in tad:
                        lines.remove(tad)
                        break
            Sleep(1)       
            continue
        else:
            try:
                print (a+' Adding {}'.format(user['name']))
                if True :
                    if user['username'] == "":
                        continue
                user_to_add = client.get_input_entity(user['username'])
                client(InviteToChannelRequest(target_group_entity,[user_to_add]))
                print(m+" 📍 Waiting for 1-2 Seconds...")
                with open('M4nifest0.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            break
                with open("M4nifest0.csv","w",encoding='UTF-8') as f:
                    writer=csv.writer(f,delimiter=",",lineterminator="\n")
                    for line in lines:
                        writer.writerow(line)        
                             
                time.sleep(random.randrange(2,4))
                
                q=0
            except PeerFloodError:
                print(r+' ❌ Getting Flood Error from telegram. Script is stopping now. Please try again after some time.')
                Sleep(1)
                q+= 1
            except UserPrivacyRestrictedError:
                print(r+' ❌ The user\'s privacy settings do not allow you to do this. Skipping.')
                with open('M4nifest0.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            break
                Sleep(1)
            except UserBotError:
                print(r+' ❌ Can\'t add Bot. Skipping...')
                with open('M4nifest0.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            break    
            except InputUserDeactivatedError:
                print(r+' ❌ The specified user was deleted. Skipping...')
                with open('M4nifest0.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            break
                Sleep(1)
            except UserChannelsTooMuchError:
                print(r+' ⚙️ User in too much channel. Skipping.')
                with open('M4nifest0.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            break
                Sleep(1)
            except UserNotMutualContactError:
                print(r+' Mutual No. Skipped.')
                with open('M4nifest0.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            break
                Sleep(1)
            except KeyboardInterrupt:
                i=0
                kst=["stop","❤️ continue","switch to next account"]
                for ks in kst:
                    print('\n'+m+ str(i) +y+ ' - ' +a+ ks)
                    i+=1
                keyb=int(input(y+" ⚙️ Enter a number : "))
                if keyb==1:
                    print(a+" ❤️ Ok continuing...")
                    Sleep(1)
                elif keyb==0:
                    print(y+" ❌ exiting...")
                    sys.exit(1)
                else:
                    print(a+ " \n\n⛔️ Switching... to next account\n\n")
                    x+=1
                    break                
            except Exception as e:
                print(r+' 🚫 Error:', e)
                print('📌 Trying to continue...')
                q += 1
                Sleep(1)
                continue