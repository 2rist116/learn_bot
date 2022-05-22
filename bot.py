import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def ephem_planet(update, context):
    planets = {'Mars': ephem.Mars('2022/05/18'), 
               'Jupiter': ephem.Jupiter('2022/05/18'),
               'Saturn': ephem.Saturn('2022/05/18'),
               'Mercury': ephem.Mercury('2022/05/18'),
               'Venus': ephem.Venus('2022/05/18'),
               'Uranus': ephem.Uranus('2022/05/18'),
               'Neptune': ephem.Neptune('2022/05/18')
               }

    planet_text = update.message.text
    planet_text2 = planet_text.split()
    planet_text3 = planet_text2[1]
    print(planet_text3)
    if planet_text3 in planets:
        const = ephem.constellation(planets[planet_text3])
        print(const)
        update.message.reply_text(const)


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Здравствуй, пользователь!')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context = True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler("planet", ephem_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info('Bot started')
    
    mybot.start_polling()
    mybot.idle()
if __name__=='__main__':
    main()