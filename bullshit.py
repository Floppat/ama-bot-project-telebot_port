import pathlib

from functional import fetch_args


def cmd(message, bot) -> None:
    bot.send_message(message.chat.id,  '!hi              (1.0)\n'
                    '!his             (2.0)\n'
                    '!hist            (2.1)\n'
                    '!pet sad/tochi   \n'
                    '!cmd_bullshit')

def hi(message, bot) -> None:
    bot.send_message(message.chat.id, 'just wanted do cool bot... 27/04/24')
def his(message, bot) -> None:
    bot.send_message(message.chat.id, 'big improvement and firs try to add bd... 05/10/24')
def hist(message, bot) -> None:
    bot.send_message(message.chat.id, 'finally normal SQLite db... 09/03/25')
def histo(message, bot) -> None:
    bot.send_message(message.chat.id, 'first attempt to do telebot port... 19/04/25 \nsecond attempt to do telebot port... 05/06/25')

def pet(message, bot) -> None:
    valid_images = [image.name for image in pathlib.Path('img/pet/').iterdir()]
    images = fetch_args('/pet', message.text)

    for image in images: # type: ignore
        if f'{image}.gif' in valid_images:
            with open(f'img/pet/{image}.gif', 'rb') as photo:
                bot.send_photo(message.chat.id, photo)