
def programAction():  # Выводит на экран меню, получает номер меню, начало работы программы
    dict_tel = {1: ' - Показать все записи',
                2: ' - Найти запись по вхождению частей имени',
                3: ' - Найти запись по телефону',
                4: ' - Добавить новый контакт',
                5: ' - Удалить контакт',
                6: ' - Изменить номер телефона у контакта',
                7: ' - Выход'}
    print('-' * 50)
    print(f'Меню программы. ')
    print(f'Введите номер действия: ')
    print('-' * 50)
    for key, value in dict_tel.items():
        print(key, value)
    print('-' * 50)
    print()
    act_num = int(input(f'Ввод-> '))
    print()
    if act_num == 1:
        plain_text(fileName)
    if act_num == 2:
        find_persons(fileName)
    elif act_num == 3:
        tel_num(fileName)
    elif act_num == 4:
        addContact(fileName)
    elif act_num == 5:
        del_person(fileName)
    elif act_num == 6:
        change_tel(fileName)
    elif act_num == 7:
        print('Вы вышли из программы.')
        exit()
    else:
        print(f'Выбрано другое действие')


def plain_text(file_name):  # 1 - Показывает все записи. Осуществляет действие 1.
    print('-' * 50)
    print(f'Телефонный справочник: ')
    print('-' * 50)
    with open(file_name, 'r') as data:
        new_str = data.read()
        answer = ''
        for i in range(len(new_str) - 1):
            if new_str[i] != ',':
                answer += new_str[i]
        print(answer)
    print('-' * 50)
    print()
    programAction()


def find_persons(file_name):  # 2 Находит запись по вхождению частей имени
    person = input(f'Введите имя, фамилию, отчество, чтобы найти контакт человека: ')
    person = ' ' + person.lower()
    result = []
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            result.append(line.split(','))
    print('-' * 50)
    person_contact = ''
    for user in result:
        for item in user:
            if item.lower() == person or item.lower() == person.lstrip():
                person_contact = ' '.join(user)
                print(f"Найден контакт: {person_contact}")
    if person_contact == '':
        print(f"Человек не найден. Такого контакта не существует.")
    print('-' * 50)
    programAction()


def tel_num(file_name):  # 3 - Находит запись по телефону
    num = input(f'Введите номер телефона в формате 8987654321, чтобы найти запись: ')
    answer = ''
    result = []
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            result.append(line.split(','))
        for item in result:
            if item[3].lstrip() == num:
                for i in range(len(item) - 1):
                    if item[i] != ',':
                        answer += item[i]
        if answer != '':
            print(f'Найден контакт: {answer}')
    if answer == '':
        print(f"Телефон не найден. Такого контакта не существует.")
    print()
    programAction()


def addContact(file_name):  # 4 - Добавляет новый контакт
    print(f'Чтобы добавить новый контект')
    person_surname = input(f'Введите фимилию: ').capitalize()
    person_name = input(f'Введите имя: ').capitalize()
    person_patronymic = input(f'Введите отчество: ').capitalize()
    person_telephone = input(f'Введите телефон в формате 8987654321: ')
    new_data = [person_surname, person_name, person_patronymic, person_telephone]
    new_str = '\n' + ', '.join(new_data) + ','
    with open(file_name, 'a', encoding='utf-8') as data:
        data.writelines(new_str)
    print(f'Контакт добавлен в телефонную книгу. Для просмотра воспользуйтесь меню.')
    print()
    programAction()


def del_person(file_name):  # 5 Удаляет контакт
    print('-' * 50)
    print(f'Список контактов: ')
    print('-' * 50)
    result = []
    with open(file_name, 'r') as data:
        for line in data:
            result.append((line.split(','))[0:-1])
    for i in range(len(result)):
        result[i].insert(0, str((i + 1)) + ' -')
    for word in result:
        answer = ' '.join(word)
        print(answer)
    print('-' * 50)
    del_tel = int(input(f'Введите номер контакта, который хотите удалить: '))
    result.pop(del_tel - 1)
    result.reverse()
    new2_str = ''
    for line in result:
        new2_str = ','.join(line[1:]) + ',' + '\n' + new2_str

    with open(file_name, 'w', encoding='utf-8') as data:
        data.writelines(new2_str)
    print(f'Контакт удален из телефонной книги. Для просмотра воспользуйтесь меню.')

    print()
    programAction()


def change_tel(file_name):  # 6 Изменяет номер телефона у контакта
    print('-' * 50)
    print(f'Список контактов: ')
    print('-' * 50)
    result = []
    with open(file_name, 'r') as data:
        for line in data:
            result.append((line.split(','))[0:-1])
    for i in range(len(result)):
        result[i].insert(0, str((i + 1)) + ' -')
    for word in result:
        answer = ' '.join(word)
        print(answer)
    print('-' * 50)
    contact = input(f'Введите номер контакта, телефон которого хотите поменять: ')
    for line in result:
        if line[0][0] == contact:
            d = ' '.join(line[1:])
            print(f'Контакт номер телефона которого вы хотите заменить: {d}')
            line[-1] = input(f'Введите новый номер телефона: ')
            line[-1] = ' ' + line[-1]
    new3_str = ''
    for line in result:
        new3_str = ','.join(line[1:]) + ',' + '\n' + new3_str

    with open(file_name, 'w', encoding='utf-8') as data:
        data.writelines(new3_str)

    print(f'Изменен телефонный номер контакта. Для просмотра воспользуйтесь меню.')

    print()
    programAction()


fileName = 'tel.txt'
programAction()
