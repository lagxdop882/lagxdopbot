import requests
import telebot,time
from telebot import types
from gatet import Tele
import os
dollar=50
GROUP_ID = ['#']
token = '625524568a3M'
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber =1084525687
@bot.message_handler(commands=["start"])
def start(message):
	found='unpr'
	chat_id = message.chat.id
	with open("premium.txt", "r") as file:
		for line in file:
			if str(chat_id) in line.strip():
				found='pro'
	if not 'pro' in found:
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @MNOW4")
		return
	bot.reply_to(message,"Send the file now \n ارسل الملف الان")
@bot.message_handler(content_types=["document"])
def main(message):
	found='unpr'
	chat_id = message.chat.id
	with open("premium.txt", "r") as file:
		for line in file:
			if str(chat_id) in line.strip():
				found='pro'
	if not 'pro' in found:
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @MNOW4")
		return
	current_dir = os.getcwd()
	for filename in os.listdir(current_dir):
		if filename.endswith(".start"):
			bot.reply_to(message, "هناك شخص اخر يستخدم البوت")
			return
	dd = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			if total > 100000:
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='الحد الاقصي للفحص 100 بطاقه لكل ملف ')
				return
			with open("start.start", "w") as yu:
				pass
			for cc in lino:
				time.sleep(15)
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @MNOW4')
						os.remove('start.start')
						os.remove('stop.stop')
						return
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
