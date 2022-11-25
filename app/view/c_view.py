from app.controller import ctrl


def menu():
    print('\nГлавное меню:\n'
          '\n1. Открыть CSV-файл\n'
          '2. Сохранить CSV-файл\n'
          '3. Показать все контакты\n'
          '4. Поиск контакта\n'
          '5. Добавить контакт\n'
          '6. Изменить контакт\n'
          '7. Удалить контакт\n'
          '8. Выход')
    return (int(input('Введите пункт меню: ')))


def main_loop():
    while True:
        choise = menu()
        match choise:
            case 1:
                btn_load_click()
            case 2:
                print('сохранение CSV не сделано')
            case 3:
                fill_main_table()
            case 4:
                btn_find_click()
            case 5:
                print('добавление не сделано')
            case 6:
                print('изменение не сделано')
            case 7:
                btn_remove_click()
            case 8:
                break


def fill_main_table(str_pattern=''):

    global main_table
    data = ctrl.get_data_from_database(str_pattern)
    for record in data:
        print(f'{record[0]} \t {record[1]} ')
    input('Нажмите <Enter> для продолжения...')


def btn_find_click():

    str_query = input('Введите текст для поиска: ')
    if str_query == '':
        clean_main_table()
        fill_main_table()
    else:
        clean_main_table()
        fill_main_table(str_query)


def btn_load_click():

    # file_name = input('Введите имя файла для загрузки: ')
    file_name = 'tel.csv'
    ctrl.load_from_csv(file_name)
    clean_main_table()
    fill_main_table()


def btn_remove_click():

    data = tuple(main_table.item(main_table.focus())['values'])
    if data == ():
        return
    ctrl.remove_data_from_database(data)
    clean_main_table()
    fill_main_table()


def clean_main_table():
    pass


def init():
    main_loop()
