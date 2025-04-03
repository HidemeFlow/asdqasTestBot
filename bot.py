import asyncio
import logging
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
import time
logging.basicConfig(level=logging.INFO)
bot = Bot(token="8068734237:AAEX9kaR0u1rR8Huha6Ra5FJPNUiztfbH-A")
dp = Dispatcher()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="\"ХОЧУ УЗНАТЬ ПРО ПАРТНЕРКИ\"", callback_data="shag3")],
    [InlineKeyboardButton(text="\"ХОЧУ СИСТЕМУ\"", callback_data="shag12")]
])

keyboard2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Cмотреть мини презентацию о партнерках", callback_data="shag4")],
    [InlineKeyboardButton(text="МОЯ ГРУППА ТЕЛЕГРАМ ", url="https://t.me/botdarigetit")]
])
keyboard3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="КУПИТЬ ЗА 6000Р", url="https://t.me/miroslava_chizh")],
    [InlineKeyboardButton(text="ХОЧУ В КОМАНДУ", callback_data="shag13")],
    [InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="shag4")]
])
keyboard5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Регистрация в мою 1 линию", url="https://www.skill--boost.com?ref=margo1912")],
    [InlineKeyboardButton(text="Написать мне в лс", url="https://t.me/miroslava_chizh")],
    [InlineKeyboardButton(text="КУПИТЬ СИСТЕМУ", callback_data="shag12")],
    [InlineKeyboardButton(text="Смотреть стратегию", callback_data="shag4")],
])
keyboard4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="СТАРТ NEON X6", callback_data="shag5")],
    [InlineKeyboardButton(text="МИКРОМИЛЛИОНС", callback_data="shag6")],
    [InlineKeyboardButton(text="LUX+DREAMS", callback_data="shag7")],
    [InlineKeyboardButton(text="Задать вопрос", url="https://t.me/miroslava_chizh")],
    [InlineKeyboardButton(text="Регистрация в 1 линию", url="https://www.skill--boost.com?ref=margo1912")],
    [InlineKeyboardButton(text="Начать бесплатно", callback_data="shag11"),InlineKeyboardButton(text="Хочу систему", callback_data="shag12"),InlineKeyboardButton(text="Хочу в команду", callback_data="shag13")],
])
keyboard6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Хочу в команду", url="https://t.me/miroslava_chizh")],
    [InlineKeyboardButton(text="Микромиллионс", callback_data="shag6")],
    [InlineKeyboardButton(text="LUX+DREAMS", callback_data="shag7")],
    [InlineKeyboardButton(text="Регистрация в мою 1 линию", url="https://www.skill--boost.com?ref=margo1912")],
    [InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="shag4")],
    [InlineKeyboardButton(text="Начать бесплатно", callback_data="shag11"),InlineKeyboardButton(text="Хочу систему", callback_data="shag12"),InlineKeyboardButton(text="Хочу в команду", callback_data="shag13")],
])
keyboard7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="LUX+DREAMS", callback_data="shag7")],
    [InlineKeyboardButton(text="Хочу в команду", url="https://t.me/miroslava_chizh")],
    [InlineKeyboardButton(text="Регистрация в мою 1 линию", url="https://www.skill--boost.com?ref=margo1912")],
    [InlineKeyboardButton(text="Задать вопрос", url="https://t.me/miroslava_chizh")],
    [InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="shag4")],
])
keyboard8 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Хочу в команду", url="https://t.me/miroslava_chizh")],
    [InlineKeyboardButton(text="Регистрация в мою 1 линию", url="https://www.skill--boost.com?ref=margo1912")],
    [InlineKeyboardButton(text="Задать вопрос", url="https://t.me/miroslava_chizh")],
    [InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="shag4")],
])
keyboard9 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Регистрация в мою 1 линию", url="https://www.skill--boost.com?ref=margo1912")],
    [InlineKeyboardButton(text="Пиши в лс", url="https://t.me/miroslava_chizh")],
    [InlineKeyboardButton(text="КУПИТЬ СИСТЕМУ", callback_data="shag12")],
    [InlineKeyboardButton(text="ГОТОВ(А) К АКТИВАЦИИ", callback_data="shag13")],
    [InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="shag4")],
])

