from telebot import TeleBot


from config import token
import functional as fn
from users import registred
# from embeds import bcmd,lb_embed
import mini_game
import bullshit
import global_warming 


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

@bot.message_handler(commands=['change_nick'])
def task_change_nick(message):
    bot.send_message(message.chat.id, "Введите новый никнейм:")
    bot.register_next_step_handler(message, change_nick)

def change_nick(message):
    new_nick = message.text
    registred(message=message)
    bot.send_message(message.chat.id, fn.db.change('users',message.from_user.id,'nickname',new_nick))
    fn.plus_xp(message=message)

@bot.message_handler(commands=['change_pet_name'])
def task_change_pet_name(message):
    bot.send_message(message.chat.id, "Введите новую кличку питомца:")
    bot.register_next_step_handler(message, change_pet_name)

def change_pet_name(message)-> None:
    new_name = message.text
    registred(message=message)
    bot.send_message(message.chat.id, fn.db.change('pets',fn.db.read('users',message.from_user.id,'pet_id')[0],'pet_name',new_name))
    fn.plus_xp(message=message)

# @bot.message_handler(commands=['leaderboard'])
# def leaderboard(message, entity: str, page: int, parameter: str) -> None:
#     registred(message=message)
#     page = fn.db.leaderboard(entity,page,parameter)
#     bot.send_message(message.chat.id, embed=lb_embed(page,entity,parameter))
#     fn.plus_xp(message=message)


@bot.message_handler(commands=['change_status'])
def task_change_status(message):
    bot.send_message(message.chat.id, "Введите имя пользователя (@ упоминание):")
    bot.register_next_step_handler(message, task_change_status_get_status)

def task_change_status_get_status(message):
    user_tag = message.text
    bot.send_message(message.chat.id, "Введите новый статус пользователя:")
    bot.register_next_step_handler(message, change_status, user_tag=user_tag)

def change_status(message, user_tag: str)-> None:
    status_id = message.text
    registred(message=message)
    bot.send_message(message.chat.id, fn.change_status(message=message,status_id=status_id,user_tag=user_tag))

@bot.message_handler(commands=['delete_user'])
def task_delete_user(message):
    bot.send_message(message.chat.id, "Введите имя пользователя (@ упоминание):")
    bot.register_next_step_handler(message, delete_user)

def delete_user(message)-> None:
    user_tag = message.text
    registred(message=message)
    bot.send_message(message.chat.id, fn.delete_user(message=message, user_tag=user_tag))


@bot.message_handler(commands=['cmd_game'])
def cmd_game(message) -> None:
    bot.send_message(message.chat.id, mini_game.cmd())

@bot.message_handler(commands=['prehistory'])
def prehistory(message) -> None:
    bot.send_message(message.chat.id, mini_game.prehistory(message=message))
    fn.plus_xp(message=message)

@bot.message_handler(commands=['guide'])
def guide(message) -> None:
    bot.send_message(message.chat.id, mini_game.guide(message=message))
    fn.plus_xp(message=message)

@bot.message_handler(commands=['user'])
def task_user(message):
    bot.send_message(message.chat.id, 'Введите имя пользователя (@ упоминание) или "me" для себя:')
    bot.register_next_step_handler(message, user)

def user(message) -> None:
    user_tag = message.text
    mini_game.user(message=message, bot=bot, user_tag=user_tag)
    fn.plus_xp(message=message)

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

@bot.message_handler(commands=['shop'])
def task_shop(message):
    bot.send_message(message.chat.id, 'Введите номер предмета который хотите купить: \nДля справки введите "?".')
    bot.register_next_step_handler(message, shop)

def shop(message) -> None:
    item = message.text
    mini_game.shop(message=message, bot=bot, item=item)
    fn.plus_xp(message=message)


@bot.message_handler(commands=['cmd_bullshit'])
def cmd_bullshit(message) -> None:
    bullshit.cmd(message=message, bot=bot)

@bot.message_handler(commands=['hi'])
def hi(message) -> None:
    bullshit.hi(message=message, bot=bot)

@bot.message_handler(commands=['his'])
def his(message) -> None:
    bullshit.his(message=message, bot=bot)

@bot.message_handler(commands=['hist'])
def hist(message) -> None:
    bullshit.hist(message=message, bot=bot)

@bot.message_handler(commands=['histo'])
def histo(message) -> None:
    bullshit.histo(message=message, bot=bot)

@bot.message_handler(commands=['pet'])
def pet(message) -> None:
    bullshit.pet(message=message, bot=bot)


@bot.message_handler(commands=['cmd_warming'])
def cmd_warming(message) -> None:
    global_warming.cmd(message=message, bot=bot)

@bot.message_handler(commands=['about'])
def about(message) -> None:
    global_warming.about(message=message, bot=bot)

@bot.message_handler(commands=['reasons'])
def reasons(message) -> None:
    global_warming.reasons(message=message, bot=bot)

@bot.message_handler(commands=['how_help'])
def how_help(message) -> None:
    global_warming.how_help(message=message, bot=bot)

# @bot.message_handler(commands=['quiz'])
# def quiz(message) -> None:
#     global_warming.quiz(message=message, bot=bot)
#     fn.plus_xp(message=message)


bot.infinity_polling()
