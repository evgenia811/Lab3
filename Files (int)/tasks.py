from functions import create_file, write_file, read_file
from functions import create_zip, add_file_in_zip, get_list_file_in_zip, extract_file
from functions import remove_file, parse_xml, get_info_file
from functions import write_json, read_json
from functions import write_xml, add_new_obj_xml


def task1():
    print("1. Вывести информацию в консоль о логических дисках, именах, метке тома, размере и типе файловой системы.")

    import psutil
    info_disk = psutil.disk_partitions()

    for i in range(len(info_disk)):
        print(info_disk[i])


def task2():
    print('\n2. Работа с файлами')

    # Создать файл
    name_file = input('Введите имя файла: ')
    create_file(name_file)
    print(f'Создан файл с именем "{name_file}"')

    # Записать в файл строку
    text = input('Введите строку для записи в файл:\n')
    write_file(name_file, text, rewrite_existing=False)
    print(f'Текст "{text}" записан в файл "{name_file}"')

    # Прочитать файл в консоль
    text_file = read_file(name_file)
    print(f'Текст из файла {name_file}:\n{text_file}')

    # Удалить файл
    text_print = remove_file(name_file)
    print(text_print)


def task3():
    # текстовый формат обмена данными, основан ан javascript
    print("\n3. Работа с форматом JSON")

    # Создать файл формате JSON в любом редакторе или с использованием данных, введенных пользователем
    name_file = 'json_file.json'

    # Прочитать файл в консоль
    data = read_json(name_file)
    print(data)

    # Создать новый объект. Выполнить сериализацию объекта в формате JSON и записать в файл.
    new_dict = {'fio': 'PopovaDL', 'group': 'BIS0-01-18', 'array': [1, 2, 'usdfh3']}

    new_name_file = 'new_json_file.json'
    write_json(new_name_file, new_dict)
    print('Новый объект сериализован в формат JSON и записан в файл')

    # Прочитать файл в консоль
    data = read_json(new_name_file)
    print(data)

    # Удалить файл
    text_print = remove_file(new_name_file)
    print(text_print)


def task4():
    # расширяемый язык разметки, для передачи данных
    print('\n4. Работа с форматом XML')
    # Создать файл формате XML из редактора
    name_file = 'xml_file.xml'
    name_new_file = 'new_xml_file.xml'

    print("Исходный файл:")
    xml_tree = parse_xml(name_file)
    new_tree = add_new_obj_xml(xml_tree)
    write_xml(name_new_file, new_tree, rewrite_existing=True)

    # Прочитать файл в консоль.

    print("\nИзменённый файл:")
    parse_xml(name_new_file)

    # Удалить файл.
    text_print = remove_file(name_new_file)
    print(text_print)


def task5():
    # формат архивации данных и сжатия без потерь данных
    path = 'for_zip'
    name_zip = 'test.zip'
    create_zip(path, name_zip)

    print('созданный архив')
    get_list_file_in_zip(name_zip)

    new_name_file = add_file_in_zip(name_zip)

    print('\nдобавляем один файл')
    get_list_file_in_zip(name_zip)

    extract_file(name_zip, new_name_file)

    get_info_file(new_name_file)

    print(new_name_file)
    print(remove_file(new_name_file))
    print(remove_file(name_zip))
    print('')


if __name__ == '__main__':

    tasks = [task1, task2, task3, task4, task5]

    text_tasks = '''
    1. Вывести информацию в консоль о логических дисках, именах, метке тома, размере и типе файловой системы.
    2. Работа с файлами
    3. Работа с форматом JSON
    4. Работа с форматом XML
    5. Создание zip архива, добавление туда файла, определение размера архива
    0. Выход'''

    while (True):
        print(text_tasks)

        num_task = int(input("Введите номер задания:  "))
        if num_task >= 1 and num_task <= 5:
            tasks[num_task - 1]()
        elif num_task == 0:
            exit()
        else:
            print('Такого номера задания нет, введите ещё раз')
