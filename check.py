Аким 2, [16.06.2023 19:37]
stock_currency_exchange_rate_usd = 70  # Задаем наши курсы валют
stock_currency_exchange_rate_eur = 80
income = 0.15  # Сколько мы (обменник) хотим заработать
requisites1 = 'Получатель: Иванов Иван Иванович\nБанк: OTP\nКарта получателя: 0000001234567899999\nВалюта счёта: RUB'
requisites2 = 'Получатель: Nikita Anisimov\nБанк:Bank of America\nКарта получателя: 0000001234567888889\nВалюта счёта: USD'
requisites3 = 'Получатель: Sergei Lavrov\nБанк: Raiffeisenlandesbank\nКарта получателя: 0000001234567778999\nВалюта счёта: EUR'

# скупка рублей, продажа валюты
def acceptable_currency_exchange_rate_rub_in_usd(stock_currency_exchange_rate_usd):
    while True:
        try:
            wanted_currency_exchange_rate_usd = float(input('По какому курсу вы хотели бы купить доллары?'))
            if wanted_currency_exchange_rate_usd >= usd_selling:
                satisfying_exchange_rate = wanted_currency_exchange_rate_usd
            else:
                agreement = input(f"К сожалению, мы не готовы провести операцию по такому курсу.\n"
                                 f"Предлагаемый курс: {usd_selling}\nВы согласны с таким курсом?").lower()
                if agreement == 'нет':
                    print('Всего доброго!')
                    return None
                elif agreement == 'да':
                    satisfying_exchange_rate = usd_selling
                else:
                    print('Пожалуйста, ответьте "да" или "нет".')
                    continue
            return satisfying_exchange_rate
        except ValueError:
            print('Пожалуйста, введите числовое значение.')


# то же самое, но для другой валюты
def acceptable_currency_exchange_rate_rub_in_eur(stock_currency_exchange_rate_eur):
    while True:
        try:
            wanted_currency_exchange_rate_eur = float(input('По какому курсу вы хотели бы купить евро?'))
            if wanted_currency_exchange_rate_eur >= eur_selling:
                satisfying_exchange_rate = wanted_currency_exchange_rate_eur
            else:
                agreement = input(f"К сожалению, мы не готовы провести операцию по такому курсу.\n"
                                 f"Предлагаемый курс: {eur_selling}\nВы согласны с таким курсом?").lower()
                if agreement == 'нет':
                    print('Всего доброго!')
                    return None
                elif agreement == 'да':
                    satisfying_exchange_rate = eur_selling
                else:
                    print('Пожалуйста, ответьте "да" или "нет".')
                    continue
            return satisfying_exchange_rate
        except ValueError:
            print('Пожалуйста, введите числовое значение.')


# покупка USD, продажа рублей (отн. фирмы)
def acceptable_currency_exchange_rate_usd_in_rub(stock_currency_exchange_rate_usd):
    while True:
        try:
            wanted_currency_exchange_rate_usd_in_rub = float(input('По какому курсу вы хотели бы продать доллары?'))
            if wanted_currency_exchange_rate_usd_in_rub <= usd_buying:
                satisfying_exchange_rate = wanted_currency_exchange_rate_usd_in_rub
            else:
                agreement = input(f"К сожалению, мы не готовы провести операцию по такому курсу.\n"
                                 f"Предлагаемый курс: {usd_buying}\nВы согласны с таким курсом?").lower()
                if agreement == 'нет':
                    print('Всего доброго!')
                    return None
                elif agreement == 'да':
                    satisfying_exchange_rate = usd_buying
                else:
                    print('Пожалуйста, ответьте "да" или "нет".')
                    continue
            return satisfying_exchange_rate
        except ValueError:
            print('Пожалуйста, введите числовое значение.')


# покупка EUR, продажа рублей (отн. фирмы)
def acceptable_currency_exchange_rate_eur_in_rub(stock_currency_exchange_rate_eur):
    while True:
        try:
            wanted_currency_exchange_rate_eur_in_rub = float(input('По какому курсу вы хотели бы продать евро?'))

