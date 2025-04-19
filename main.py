from telebot import TeleBot

from config import token
import functional as fn
from users import registred
import mini_game



bot = TeleBot(token)



@bot.message_handler(commands=['start'])
def cmd(message) -> None:
    registred(message=message)
    bot.send_message(message.chat.id,'kinda hello bro')
    fn.plus_xp(message=message)


# @bot.message_handler(commands=['cmd'])
# def cmd(message) -> None:
#     registred(message=message)
#     bot.send_message(message.chat.id,  embed=bcmd)
#     fn.plus_xp(message=message)

# @bot.message_handler(commands=['change_nick'])
# def change_nick(message, new_nick: str)-> None:
#     registred(message=message)
#     bot.send_message(message.chat.id, fn.db.change('users',message.from_user.id,'nickname',new_nick))
#     fn.plus_xp(message=message)

# @bot.message_handler(commands=['change_pet_name'])
# def change_nick(message, new_name: str)-> None:
#     registred(message=message)
#     bot.send_message(message.chat.id, fn.db.change('pets',fn.db.read('users',message.from_user.id,'pet_id')[0],'pet_name',new_name))
#     fn.plus_xp(message=message)

# @bot.message_handler(commands=['change_status'])
# def change_status(message, status_id: int, user_tag: str)-> None:
#     registred(message=message)
#     bot.send_message(message.chat.id, fn.change_status(message=message,status_id=status_id,user_tag=user_tag))

# @bot.message_handler(commands=['delete_user'])
# def change_nick(message, user_tag: str)-> None:
#     registred(message=message)
#     bot.send_message(message.chat.id, fn.delete_user(message=message, user_tag=user_tag))

# @bot.message_handler(commands=['leaderboard'])
# def leaderboard(message, entity: str, page: int, parameter: str) -> None:
#     registred(message=message)
#     page = fn.db.leaderboard(entity,page,parameter)
#     bot.send_message(message.chat.id, embed=lb_embed(page,entity,parameter))
#     fn.plus_xp(message=message)


@bot.message_handler(commands=['cmd_game'])
def cmd_game(message) -> None:
    mini_game.cmd(message=message, bot=bot)

@bot.message_handler(commands=['prehistory'])
def prehistory(message) -> None:
    mini_game.prehistory(message=message, bot=bot)
    fn.plus_xp(message=message)

@bot.message_handler(commands=['guide'])
def guide(message) -> None:
    mini_game.guide(message=message, bot=bot)
    fn.plus_xp(message=message)

# @bot.message_handler(commands=['user'])
# def user(message, user_tag: str) -> None:
#     mini_game.user(message=message, bot=bot, user_tag=user_tag)
#     fn.plus_xp(message=message)

@bot.message_handler(commands=['stats'])
def stats(message) -> None:
    mini_game.stats(message=message,bot=bot)
    fn.plus_xp(message=message)

@bot.message_handler(commands=['train'])
def train(message) -> None:
    mini_game.train(message=message, bot=bot)
    fn.plus_xp(message=message)

@bot.message_handler(commands=['feed'])
def feed(message) -> None:
    mini_game.feed(message=message, bot=bot)
    fn.plus_xp(message=message)

@bot.message_handler(commands=['attack'])
def attack(message) -> None:
    mini_game.attack(message=message, bot=bot)
    fn.plus_xp(message=message)

@bot.message_handler(commands=['sleep'])
def sleep(message) -> None:
    mini_game.sleep(message=message, bot=bot)
    fn.plus_xp(message=message)

# @bot.message_handler(commands=['shop'])
# def shop(message, item: str) -> None:
#     mini_game.shop(message=message, bot=bot, item=item)
#     fn.plus_xp(message=message)


bot.infinity_polling()