router = Router()

@dp.callback_query()
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    callback = callback_query
    if data == "shag3":
        await callback.message.answer("💡 Что я предлагаю?\n\n\nSkillBoost — это не просто обучающая платформа, а реальный инструмент для заработка. Здесь ты можешь одновременно учиться и зарабатывать, продвигая готовые партнёрские программы.\n\n\n🔹 Что внутри?\n\n\n ✅ Обширная библиотека курсов: маркетинг, бизнес, технологии, личностный рост.\n\n ✅ Возможность зарабатывать на партнёрках без отказов и впаривания.\n\n ✅ Простая система: выбираешь программу, подключаешься и начинаешь получать деньги.\n\n ✅ Быстрые результаты: я уже заработала 374 000₽, используя эту модель!\n\n\n🔹 Кому это подойдёт?\n\n ✔ Сетевикам, уставшим от бесконечного рекрутинга и ЛТО.\n\n ✔ Тем, кто хочет реально зарабатывать в интернете, а не просто надеяться.\n\n ✔ Всем, кто ценит свободу, быстрые деньги и систему без заморочек.\n\n\n📌 Готов(а) посмотреть как все работает изнутри? \n\nЖми кнопку и забирай свою стратегию заработка! 🚀", reply_markup=keyboard2)
    elif data == "shag12":
        await callback.message.answer_photo(FSInputFile("files/next3.jpg"))
        await callback.message.answer("Супер🔥 прямо сейчас ты уже можешь получить мою систему \"ТУРБО-ПРОКАЧКА СОЦСЕТЕЙ\" + пошаговые четкие действия на каждый день в соцсетях инстаграм,вк, телеграм, ютуб.\n\n\nБлагодаря системе вы за 7 дней упакуете правильно и грамотно свои соцсети, наполните целевыми постами, видео и будете знать какие конкретные действия делать каждый день для привлечения партнеров в свой бизнес\n\n\n+ получишь такого же готового бота рекрутера в телеграмм. Просто поставишь свои ссылки и информацию о своем проекте. На основе полученных знаний ты можешь создать свою систему для своей команды.\n\n\n✅Бот может  каждый день показывать десятки,тысячи презентаций твоего предложения, чего человек не сможет сделать за 1 день !\n\n✅Он отвечают на вопросы и возражения, делает всю рутинную работу.\n\n\nОбучение находится в телеграм. Доступ к каналу стоит 6000р единоразово. Доступ навсегда. Все обновления , которые будут добавляться в обучение уже бесплатно. Пиши мне в телеграм \"Хочу купить систему скиньте реквизиты\" https://t.me/miroslava_chizh\n\n\n", reply_markup=keyboard3)
    elif data == "shag4":
        await callback.message.answer("ВАЖНО СНАЧАЛА ПОСМОТРИ ЭТО ВИДЕО👇👇👇\n\n\nСкоростная стратегия движения в нашей команде NEON X6 + Микромиллионс+LUX+DREAMS. Как заработать минимум 8 миллионов руб.\n\n\nСМОТРЕТЬ НА ЮТУБ\n\n\n🔹 Если тебя заинтересовали партнёрские программы и наша скоростная стратегия, у тебя есть возможность детально ознакомиться с каждой из них.\n\n\n💸 Почему это работает?\n\n\n Каждая программа имеет чёткую систему, которая позволяет быстро выйти на доход. У нас управляемый маркетинг. А вместе эти программы дают на выходе от 8 млн рублей!\n\n\n🔥 Выбирай свой старт👇 как ты уже понял(а) стартуем мы с партнерской программы NEON X6 или же ты можешь активировать все 3 партнерские программы. Лучше по всем вопросам сразу пиши мне в личку.", reply_markup=keyboard4)
        # await callback.message.answer_video(FSInputFile("files/shag4.mp4"))
    elif data == "shag13":
        await callback.message.answer_photo(FSInputFile("files/next3.jpg"))
        await callback.message.answer("Всю эту уникальную систему можно получить в моей команде, при этом постоянно зарабатывать 50% по 3000р с каждой продажи моей системы и также выйдешь на доход от 30тыс и больше уже в первый месяц (если четко будешь следовать системе).\n\n\nТвой доход с каждым месяцем будет только расти. Вход в команду единоразовый. Активируешь партнерскую программу Neon X6 за 6000р и следуешь нашей скоростной стратегии. Советую еще раз посмотреть нашу командную стратегию. Если ты согласна (согласен) двигаться по стратегии, то добро пожаловать в команду.\n\n\n-У нас нет ЛТО, ежемесячных закупок\n\n-нет отложенных балансов\n\n-не инвестиции, не хайп\n\n-нет халявы\n\n\nВы зарабатываете деньги по маркетинг плану. У нас командная работа и каждый человек участвует в движении.\n\n\nПроходите регистрацию в мою 1 линию, после регистрации пишите мне в личку https://t.me/miroslava_chizh \"Я зарегистрировалась(ся) готова активировать NEON X6 6000Р\" пишите также свой логин , чтобы я проверила вашу регистрацию на сайте.\n\n\nКабинет будем пополнять вместе.\n\n\nПосле активации я добавляю вас в чат СТАРТ ЗАПУСК НОВИЧКА и рабочий чат. После того как вы посмотрели всю информацию и прошли первые уроки создали свою группу в телеграм , наполнили информацией , пригласили первых людей по обучению вы получаете доступ к системе \"ТУРБО ПРОКАЧКА СОЦСЕТЕЙ\" и начинаем активно работать.", reply_markup=keyboard5)
    elif data == "shag5":
        await callback.message.answer("Разбор Партнерской программы \n\n\nNEON X6 \n\nСМОТРИ ВИДЕО👇\n\n\nБыстрый старт 🏄‍♀ партнерская программа NEON X6 вход 6000₽. На выходе 36.000₽ бесконечно. Для более быстрого движения по партнерским программам идем по стратегии👇\n\n\nСТРАТЕГИЯ NEON X6👇\n\n\nС первой выплаты 18.000₽ мы активируем партнерскую программу LUX 10.000₽ , на вывод 8000₽. \n\n\nСо второй выплаты 18.000₽ мы активируем 7 уровень программы Микромиллионс 7.000₽. На вывод 11.000₽+ за каждого личинка вы получаете 6000₽ . +1 клон в 1 уровень и процесс начинается заново. \n\n\nКаждый клон вам приносит выплату 36.000₽. С каждой выплаты мы дополнительно ставим клонов 👆в LUX+МИКРОМИЛЛИОНС для ускорения движения. \n\n\nНа вывод вам постоянно 19.000₽ + реферальные по 6000₽ за каждого лично приглашенного человека.")
        await callback.message.answer_video("https://thinkandbiz.leadconverter.ru/vfile/8201355")
            # FSInputFile("files/shag5.mp4"))
        await callback.message.answer_photo(FSInputFile("files/shag5.jpg"))
        await callback.message.answer("Маркетинг наглядно👆", reply_markup=keyboard6)
    elif data == "shag6":
        await callback.message.answer("Разбор партнерской программы Микромиллионс\n\n\nСмотри видео👇\n\n\nСКОРОСТНАЯ СТРАТЕГИЯ МИКРОМИЛЛИОНС 👇👇👇вход 7000р сразу на 7 уровень\n\n\n🔥 с 7 по 9 уровень все на вывод , бонусы копятся.\n\n\nВсего 9 уровней😍🔥🚀 по нашей стратегии. \n\n\n7 уровень вход 7000₽. \n\n\nПо маркетингу: 500 бонусов копятся на балансе. 1200р на вывод. 300р наставнику.\n\n\n8 уровень. 1500 бонусов копятся на балансе. 2000р на вывод. 500р наставнику.\n\n\n9 уровень. 1700 бонусов копятся на балансе. 2300р на вывод. 1000р наставнику.\n\n\nСКОРОСТНАЯ СТРАТЕГИЯ 👇\n\n\n10 уровень. 12 000 бонусы. 20 000 р на вывод. 3000р наставнику.\n\n\nС 7 по 9 ур накопилось 3700 бонусов + 12.000 бонусов = 15.700 бонусов. \n\n\nНа 12.000 бонусов ставим 2 клона в NEON X6 за 6000₽.\n\n\nОстаток бонусов 3.700 оставляем на балансе. \n\n\nНа вывод 20 000р\n\n\n11 уровень. 6500 бонусов+ 3700 бонусов = 10 200 (3700 остаток с предыдущих уровней) Ставим 1 клона в LUX 10.000P. Остаток 200 бонусов. \n\n\n12 000р на вывод. 1500р наставнику. \n\n\n12 уровень. 14 000 бонусы. 23 500р на вывод. 2500р наставнику. \n\n\nНа 14 000 бонусов ставим 2 клона в 7 уровень микромиллионс за 7000₽\n\n\nС выплаты ставим 1 клона в NEON X6 6000₽. \n\n\nНа вывод 17.500₽\n\n\n13 уровень. 20 000 бонусы. 27 000р на вывод. 3000р наставнику. \n\n\nНа бонусы 14 000 ставим 2 клона в 7 ур. микромиллионс за 7000₽. Остаток 6000 бонусов ставим клона в NEON X6. \n\n\nНа вывод 27.000р.\n\n\n14 уровень. 95 000 бонусы. 100 000р на вывод. 5000р наставнику.\n\n\nНа бонусы ставим 2 клона в 10 ур.микромиллионс. и 2 клона в программу LUX M1. \n\nОстаток всего бонусов 5200.\n\n\nНа вывод 100 000р \n\n\n15 уровень. 200 000 бонусы. 1 270 000 р на вывод. 30 000р наставнику.\n\n\n129 000 бонусы ставим клоны в программу LUX М1,М2,М3,М4 и за 70 000 бонусов ставим 2 клона в 10 ур.микромиллионс.\n\n\nНа вывод 1 270 000р\n\n\nИтого на вывод с Микромиллионс\n\n1 442 000р на вывод.")
        # await callback.message.answer_video(FSInputFile("files/shag6.mp4"))
        await callback.message.answer_photo(FSInputFile("files/shag6_1.jpg"))
        await callback.message.answer_photo(FSInputFile("files/shag6_2.jpg"))
        await callback.message.answer_photo(FSInputFile("files/shag6_3.jpg"))
        await callback.message.answer("Маркетинг наглядно👆", reply_markup=keyboard7)
    elif data == "shag7":
        await callback.message.answer("Разбор партнерских программ LUX+DREAMS\n\nСМОТРИ ВИДЕО 👇\n\n\nСтратегия ЛЮКС+ЖИЛИЩНАЯ ПРОГРАММА:\n\n\nНа ЛЮКСЕ до 6 уровня всё на вывод. \n\n\nНачиная с 6 уровня распределяется следующим образом:\n\n\n6 УРОВЕНЬ: с выплаты (27 000 р) - 10 300 в движ (приобретаем клона в 1 уровень). Клоны по маркетингу в движ.\n\n\nНа вывод 16 700 р.\n\n\n7 УРОВЕНЬ: с выплаты (38 000 р) - 13 650 в движ (+ бонусы 6000 р приобретаем клона во 2 уровень). Клоны по маркетингу в движ.\n\n\nНа вывод 24 350 р.\n\n\n8 УРОВЕНЬ: с выплаты (95 000 р) - 40 370 р в движ (+ бонусы 25 000 р приобретаем 1 клон в 1 уровень, во 2 и в 3). Клоны по маркетингу в движ.\n\n\nНа вывод 54 630 р.\n\n\n9 УРОВЕНЬ: с выплаты (210 000 р) - 66 950 р в движ (+ бонусы 100 000 руб приобретаем 1 клон в 3 уровень и 2 клона в 4 уровень). Клоны по маркетингу в движ.\n\n\nНа вывод 143 050 р.\n\n\n10 УРОВЕНЬ: с каждой выплаты (1 000 000 р) - 232 750 р в движ (+ бонусы 350 000 руб приобретаем клон в жилищку, приобретаем 1 клон в 4 уровень ЛЮКС и 1 клон в 5уровень ЛЮКС). Так с каждой ножки.\n\n\n\nНа вывод с 10 уровня программы ЛЮКС - \n\nпо 767 250 р. с каждого места.\n\n\nЖИЛИЩНАЯ ПРОГРАММА DREAMS:\n\n\n10 УРОВЕНЬ: с выплаты (150 000 р) - 5 250 р в движ (+ бонусы 30 000 р приобретаем 1 клона в 3 уровень ЛЮКС). \n\n\nНа вывод 144 750 р\n\n\n12 УРОВЕНЬ: с выплаты (1 500 000 р) - 350 700 р в движ (+ бонусы 400 000 р приобретаем 1 клон в 7 уровень ЛЮКС, 1 клон в 6 уровень ЛЮКС, 1 клон в 5 уровень ЛЮКС, 1 клон в 4 уровень ЛЮКС, 1 клон в 3 уровень ЛЮКС). \n\n\nНа вывод 1 149 300 р\n\n\nС выплат (1 800 000 р) - 350 200 р в движ (+ бонусы 100 000 р приобретаем 1 клон в 7 уровень ЛЮКС, 1 клон в 4 уровень ЛЮКС, 1 клон в 3 уровень ЛЮКС). \n\n\nНа вывод по 1 449 800 р со 2 и с 3 места.\n\n\nИТОГО НА ВЫВОД 5 966 880 Р")
        # await callback.message.answer_video(FSInputFile("files/shag7.mp4"))
        await callback.message.answer_document(FSInputFile("files/shag7.pdf"))
        await callback.message.answer_photo(FSInputFile("files/shag7.jpg"))
        await callback.message.answer("С люкс мы сразу заходим на 10ур программы Dreams👆")
        await callback.message.answer("ВАЖНО ПОСЛЕ РЕГИСТРАЦИИ ПЕРЕД АКТИВАЦИЕЙ ПИШИ МНЕ В ЛС ЧТОБЫ ПОПАСТЬ ИМЕННО В МОЮ КОМАНДУ !!! https://t.me/miroslava_chizh", reply_markup=keyboard8)
    elif data == "shag11":
        # await callback.message.answer_video(FSInputFile("files/shag11.mp4"))
        await callback.message.answer("🚀 Бесплатный старт на платформе SkillBoost!\n\n\nХочешь разобраться в партнёрских программах и понять, как зарабатывать без вложений? Теперь у тебя есть возможность бесплатно зарегистрироваться на платформе и получить доступ к чату \"Запуск новичка\"!\n\n\nЧто ты получишь внутри?\n\n✅ Полное знакомство с платформой и партнёрскими программами\n\n✅ Пошаговые инструкции, как создать свою группу в Telegram и наполнить её контентом\n\n✅ Готовые скрипты, чтобы легко пригласить первых людей в свою группу и команду.\n\n✅ Рекомендации по ведению чата, чтобы он работал на тебя 24/7\n\n\nТы сможешь протестировать всё бесплатно, а если тебе понравится и ты решишь серьёзно развивать партнёрские программы и строить команду, то сможешь активировать партнёрскую программу и получить доступ к основному обучению по соцсетям и ведению блога без лица.\n\n\n🎯 Регистрируйся бесплатно прямо сейчас и заходи в чат \"Запуск новичка\"!\n\nНапиши @NatalyaKochetkova \"Хочу в чат\", и я отправлю тебе ссылку на регистрацию! 🚀", reply_markup=keyboard9)

    # Підтвердження отримання callback-запиту
    await bot.answer_callback_query(callback_query.id)