Аким 2, [16.06.2023 19:37]
if wanted_currency_exchange_rate_eur_in_rub <= eur_buying:
                satisfying_exchange_rate = wanted_currency_exchange_rate_eur_in_rub
            else:
                agreement = input(f"К сожалению, мы не готовы провести операцию по такому курсу.\n"
                                 f"Предлагаемый курс: {eur_buying}\nВы согласны с таким курсом?").lower()
                if agreement == 'нет':
                    print('Всего доброго!')
                    return None
                elif agreement == 'да':
                    satisfying_exchange_rate = eur_buying
                else:
                    print('Пожалуйста, ответьте "да" или "нет".')
                    continue
            return satisfying_exchange_rate
        except ValueError:
            print('Пожалуйста, введите числовое значение.')


usd_selling = stock_currency_exchange_rate_usd * (1 + income)  # Курс продажи USD
usd_buying = stock_currency_exchange_rate_usd * (1 - income)  # Курс покупки USD
eur_selling = stock_currency_exchange_rate_eur * (1 + income)  # Курс продажи EUR
eur_buying = stock_currency_exchange_rate_eur * (1 - income)  # Курс покупки EUR

available_currency = input('Какую валюту вы хотели бы продать?').lower()  # Узнаем какая валюта имеется у покупателя
wanted_currency = input('Какую валюту вы хотели бы купить?').lower()  # Узнаем какую валюту покупатель хочет приобрести

if (available_currency == 'рубли' or available_currency == 'rub' or available_currency == 'rur') and \
        (wanted_currency == 'доллары' or wanted_currency == 'usd'):
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

elif (available_currency == 'рубли' or available_currency == 'rub' or available_currency == 'rur') and \
        (wanted_currency == 'евро' or wanted_currency == 'eur'):
    satisfying_exchange_rate = acceptable_currency_exchange_rate_rub_in_eur(stock_currency_exchange_rate_eur)
    if satisfying_exchange_rate is not None:
        while True:
            try:
                amount = float(input('Введите сумму, которую вы хотите обменять: '))
                result = amount / satisfying_exchange_rate
                print(f'Вы получите {round(result, 2)} евро')
                break
            except ValueError:
                print('Пожалуйста, введите числовое значение.')

elif (available_currency == 'доллары' or available_currency == 'usd') and \
        (wanted_currency == 'рубли' or wanted_currency == 'rub' or wanted_currency == 'rur'):
    satisfying_exchange_rate = acceptable_currency_exchange_rate_usd_in_rub(stock_currency_exchange_rate_usd)
    if satisfying_exchange_rate is not None:
        while True:
            try:
                amount = float(input('Введите сумму, которую вы хотите обменять: '))
                result = amount * satisfying_exchange_rate
                print(f'Вы получите {round(result, 2)} рублей')
                break
            except ValueError:
                print('Пожалуйста, введите числовое значение.')

elif (available_currency == 'евро' or available_currency == 'eur') and \
        (wanted_currency == 'рубли' or wanted_currency == 'rub' or wanted_currency == 'rur'):
    satisfying_exchange_rate = acceptable_currency_exchange_rate_eur_in_rub(stock_currency_exchange_rate_eur)
    if satisfying_exchange_rate is not None:
        while True:
            try:
                amount = float(input('Введите сумму, которую вы хотите обменять: '))
                result = amount * satisfying_exchange_rate
                print(f'Вы получите {round(result, 2)} рублей')
                break
            except ValueError:

Аким 2, [16.06.2023 19:37]
print('Пожалуйста, введите числовое значение.')

else:
    print('Извините, но данная операция недоступна.')


# Запрос пользовательского согласия на обмен
agreement = input('Вы согласны совершить обмен? (да/нет): ').lower()

if agreement == 'да':
    # Запрос данных пользователя
    debit_card = input('Введите карту списания средств (счет списания): ')
    credit_card = input('Введите карту зачисления средств (счет зачисления): ')

     # Отправка реквизитов для перевода в зависимости от выбранных валют
    if available_currency == 'рубли' or available_currency == 'rub' or available_currency == 'rur':
        print(f'Совершите перевод средств на реквизиты {requisites1}')
    elif available_currency == 'доллары' or available_currency == 'usd':
        print(f'Совершите перевод средств на реквизиты {requisites2}')
    elif available_currency == 'евро' or available_currency == 'eur':
        print(f'Совершите перевод средств на реквизиты {requisites3}')