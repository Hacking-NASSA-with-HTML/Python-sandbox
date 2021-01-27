today = list()  # today = []
tomorrow = list()  # tomorrow = []
other = list()  # other = []


HELP = """
Список доступных комманд:
* print - напечатать все задачи на заданную дату
* todo - добавить задачу
* help - напечатать help
* exit - выход
"""


while True:
    command = input("Введите команду\n")
    if command == "help":
        print(HELP)
    elif command == "todo":
        date = input("Введите дату: ")
        task = input("Введите задачу: ")
        if date.lower() == "Сегодня":
            today.append(task)
        elif date == "Завтра":
            tomorrow.append(task)
        else:
            other.append(task)
        print(f"Задача {task} добавлена")
    elif command == "print":
        print("Сегодня")
        for task in today:
            print(task)
        print("Завтра")
        for task in tomorrow:
            print(task)
        print("Другие")
        for task in other:
            print(task)
    elif command == "exit":
        print("Спасибо за использование!")
        break
    else:
        print("Неизвестная команда")
        break