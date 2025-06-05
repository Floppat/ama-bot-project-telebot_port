from users import registred, get_other_user


def cmd() -> str:
     return ('/change_nick       (изменяет ник который будет отображатся лидербордах)\n'
            '/change_pet_name   (изменяет имя питомца)\n'
            '/leaderboard       (entity= users/pets ; page= номер страницы ; \n'
            'для users: tag/username/coins/quiz_record/xp , для pets: pet_name/str/xp\n'
            '/prehistory        (предистория, немного сюжета)\n'
            '/guide             (ввод в игру)\n'
            '/me                (данные о вас как о пользователе амы)\n'
            '/stats             (хар-ки вашего питомца)\n'
            '/train             (+сила; -здоровье; -выносливость)\n'
            '/feed              (+здоровье; +выносливость)\n'
            '/sleep             (полное восстановление выносливости)\n'
            '/attack            (-здоровье (ведь это же битва))\n'
            '/shop              (покупка артефактов)\n'
            '!cmd_game')

def prehistory(message) -> str:
    registred(message=message)
    return  ('Давным-давно люди жили в мире с природой и животными...\n'
            'но не так давно, всего каких два века назад, люди забыли свою историю и начали загрязнять природу всё сильнее...\n'
            'Это породило маленьких монстров - Карков\n'
            'Карки хотят уничтожить всю жизнь на земле, и нагревают её, и не остановятся пока земля не превратится в большую печку!\n'
            'Спасите планету - победите всех Карков. Но... проблема в том что люди не видят Карков... Как же быть? Природа поможет! \n' 
            'Ваш питомец - возможно единственный в своём роде, может остановить Карков! Тренируёте его и спасите землю от Карков!\n')


def guide(message) -> str:
    registred(message=message)
    return  ('Каждый день (до использования команды /sleep) вы можете 2 раза потренироватся, затем 1 раз поесть.\n'
            'За день можно 2 раза потренироватся, или 1 раз потренироватся и 1 раз подратся.\n'
            'Совет: лучше перед боем не тренероватся, ведь будет меньше здоровья, а поесть вы не сможете.\n'
            'Тактика про: каждый день 2 раза тренироваться и 1 раз есть, после того как набралось 10 атаки на следущий день идти в бой.\n' 
            'Также противник становится сильнее не по дням, а по боям, так что покупайте артефакты, ведь они повышают защиту.\n'
            'Важно: руководство для новичков и после покупки первого артефакта численные данные становятся неактуальны.\n')


def user(message, bot, user_tag: str):
    user = registred(message=message)
    if user_tag == 'me':
        bot.send_message(message.chat.id, f'{user}')
    else:
        bot.send_message(message.chat.id, get_other_user(user_tag=user_tag))

def stats(message, bot):
    user = registred(message=message)
    bot.send_message(message.chat.id, f'{user.pet}')

def train(message, bot):
    user = registred(message=message)
    user.train(message=message, bot=bot)

def feed(message, bot):
    user = registred(message=message)
    user.feed(message=message, bot=bot)

def attack(message, bot):
    user = registred(message=message)
    user.attack(message=message, bot=bot)

def sleep(message, bot):
    user = registred(message=message)
    user.sleep(message=message, bot=bot)

def shop(message, bot, item: str):
    user = registred(message=message)
    user.shop(message=message, bot=bot, item=item)
