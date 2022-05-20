from random import randint
from balans import many

slot = randint(1, 30)
bank = many


def game():
    global bank
    print('~~~Добро пожаловать в казино MAIN!\n'
          'Попытайте свою удачи в этом казино.\n'
          'Eсли угадаете то ваша ставка повыситься в 5 раз,\n'
          'Посмотрим как у вас с удачей поехали!~~~')
    try:
        while 1:
            print(f'Ваш нынешний баланс: {bank}')
            com = input('Сделайте свой выбор\n1 Играть \n2 Выйти\n')
            if com == '1':
                insrt = int(input('Выберите слот: '))
                stav = int(input('Сколько хотите поставить: '))
                if insrt == slot and stav <= bank:
                    bank += (stav * 5)
                    print('Вы угадали!')
                elif slot != insrt and stav <= bank:
                    if bank > 0 and stav <= bank:
                        bank -= stav
                        print('Вы не угадали!')
                elif bank == 0:
                    print('Вы проиграли все свои деньги')
                    break
                elif stav > bank:
                    print('У вас не хватает средств!')
            elif com == '2':
                if bank < 1000:
                    print('Вы в проиграше')
                    print('Игра окончена')
                    print(f'Ваша баланс {bank}')
                    break
                elif bank > 1000:
                    print('Вы в выигрыше')
                    print('Игра окончена')
                    print(f'Ваш баланс {bank}')
                    break
            else:
                print('Нет такого в меню!')
    except TypeError:
        print('Что-то пошло не так!')
    except ValueError:
        print('Пишите только числа!')
    except Exception:
        print('Что-то пошло не так')
