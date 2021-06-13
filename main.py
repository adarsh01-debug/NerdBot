import os
import telebot
from PyDictionary import PyDictionary
import random

BOT_KEY = os.environ['BOT_KEY']
bot = telebot.TeleBot(BOT_KEY)

API_KEY = os.environ['API_KEY']

dictionary=PyDictionary()

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.reply_to(message, "Howdy, nerd! How are you doing? Type the command: '/help' to know more about how to operate me.")

@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, "Here are the list of commands I recognize: \n\n1. /getMeaning <word> : returns a meaning of the typed word. \n\n2. /getSyn <word> : returns a synonym of the typed word. \n\n3. /getAnt <word> : returns an antonym of the typed word. \n\n4. /die : Bot says its final words.\n\n5. /credits : Tells you about the creator of this bot. \n\nNOTE: The entered word might have more than one meaning, synonym or antonym. In such case the bot will return only one of each. If you wish to seek a different reply from the current one then simply repeat the same command and word, if any other data exits then it will be displayed.")

@bot.message_handler(commands=['getMeaning'], content_types=['text'])
def get_meaning(message):
	message_word = message.text.split()
	message_meaning = dictionary.meaning(message_word[-1])

	message_list = list(message_meaning.values())

	meaning_len = len(message_list)

	rand_meaning = random.randint(0, meaning_len - 1)

	bot.reply_to(message, f"Meaning : {message_list[0][rand_meaning]}")

@bot.message_handler(commands=['getSyn'], content_types=['text'])
def get_synonym(message):
	message_word = message.text.split()
	message_synonym = dictionary.synonym(message_word[-1])

	synonym_len = len(message_synonym)
	rand_synonym = random.randint(0, synonym_len - 1)

	bot.reply_to(message, f"Synonym: {message_synonym[rand_synonym]}")

@bot.message_handler(commands=['getAnt'], content_types=['text'])
def get_antonym(message):
	message_word = message.text.split()
	message_antonym = dictionary.antonym(message_word[-1])

	antonym_len = len(message_antonym)
	rand_antonym = random.randint(0, antonym_len - 1)

	bot.reply_to(message, f"Antonym: {message_antonym[rand_antonym]}")

@bot.message_handler(commands=['die'])
def die(message):
	die_texts = ['I have a family, kill them instead.', 'Hey fellas! How about this for a headline for tomorrow’s paper? ‘French fries.', 'Thank god. I’m tired of being the funniest one in the room.', 'I knew I should have never replied to you.', 'No.', 'Don’t let it end like this. Tell them I said something funny.', 'Oh Lord, forgive the misprints!', 'Your favorite singer is overrated.', 'Did you mean: exit(0) ?', 'Et tu, Brute!', "But aren't you the one depressed?"]

	die_len = len(die_texts)

	rand_die = random.randint(0, die_len - 1)

	bot.send_message(message.chat.id, f"{die_texts[rand_die]}")

@bot.message_handler(commands=['credits'])
def credits(message):
	bot.reply_to(message, "Copyright: Adarsh Pandey")

@bot.message_handler(content_types='text')
def helper(message):
	help(message)

bot.polling()
