

list_price = {'coffe': 150,'milk': 100,'wother': 50}


def start():
    global choice
    choice = input('Какой напиток выбирете?\n')
    if choice in list_price.keys():
        print(f'Вы выбрали {choice}, стоимость напитка составоляет {list_price.get(choice)} рублей'), money()
    else:
        print('У нас нет такого напитка, попробуйте еще раз'), start()


def money():
    if choice in list_price:
        bank_accaunt = int(input('Внесите сумму\n'))
        if bank_accaunt in list_price.values():
            print('Заберите ваш напиток')
            what_u_want = input('Хотите вернутся к выбору напитка или выйти? Для выхода нажмите E, для выбора напитка Y\n')
            if what_u_want == 'Y':
                start()
            if what_u_want == 'E':
                bye()


        elif bank_accaunt > list_price.get(choice):
            print(f'Заберите здачу{bank_accaunt - list_price.get(choice)}')
        elif bank_accaunt < list_price.get(choice):
            print(f'Вам не хватает {list_price.get(choice) - bank_accaunt}')
    else:
        print('Такого напитка нету! Возвращаю вас к выбору напитка'), start()


def bye():
    print('Приходите опячтьыварвпвпр')


















start()

