from create_bot import bot, dp
from aiogram import types

stock_currency_exchange_rate_usd = 70  # Задаем наши курсы валют
stock_currency_exchange_rate_eur = 80
income = 0.15  # Сколько мы (обменник) хотим заработать
requisites1 = 'Получатель: Иванов Иван Иванович\nБанк: OTP\nКарта получателя: 0000001234567899999\nВалюта счёта: RUB'
requisites2 = 'Получатель: Nikita Anisimov\nБанк:Bank of America\nКарта получателя: 0000001234567888889\nВалюта счёта: USD'
requisites3 = 'Получатель: Sergei Lavrov\nБанк: Raiffeisenlandesbank\nКарта получателя: 0000001234567778999\nВалюта счёта: EUR'

usd_selling = stock_currency_exchange_rate_usd * (1 + income)  # Курс продажи USD
usd_buying = stock_currency_exchange_rate_usd * (1 - income)  # Курс покупки USD
eur_selling = stock_currency_exchange_rate_eur * (1 + income)  # Курс продажи EUR
eur_buying = stock_currency_exchange_rate_eur * (1 - income)


# скупка рублей, продажа валюты
@dp.message_handler(command='/start')
async def greeting(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Приветствую тебя в нашем боте {message.from_user.first_name}, данный бот поможет тебе обменивать валюты и смотреть курсы")


@dp.message_handler(command='/acceptablecurex')
async def acceptable_currency_exchange_rate_rub_in_usd(message: types.Message):
    while True:
        try:
            await bot.send_message(message.chat.id, 'По какому курсу вы хотели бы купить доллары?')
            wanted_currency_exchange_rate_usd = float(message.text)
            if wanted_currency_exchange_rate_usd >= usd_selling:
                satisfying_exchange_rate = wanted_currency_exchange_rate_usd
            else:
                await bot.send_message(message.chat.id,
                                       f"К сожалению, мы не готовы провести операцию по такому курсу.\n"
                                       f"Предлагаемый курс: {usd_selling}\nВы согласны с таким курсом?").lower()
                if message.text == 'нет':
                    await bot.send_message(message.chat.id, "Всего доброго")
                    return None
                elif message.text == 'да':
                    satisfying_exchange_rate = usd_selling
                else:
                    await bot.send_message(message.chat.id, 'Пожалуйста, ответьте "да" или "нет".')
                    continue
            return satisfying_exchange_rate
        except ValueError:
            await bot.send_message(message.chat.id, 'Пожалуйста, введите числовое значение.')


# то же самое, но для другой валюты
@dp.message_handler(command='/acceptcurexrubineur')
async def acceptable_currency_exchange_rate_rub_in_eur(stock_currency_exchange_rate_eur, message: types.Message):
    await bot.send_message(message.chat.id, "здесь вы получите курс валюты для рублей в евро")
    while True:
        try:
            await bot.send_message(message.chat.id, 'По какому курсу вы хотели бы купить евро?')
            wanted_currency_exchange_rate_eur = float(message.text)
            if wanted_currency_exchange_rate_eur >= eur_selling:
                satisfying_exchange_rate = wanted_currency_exchange_rate_eur
            else:
                await bot.sendMessage(message.chat.id, f"К сожалению, мы не готовы провести операцию по такому курсу.\n"
                                                       f"Предлагаемый курс: {eur_selling}\nВы согласны с таким курсом?").lower()
                if message.text == 'нет':
                    await bot.send_message(message.chat.id, 'Всего доброго!')
                    return None
                elif message.text == 'да':
                    satisfying_exchange_rate = eur_selling
                else:
                    await bot.send_message(message.chat.id, 'Пожалуйста, ответьте "да" или "нет".')
                    continue
            return satisfying_exchange_rate
        except ValueError:
            await bot.send_message(message.chat.id, 'Пожалуйста, введите числовое значение.')


# покупка USD, продажа рублей (отн. фирмы)
@dp.message_handler(command='/buyusdsellrub')
async def acceptable_currency_exchange_rate_usd_in_rub(stock_currency_exchange_rate_usd, message: types.Message):
    await bot.send_message(message.chat.id, "продажа usd и рублей относительно фирмы")
    while True:
        try:
            await bot.send_message(message.chat.id, "По какому курсу вы хотели бы продать доллары?")
            wanted_currency_exchange_rate_usd_in_rub = message.text
            if wanted_currency_exchange_rate_usd_in_rub <= usd_buying:
                satisfying_exchange_rate = wanted_currency_exchange_rate_usd_in_rub
            else:
                await bot.send_message(message.chat.id,
                                       f"К сожалению, мы не готовы провести операцию по такому курсу.\n"
                                       f"Предлагаемый курс: {usd_buying}\nВы согласны с таким курсом?").lower()
                if message.text == 'нет':
                    await bot.send_message(message.chat.id, 'Всего доброго!')

                elif message.text == 'да':
                    satisfying_exchange_rate = usd_buying
                else:
                    await bot.send_message(message.chat.id, 'Пожалуйста, ответьте "да" или "нет".')

        except ValueError:
            await bot.send_message(message.chat.id, 'Пожалуйста, введите числовое значение.')
    return satisfying_exchange_rate


# покупка EUR, продажа рублей (отн. фирмы)
@dp.message_handler(commands='/buyeursellrub')
async def acceptable_currency_exchange_rate_eur_in_rub(stock_currency_exchange_rate_eur, message: types.Message):
    await bot.send_message(message.chat.id, "покупка евро и продажа рубей относительно фирмы")
    while True:
        try:
            wanted_currency_exchange_rate_eur_in_rub = float(
                await bot.send_message(message.chat.id, 'По какому курсу вы хотели бы продать евро?'))
            if wanted_currency_exchange_rate_eur_in_rub <= eur_buying:
                satisfying_exchange_rate = wanted_currency_exchange_rate_eur_in_rub
            else:
                await bot.send_message(message.chat.id,
                                       f"К сожалению, мы не готовы провести операцию по такому курсу.\n"
                                       f"Предлагаемый курс: {eur_buying}\nВы согласны с таким курсом?").lower()
                if message.text == 'нет':
                    await bot.send_message(message.chat.id, 'Всего доброго!')
                elif message.text == 'да':
                    satisfying_exchange_rate = eur_buying
                else:
                    await bot.send_message(message.chat.id, 'Пожалуйста, ответьте "да" или "нет".')
                    continue
            return satisfying_exchange_rate
        except ValueError:
            await bot.send_message(message.chat.id, 'Пожалуйста, введите числовое значение.')

    usd_selling = stock_currency_exchange_rate_usd * (1 + income)  # Курс продажи USD
    usd_buying = stock_currency_exchange_rate_usd * (1 - income)  # Курс покупки USD
    eur_selling = stock_currency_exchange_rate_eur * (1 + income)  # Курс продажи EUR
    eur_buying = stock_currency_exchange_rate_eur * (1 - income)  # Курс покупки EUR

    await bot.send_message('Какую валюту вы хотели бы продать?').lower()  # Узнаем какая валюта имеется у покупателя
    await bot.send_message(message.chat.id,
                           'Какую валюту вы хотели бы купить?').lower()  # Узнаем какую валюту покупатель хочет приобрести

    if (message.text == 'рубли' or message.text == 'rub' or message.text == 'rur') and \
            (message.text == 'доллары' or message.text == 'usd'):
        satisfying_exchange_rate = acceptable_currency_exchange_rate_rub_in_usd(stock_currency_exchange_rate_usd)
        if satisfying_exchange_rate is not None:
            while True:
                try:
                    amount = float(input('Введите сумму, которую вы хотите обменять: '))
                    result = amount / satisfying_exchange_rate
                    print(f'Вы получите {round(result, 2)} долларов')
                    break
                except ValueError:
                    print('Пожалуйста, введите числовое значение.')

    elif (message.text == 'рубли' or message.text == 'rub' or message.text == 'rur') and \
            (message.text == 'евро' or message.text == 'eur'):
        satisfying_exchange_rate = acceptable_currency_exchange_rate_rub_in_eur(stock_currency_exchange_rate_eur)
        if satisfying_exchange_rate is not None:
            while True:
                try:
                    amount = float(
                        await bot.send_message(message.chat.id, 'Введите сумму, которую вы хотите обменять: '))
                    result = amount / satisfying_exchange_rate
                    await bot.send_message(message.chat.id, f'Вы получите {round(result, 2)} евро')
                    break
                except ValueError:
                    await bot.send_message(message.chat.id, 'Пожалуйста, введите числовое значение.')

    elif (message.text == 'доллары' or message.text == 'usd') and \
            (message.text == 'рубли' or message.text == 'rub' or message.text == 'rur'):
        satisfying_exchange_rate = acceptable_currency_exchange_rate_usd_in_rub(stock_currency_exchange_rate_usd)
        if satisfying_exchange_rate is not None:
            while True:
                try:
                    amount = float(input('Введите сумму, которую вы хотите обменять: '))
                    result = amount * satisfying_exchange_rate
                    await bot.send_message(message.chat.id, f'Вы получите {round(result, 2)} рублей')
                    break
                except ValueError:
                    print('Пожалуйста, введите числовое значение.')

    elif (message.text == 'евро' or message.text == 'eur') and \
            (message.text == 'рубли' or message.text == 'rub' or message.text == 'rur'):
        satisfying_exchange_rate = acceptable_currency_exchange_rate_eur_in_rub(stock_currency_exchange_rate_eur)
        if satisfying_exchange_rate is not None:
            while True:
                try:
                    await bot.send_message(message.chat.id, 'Введите сумму, которую вы хотите обменять: ')
                    amount = float(message.text)
                    result = amount * satisfying_exchange_rate
                    await bot.send_message(message.chat.id, f'Вы получите {round(result, 2)} рублей')
                    break
                except ValueError:
                    await bot.send_message(message.chat.id, 'Пожалуйста, введите числовое значение.')

    else:
        await bot.send_message(message.chat.id, 'Извините, но данная операция недоступна.')

    # Запрос пользовательского согласия на обмен
    await bot.send_message(message.chat.id, 'Вы согласны совершить обмен? (да/нет): ').lower()

    if message.text == 'да':
        # Запрос данных пользователя
        await bot.send_message(message.chat.id, 'Введите карту списания средств (счет списания): ')
        debit_card = message.text
        await bot.send_message(message.chat.id, 'Введите карту зачисления средств (счет зачисления): ')
        credit_card = message.text
        # Отправка реквизитов для перевода в зависимости от выбранных валют
        if message.text == 'рубли' or message.text == 'rub' or message.text == 'rur':
            await bot.send_message(message.chat.id, f'Совершите перевод средств на реквизиты {requisites1}')
        elif message.text == 'доллары' or message.text == 'usd':
            await bot.send_message(message.chat.id, f'Совершите перевод средств на реквизиты {requisites2}')
        elif message.text == 'евро' or message.text == 'eur':
            await bot.send_message(message.chat.id, f'Совершите перевод средств на реквизиты {requisites3}')
        while True:
            await bot.send_message(message.chat.id, 'Сделали ли Вы перевод? (да/нет): ').lower()
            if message.text == 'да':
                await bot.send_message(message.chat.id, 'Спасибо за сотрудничество, ожидайте зачисление средств!')
                break
            elif message.text == 'нет':
                continue
            else:
                await bot.send_message('Пожалуйста, ответьте "да" или "нет".')

    if message.text == "нет":
        await bot.send_message(message.chat.id, 'Если что - обращайтесь')

    # Вывод информации о заявке для администратора
    await bot.send_message(message.chat.id, 'Информация для администратора:')
    await bot.send_message(message.chat.id, 'Новая заявка!')
    await bot.send_message(message.chat.id, f'счет списания: {debit_card}')
    await bot.send_message(message.chat.id, f'счет зачисления: {credit_card}')
    await bot.send_message(message.chat.id, f'сумма перевода: {round(result, 2)}')
    await bot.send_message(message.chat.id, 'заявка оплачена')
