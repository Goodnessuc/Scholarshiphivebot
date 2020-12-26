import telebot
from telebot import TeleBot
from telebot import types
from scarper import *

bot = TeleBot(token="1465907655:AAHbCRtgyykGpkuHhq3aAfcOODdgWJ1nHLk")


markup = types.ReplyKeyboardMarkup(row_width=3)
undergraduate_button = types.KeyboardButton('/undergraduate')
phd_button = types.KeyboardButton('/phd')
masters_button = types.KeyboardButton('/masters')
job_button = types.KeyboardButton("/jobs")
secondary_button = types.KeyboardButton("/secondary")
competitions_button = types.KeyboardButton("/competitions")
internships_button = types.KeyboardButton("/internships")
training_button = types.KeyboardButton("/training")
help_button = types.KeyboardButton("/help")
markup.add(training_button,internships_button,competitions_button,secondary_button,job_button,masters_button,phd_button,undergraduate_button,help_button)

#send_message and then command


@bot.message_handler(commands=['start'])
def start_bot(message):
    users_name = message.from_user.username
    bot.reply_to(message,
                 f"Hi {users_name}, i am your scholarship updates bot 🐱‍🏍😎 for the taking. I help you get informed about ongoing scholarships and ooportunities around you depending on your level of study 🔍📚, jobs 🔍🏛, internships 👩‍🎤 and so much more🌟.\n\n Use /help to learn more about how i work 🤖")
    bot.send_message(message.chat.id, f"What do you want to do today 😁", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_bot(message):
    users_name = message.from_user.username

    bot.reply_to(message,
                 f"Hey, {users_name} what do you need help with.\nHere is a list of commands you can give me to get started")
    bot.reply_to(message,
                 f"/start - start me up\n/help - to get this menu 🤔\n/secondary - high school opportunities updates 🌱 \n/undergraduate - get undergraduate scholarship opportunities\n/competitions - take on the finest in a bid to become a champion 🎖\n/internships - grab cool internship opportunities\n/masters - get funded opportunities to bag a masters degree 🐱‍👤\n/jobs - for job opportunities to aid you secure the bag 🤑\n/trainings - training opportunities are open, make a breakthrough 🚀\n/phd - schools have tabs on you. pick a call, get a doctorate degree today 😉")
    bot.send_message(message.chat.id, f"What do you want to do today 😁", reply_markup=markup)

@bot.message_handler(commands=['undergraduate'])
def undergraduate_updates(message):
    scraper_instance = get_scholarship_updates("https://www.intelregion.com/category/scholarships/undergraduate-scholarships/")
    undergradata = prepare_updates_data(scraper_instance, 5)
    for i in undergradata:
        bot.send_message(message.chat.id, i)
    bot.reply_to(message, "Check out these if you've got the requirements and would love to apply, Goodluck 😉")


@bot.message_handler(commands=['internships'])
def internship_updates(message):
    bot.reply_to(message, f"loading..")
    scraper_instance = get_scholarship_updates("https://www.intelregion.com/category/scholarships/internships/")
    internship_data = prepare_updates_data(scraper_instance, 5)
    for i in internship_data:
        bot.send_message(message.chat.id, i)
    bot.reply_to(message, "Check out these if you've got the requirements and would love to apply, Goodluck 😉")


@bot.message_handler(commands=['masters'])
def masters_updates(message):
    bot.reply_to(message, f"loading...")
    scraper_instance2 = get_scholarship_updates("https://www.intelregion.com/category/scholarships/masters-scholarships/")
    masters = prepare_updates_data(scraper_instance2, 5)
    for i in masters:
        bot.send_message(message.chat.id, i)
    bot.reply_to(message, "Check out these if you've got the requirements and would love to apply, Goodluck 😉")


@bot.message_handler(commands=['phd'])
def phd_updates(message):
    bot.reply_to(message, f"loading...")
    scraper_instance = get_scholarship_updates("https://www.intelregion.com/category/scholarships/phd-scholarships/")
    phd_data = prepare_updates_data(scraper_instance, 5)
    for i in phd_data:
        bot.send_message(message.chat.id, i)
    bot.reply_to(message, "Check out these if you've got the requirements and would love to apply, Goodluck 😉")


@bot.message_handler(commands=['jobs'])
def job_updates(message):
    bot.reply_to(message, f"loading...")
    scraper_instance = get_job_updates("https://www.intelregion.com/jobs/")
    job_data = prepare_updates_data(scraper_instance, 5)
    for i in job_data:
        bot.send_message(message.chat.id, i)
    bot.reply_to(message, "Check out these if you've got the requirements and would love to apply, Goodluck 😉")


@bot.message_handler(commands=['trainings'])
def training_updates(message):
    bot.reply_to(message, f"loading...")
    scraper_instance = get_scholarship_updates("https://www.intelregion.com/category/scholarships/training/")
    training_data = prepare_updates_data(scraper_instance, 5)
    for i in training_data:
        bot.send_message(message.chat.id, i)
    bot.reply_to(message, "Check out these if you've got the requirements and would love to apply, Goodluck 😉")


@bot.message_handler(commands=['competitions'])
def competition_updates(message):
    bot.reply_to(message, f"loading...")
    scraper_instance = get_scholarship_updates("https://www.intelregion.com/category/scholarships/competitions/")
    competition_data = prepare_updates_data(scraper_instance, 5)
    for i in competition_data:
        bot.send_message(message.chat.id, i)
    bot.reply_to(message, "Check out these if you've got the requirements and would love to apply, Goodluck 😉")


@bot.message_handler(commands=['secondary'])
def secondary_updates(message):
    bot.reply_to(message, f"loading...")
    scraper_instance = get_scholarship_updates("https://www.intelregion.com/category/scholarships/secondary-school-scholarships/")
    secondary_school = prepare_updates_data(scraper_instance, 5)
    for i in secondary_school:
        bot.send_message(message.chat.id, i)
    bot.reply_to(message, "Check out these if you've got the requirements and would love to apply, Goodluck 😉")




if __name__ == '__main__':
    bot.polling()