@dp.message(Command("start"))
async def start(message: Message):
    # await message.answer_video("https://thinkandbiz.leadconverter.ru/vfile/8201355")
    await message.answer_photo(FSInputFile("files/logo.png"))
    await message.answer("Привет🤗 меня зовут Мирослава Чиж.\n\nСейчас я тебе покажу как ты можешь создать постоянный входящий поток партнеров в свой бизнес.\n\n\nБлагодаря своей системе \"ТУРБО-ПРОКАЧКА СОЦСЕТЕЙ\" и 1 мощному инструменту я ежедневно получаю от 3-5 входящих заявок в бизнес. За несколько месяцев заработала 370тыс  на партнерских программах.\n\n\nСейчас я покажу как ты сможешь выйти на доход от 30тыс уже в первый месяц благодаря системе 👇👇👇\n\n\n✅\"ТУРБО-ПРОКАЧКА СОЦСЕТЕЙ\". Пошаговое обучение по запуску соцсетей в инстаграм,вконтакте,телеграм, ютуб.\n\n✅Чат- Бот рекрутер ,который будет работать 24/7 \n\n\nСЕЙЧАС ПОКАЖУ👇👇👇")
    time.sleep(27)
    await message.answer("Я потратила несколько лет на поиск работающей системы , которая позволяет работать на входящих заявках 😤\n\n\nПрошла кучу дорогостоящих обучений, взяла все самое лучшее, применила на практике и создала свою систему, благодаря которой заработала более 300тыс за несколько месяцев.\n\n\nСейчас вкратце расскажу, что за система дает такой результат👇")
    time.sleep(17)
    await message.answer("Итак первое моя авторская система \"ТУРБО-ПРОКАЧКА СОЦСЕТЕЙ\" + пошаговые четкие действия на 30 дней в соцсетях инстаграм,вк, телеграм, ютуб.\n\n\nБлагодаря системе вы за 7 дней упакуете правильно и грамотно свои соцсети, наполните целевыми постами, видео и будете знать какие конкретные действия делать каждый день для привлечения партнеров в свою команду.\n\n\nЗапустите сервисы и программы, которые будут привлекать ежедневно все новых людей на ваши страницы.\n\n\nПокажу как я общаюсь и закрываю сделки с кандидатами без созвонов и часовых зумов.\n\n\nИ дам четкие пошаговые шаги на 30 дней для быстрого старта . Даже с нуля можно запустить соцсети и настроить входящий поток.\n\n\n👇👇👇👇")
    time.sleep(26)
    await message.answer_photo(FSInputFile("files/next1.jpg"))
    await message.answer_photo(FSInputFile("files/next2.png"))
    await message.answer("👆👆Вот такие результаты входящие заявки в бизнес без рекламы. Так работает моя система \"ТУРБО-ПРОКАЧКА СОЦСЕТЕЙ\"\n\n\nЧТО ВХОДИТ В МОЮ СИСТЕМУ ТУРБО-ПРОКАЧКА СОЦСЕТЕЙ👇")
    await message.answer_photo(FSInputFile("files/next3.jpg"))
    await message.answer("Следующий мощный инструмент чат бот рекрутер в телеграмм. Он работает 24/7 ,пока я занята другими делами.\n\n\n✅Бот нужен для того, чтобы экономить время человеку.\n\n\n✅Он может проводить каждый день десятки,тысячи презентаций, чего человек не сможет сделать за 1 день !\n\n\n✅Он отвечает на вопросы и возражения, делает всю рутинную работу\n\n\n😎Бот рекрутер-это идеальный инструмент для работы\n\nМногие его недооценивают, т.к. не знают, что в нем дать и что писать\n\nЯ УВЕРЕНА, что ты тоже хочешь получать входящие заявки и поток партнеров в бизнес. ")
    time.sleep(27)
    await message.answer("КАК ЗАБРАТЬ ВСЮ ЭТУ СИСТЕМУ?\n\nДля тебя есть 2 варианта👇\n\n\n1. Присоединиться в мою команду и зарабатывать на партнерских программах. В первый месяц если четко следовать системе ты сможешь выйти на доход от 30тыс руб и дальше доход будет только расти. Жми кнопку в боте \"ХОЧУ УЗНАТЬ ПРО ПАРТНЕРКИ\" расскажу подробнее как мы зарабатываем.\n\n\n2. Ты можешь приобрести систему \"ТУРБО-ПРОКАЧКА СОЦСЕТЕЙ\" отдельно и использовать полученные знания в своем проекте, компании. Жми в боте кнопку \"ХОЧУ СИСТЕМУ\" расскажу что в нее входит.\n\n\nПройдя один раз систему, ты поймешь ,как строить бизнес и получать входящие, абсолютно в любом проекте!!!", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    # executor.start_polling(dp, skip_updates=True, run_single_instance=True)
    asyncio.run(main())
