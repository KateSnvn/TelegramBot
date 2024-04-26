#!/usr/bin/python
# -*- coding: utf8 -*-
from telebot import types
import telebot
import webbrowser
import datetime
from random import choice

bot = telebot.TeleBot('6553458062:AAHi4h31BqATZurfdnPRmNIPdu983uPvFMc')


@bot.message_handler(commands=['training'])
def recips(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Мужчина: новичок')
    btn2 = types.KeyboardButton('Мужчина: профи')
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton('Женщина: новичок')
    btn4 = types.KeyboardButton('Женщина: профи')
    markup.row(btn3, btn4)
    bot.send_message(message.chat.id, '<b>Хотите привести себя в порядок? Вот, план тренировок для вас:</b>', reply_markup=markup, parse_mode='html')
    bot.register_next_step_handler(message, on_click4)
@bot.message_handler(commands=['training'])
def on_click4(message):
    trening_male_novichek = 'Вот пример программы тренировок для мужчины-новичка, которую можно выполнять 3 раза в неделю. Программа включает упражнения на основные группы мышц: грудь, спину, плечи, ноги и корпус. Перед началом тренировок рекомендуется проконсультироваться с врачом или тренером для подбора оптимальной нагрузки.\n\nДень 1: Грудь и трицепс\n  1. Жим гантелей лежа - 3х10-12 повторений\n  2. Отжимания на брусьях - 3х10-12 повторений\n  3. Французский жим - 3х10-12 повторений\n  4. Скручивания - 3х15-20 повторенийДень\n\nДень 2: Ноги и бицепс\n  1. Приседания со штангой - 3х10-12 повторений\n  2. Жим ногами в тренажере - 3х10-12 повторений\n  3. Молотки - 3х10-12 повторений\n  4. Подъемы ног в висе - 3х15-20 повторений\n\nДень 3: Спина и плечи\n  1. Тяга верхнего блока - 3х10-12 повторений\n  2. Подтягивания на горизонтальной перекладине - 3х10-12 повторений\n  3. Армейский жим - 3х10-12 повторений\n  4. Подтягивания к подбородку - 3х10-12 повторений\n\nПостепенно увеличивайте веса и количество повторений, чтобы поддерживать прогресс тренировок. Не забывайте также о правильном питании, режиме сна и отдыхе, которые играют важную роль в процессе набора мышечной массы и укрепления здоровья.\n\nУдачи в тренировках!'
    trening_male_profi = 'Для профессионалов в тренировках можно предложить более сложную и интенсивную программу, которая поможет добиться новых результатов и развития физической формы. Пожалуйста, ознакомьтесь с примерной программой тренировок для мужчины-профи:\n\nДень 1: Грудь и трицепс\n  1. Жим штанги лежа - 4х6-8 повторений\n  2. Скручивания на наклонной скамье с гантелями - 4х10-12 повторений\n  3. Жим гантелей сидя на наклонной скамье - 4х8-10 повторений\n  4. Французский жим - 3х8-10 повторений\n\nДень 2: Ноги и плечи\n  1. Приседания со штангой - 4х6-8 повторений\n  2. Жим штанги стоя - 4х6-8 повторений\n  3. Гакк-приседания - 3х8-10 повторений\n 4. Подъемы гантелей через стороны - 3х10-12 повторений\n\nДень 3: Спина и бицепс\n  1. Тяга штанги к поясу - 4х6-8 повторений\n  2. Подтягивания взвешенные - 4х6-8 повторений\n  3. Молотки - 3х8-10 повторений\n  4. Сгибания рук с грифом - 3х10-12 повторений\n\nТакже рекомендуется включить в программу высокоинтенсивные кардио упражнения для поддержания хорошей физической формы и ускорения обмена веществ. Помните, что качественный отдых, правильное питание и удовлетворение физиологических потребностей играют важную роль в достижении поставленных целей. Не забывайте проконсультироваться с тренером перед началом новой программы тренировок.\n\nУдачи!'
    trening_female_novichek = 'Вот программа тренировок для женщин-новичков:\n\n1. Разминка (5-10 минут):\n  - Небыстрое бегание на месте - 2 минуты\n  - Разведение рук и ног - 1 минута\n  - Приседания без отягощения - 2 минуты\n\n2. Силовые упражнения (3 круга):\n  - 10 отжиманий от пола\n  - 15 приседаний\n  - 12 подъемов на носки\n  - 10 подтягиваний на турнике или с гироскутером\n\n3. Кардио (выберите один вид):\n  - Бег на беговой дорожке/улице (10-15 минут)\n  - Велотренажер (15 минут)\n  - Быстрая ходьба с подъемом в гору (20 минут)\n\n4. Растяжка и отдых (5-10 минут):\n  - Плечевая растяжка - 1 минута\n  - Растяжка ног - 2 минуты\n  - Вдох-выдох, расслабление - 2 минуты\n\nНе забывайте выполнять упражнения правильно, следить за своим дыханием и не перенапрягаться. Помните, что регулярные тренировки и правильное питание помогут вам достичь желаемых результатов.\n\nУдачи!\n\nЕсли у вас есть какие-либо заболевания или проблемы со здоровьем, обязательно проконсультируйтесь с врачом перед началом тренировок.'
    trening_female_profi = 'Вот программа тренировок для женщин-профессионалок:\n\n1. Разминка (10-15 минут):\n  - Бег на беговой дорожке или на улице (5-10 минут)\n  - Динамическая растяжка всего тела (5 минут)\n\n2. Силовые упражнения (4 круга):\n  - 15 отжиманий от пола- 20 приседаний с гантелями\n  - 12 подтягиваний на турнике с весом\n  - 15 выпадов с гантелями\n\n3. Кардио и выносливость (выберите один вид):\n  - Интервальный бег (30 минут) - чередуйте спринты и медленный бег\n  - HIIT тренировка (High-Intensity Interval Training) - 4 раунда по 4 минуты активной работы и 1 минуте отдыха\n  - Эллиптический тренажер или велосипед (20-30 минут интенсивной тренировки)\n\n4. Функциональная тренировка (3 круга):\n  - 10 подтягиваний на перекладине\n  - 15 берпи (включая отжимания и прыжки)- 20 взрывных отжиманий\n  - 15 подъемов гантелей над головой на прессе\n\n5. Растяжка и восстановление (10-15 минут):\n  - Глубокая статическая растяжка различных групп мышц (ноги, спина, плечи, грудь)\n  - Дыхательные упражнения и расслабление\n\nЭта программа предназначена для женщин с опытом в фитнесе и физической подготовке на высоком уровне. Важно правильно выполнять упражнения, следить за техникой и не перенапрягаться. Программа разнообразная и интенсивная, поможет поддерживать высокую форму, развивать силу, выносливость и гибкость. Не забывайте также включать в рацион правильное питание и достаточный отдых для эффективных результатов.'
    if message.text == 'Мужчина: новичок':
        bot.send_message(message.chat.id, f'{trening_male_novichek}')
    elif message.text == 'Мужчина: профи':
        bot.send_message(message.chat.id, f'{trening_male_profi}')
    elif message.text == 'Женщина: новичок':
        bot.send_message(message.chat.id, f'{trening_female_novichek}')
    elif message.text == 'Женщина: профи':
        bot.send_message(message.chat.id, f'{trening_female_profi}')


@bot.message_handler(commands=['recips'])
def recips(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Завтрак')
    btn2 = types.KeyboardButton('Перекус')
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton('Обед')
    btn4 = types.KeyboardButton('Ужин')
    markup.row(btn3, btn4)
    bot.send_message(message.chat.id, '<b>Не знаете что приготовить? Вот, список интересных рецептов:</b>', reply_markup=markup, parse_mode='html')
    bot.register_next_step_handler(message, on_click3)

@bot.message_handler(commands=['recips'])
def on_click3(message):
    breakfast = ['Омлет с овощами:\n - Разбейте яйца в миску, добавьте порезанные овощи (помидоры, перец, лук) и зелень. \n- Вылейте смесь на сковороду и обжарьте до готовности. \n- Подавайте с тостами или свежими овощами.',
                 'Овсянка с фруктами и орехами:\n - Сварите овсянку на молоке или воде.\n - Добавьте порезанные фрукты (ягоды, банан, яблоко) и измельченные орехи. \n - Полейте медом или кленовым сиропом.',
                 'Греческий йогурт с медом и орехами:\n - Положите греческий йогурт в чашку.\n - Поставьте сверху порцию меда и измельченных орехов.\n - Подавайте с чашкой свежих ягод.']

    dinner = ['Куриный салат с авокадо:\n - Приготовьте куриную грудку, порежьте на кубики.\n - Добавьте кубики авокадо, помидоры, огурцы, листья салата.\n - Заправьте лимонным соком и оливковым маслом.',
              'Паста с овощами:\n - Сварите пасту аль денте.\n - Обжарьте на сковороде лук, помидоры, перец, кабачок.\n - Перемешайте с пастой, посыпьте тертым пармезаном.',
              'Чили с мясом и фасолью:\n - Обжарьте фарш с луком и чесноком.\n - Добавьте консервированную фасоль, томатную пасту, специи.\n - Тушите под крышкой около 30 минут.']

    supper = ['Гриль с лососем и овощами:\n - Замаринуйте лосось с лимонным соком, чесноком, зеленью.\n - Запекайте на гриле до готовности.\n - Подавайте с запеченными овощами.',
              'Темный рис с курицей и овощами:\n - Сварите рис.\n - Обжарьте куриную грудку и овощи (брокколи, грибы, морковь).\n - Смешайте все ингредиенты и заправьте соевым соусом.',
              'Запеченные бататы с фаршем:\n - Запеките бататы в духовке.\n - Обжарьте фарш с луком, морковью, специями.\n - Выложите фарш на бататы, посыпьте сыром и запекайте.']

    snack = ['Фруктовый салат:\n - Нарежьте фрукты небольшими кусочками (яблоки, апельсины, груши).\n - Полейте натертым имбирем и соком лайма.\n - Посыпьте гранолой или измельченными орехами.',
             'Гуакамоле с овощами:\n- Разотрите авокадо с лимонным соком, солью, перцем.\n - Подавайте с палочками моркови, перца, сельдерея.',
             'Греческий йогурт со смесью орехов:\n - Смешайте измельченные грецкие орехи, миндаль и фундук.\n - Добавьте к греческому йогурту и полейте медом.']
    if message.text == 'Завтрак':
        bot.send_message(message.chat.id, f'{choice(breakfast)}')
    elif message.text == 'Перекус':
        bot.send_message(message.chat.id, f'{choice(snack)}')
    elif message.text == 'Обед':
        bot.send_message(message.chat.id, f'{choice(dinner)}')
    elif message.text == 'Ужин':
        bot.send_message(message.chat.id, f'{choice(supper)}')




@bot.message_handler(commands=['joke'])
def joke(message):
    anekdots = ['На чемпионате мира по плаванию наш спортсмен занял третий шкафчик.',
'Робин Гуд впадал в ступор, встречая людей среднего достатка.',
'Жизнь коротка - не успеешь оглянуться, как уже никуда не успел.',
'Если вы ущипнули себя, но видение не исчезло - ущипните видение.',
'Если делить по-честному, то поровну не получается...',
'Жизнь удалась, если ты знаком с Федотом и Яковом.',
'Самый надежный способ сохранить свои деньги - забыть, куда ты их спрятал.',
'Возраст искусственной елки можно узнать, посчитав кольца скотча на ее коробке.',
'Мальчик Серёжа был настолько ленив, что просыпался пораньше, чтобы побольше ничего не делать.',
'Решили дед и бабка не повторять прошлых ошибок и вместо колобка испекли кубик.']
    bot.send_message(message.chat.id, f'{choice(anekdots)}')


@bot.message_handler(commands=['buy'])
def buy(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт DNS')
    btn2 = types.KeyboardButton('Перейти на сайт Эльдорадо')
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton('Перейти на сайт Wildberries')
    btn4 = types.KeyboardButton('Перейти на сайт OZON')
    markup.row(btn3, btn4)
    btn5 = types.KeyboardButton('Перейти на сайт Пятёрочка')
    btn6 = types.KeyboardButton('Перейти на сайт Магнит')
    markup.row(btn5, btn6)
    bot.send_message(message.chat.id, '<b>Хотите что-то купить? Вот, список популярных интернет-магазинов:</b>', reply_markup=markup, parse_mode='html')
    bot.register_next_step_handler(message, on_click2)

def on_click2(message):
    if message.text == 'Перейти на сайт DNS':
        bot.send_message(message.chat,id, webbrowser.open('https://dns-shop.ru'))
    elif message.text == 'Перейти на сайт Эльдорадо':
        bot.send_message(message.chat, id, webbrowser.open('https://eldorado.ru'))
    elif message.text == 'Перейти на сайт Wildberries':
        bot.send_message(message.chat, id, webbrowser.open('https://wildberries.ru'))
    elif message.text == 'Перейти на сайт OZON':
        bot.send_message(message.chat, id, webbrowser.open('https://ozon.ru'))
    elif message.text == 'Перейти на сайт Пятёрочка':
        bot.send_message(message.chat, id, webbrowser.open('https://5ka.ru'))
    elif message.text == 'Перейти на сайт Магнит':
        bot.send_message(message.chat, id, webbrowser.open('https://magnit.ru'))


@bot.message_handler(commands=['time'])
def main(message):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    bot.send_message(message.chat.id, f'<b>Московское время сейчас:</b> \n {current_time}', parse_mode='html')



@bot.message_handler(commands=['site'])
def site(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт Google')
    btn2 = types.KeyboardButton('Перейти на сайт Кинопоиск')
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton('Перейти на сайт Youtube')
    btn4 = types.KeyboardButton('Перейти на сайт VK')
    markup.row(btn3, btn4)
    btn5 = types.KeyboardButton('Перейти на сайт Погоды')
    btn6 = types.KeyboardButton('Перейти на сайт Карт')
    markup.row(btn5, btn6)
    btn7 = types.KeyboardButton('Перейти на сайт Курса Валют')
    markup.row(btn7)
    bot.send_message(message.chat.id, '<b>Выберите сайт</b>', reply_markup=markup, parse_mode='html')
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт Youtube':
        bot.send_message(message.chat,id, webbrowser.open('https://youtube.com'))
    elif message.text == 'Перейти на сайт VK':
        bot.send_message(message.chat,id, webbrowser.open('https://vk.com'))
    elif message.text == 'Перейти на сайт Кинопоиск':
        bot.send_message(message.chat,id, webbrowser.open('https://kinopoisk.ru'))
    elif message.text == 'Перейти на сайт Google':
        bot.send_message(message.chat,id, webbrowser.open('https://google.com'))
    elif message.text == 'Перейти на сайт Погоды':
        bot.send_message(message.chat,id, webbrowser.open('https://gismeteo.ru'))
    elif message.text == 'Перейти на сайт Карт':
        bot.send_message(message.chat,id, webbrowser.open('https://google.com/maps'))
    elif message.text == 'Перейти на сайт Курса Валют':
        bot.send_message(message.chat,id, webbrowser.open('https://cbr.ru'))


'''
@bot.message_handler(commands=['site'])
def get_site(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт Youtube', url='https://youtube.com')
    btn2 = types.InlineKeyboardButton('Перейти на сайт VK', url='https://vk.com')
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton('Перейти на сайт Кинопоиск', url='https://kinopoisk.ru')
    btn4 = types.InlineKeyboardButton('Перейти на сайт Google', url='https://google.com')
    markup.row(btn3, btn4)
    btn5 = types.InlineKeyboardButton('Перейти на сайт Погоды', url='https://gismeteo.ru')
    btn6 = types.InlineKeyboardButton('Перейти на сайт Карт', url='https://google.com/maps')
    markup.row(btn5, btn6)
    btn7 = types.InlineKeyboardButton('Перейти на сайт Курса Валют', url='https://cbr.ru')
    markup.row(btn7)
'''

'''
@bot.message_handler(commands=['google'])
def site(message):
    webbrowser.open('https://google.com')

@bot.message_handler(commands=['youtube'])
def site(message):
    webbrowser.open('https://youtube.com')

@bot.message_handler(commands=['movie'])
def site(message):
    webbrowser.open('https://kinopoisk.ru')

@bot.message_handler(commands=['vk'])
def site(message):
    webbrowser.open('https://vk.com')

@bot.message_handler(commands=['weather'])
def site(message):
    webbrowser.open('https://gismeteo.ru')

@bot.message_handler(commands=['map'])
def site(message):
    webbrowser.open('https://google.com/maps')

@bot.message_handler(commands=['exchange'])
def site(message):
    webbrowser.open('https://cbr.ru')
'''


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.username}!')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f'<b>Выберите из списка команд, с чем вам может помочь бот:</b> \n /start - Начать работу с ботом \n /help - Вызвать меню помощи \n /site - Вызвать меню для перехода на один из доступных сайтов \n /buy - Вызвать меню для перехода на один из доступных интернет-магазинов \n /time - Узнать Московское время \n /joke - Бот расскажет вам анекдот \n /recips - Выведет интересный рецепт на любой прием пищи', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.username}!')
    elif message.text.lower() == 'помоги':
        bot.reply_to(message, f'Конечно! Выберите из списка команд, с чем вам может помочь бот')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == 'как тебя зовут?':
        bot.reply_to(message, f'Меня зовут IT Telegram Bot')
    else:
        bot.reply_to(message, f'Я вас не понимаю')

bot.polling(none_stop=True)