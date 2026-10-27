from storage import file_load, file_save

def show_all(my_list):
    if my_list == []:
        print("База данных пустая")
        print("")
        return
    for dict_info in my_list:
        print(f"Категория: {dict_info['category']} Расход: {dict_info['amount']}")
    print("")

def add_amount(my_list):
    while True:
        category = input("Введите категорию: ").replace('_',' ').strip().lower()
        if category != "":
            break
        else:
            print("Ошибка ввода, повторите ввод")
    while True:
        try:
            amount = float(input("Введите расход: "))
            if amount > 0:
                break
            else:
                print("Недопустимый расход")
        except ValueError:
            print("Ошибка: Неккоректный ввод, введите заново")
    print("")
    new_dict = {'category': category, 'amount': amount}
    my_list.append(new_dict)
    file_save(my_list)
    print("Добавлен новый расход")
    print("")

def sum_list(my_list):
    sum_amount = 0
    for dict_info in my_list:
        sum_amount += dict_info['amount']
    return sum_amount

def search_cat(my_list):
    amount_cat_dict = []
    while True:
        category = input("Введите категорию: ").replace('_',' ').strip().lower()
        if category != "":
            break
        else:
            print("Ошибка ввода, повторите ввод")
    print("")
    sum_num = 0
    for amount_list in my_list:
        if amount_list['category'] == category:
            amount_cat_dict.append(amount_list)
            sum_num += amount_list['amount']
    return amount_cat_dict, sum_num

def show_menu():
    print("")
    print("1) Показать все расходы")
    print("2) Добавить расход")
    print("3) Показать общую сумму расходов")
    print("4) Поиск расходов по категории")
    print("5) Выйти из программы")
    print("")
    while True: 
        try:
            result = int(input("Выберите действие: "))
            if result <= 5 and result > 0:
                break
            else:
                print("Ошибка: Недопустимый пункт")
        except ValueError:
            print("Ошибка: Неккоректный ввод, введите заново")
    print("")
    return result

expenses = file_load()
point = 0
launch = True
if expenses is None:
    launch = False
while point != 5 and launch == True:
    point = show_menu()
    match point:
        case 1:
            show_all(expenses)
        case 2:
            add_amount(expenses)
        case 3:
            result = sum_list(expenses)
            print(f"Сумма расходов {result}")
            print("")
        case 4:
            amount_dicts_cat, amount_sum = search_cat(expenses)
            if amount_dicts_cat == []:
                print("Категория не найдена")
            else:
                for amount_dict_cat in amount_dicts_cat:
                    print(f"Категория: {amount_dict_cat['category']} Расход: {amount_dict_cat['amount']}")
                print("")
                print(f"Общая сумма расходов по категории - {amount_sum}")
            print("")