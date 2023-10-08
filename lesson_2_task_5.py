def month_to_season(number_of_month):
    if number_of_month == 1 or number_of_month == 2 or number_of_month == 12 : print("Зима")
    elif number_of_month == 3 or number_of_month == 4 or number_of_month == 5 : print("Весна")
    elif number_of_month == 6 or number_of_month == 7 or number_of_month == 8 : print("Лето")
    elif number_of_month == 9 or number_of_month == 10 or number_of_month == 11 : print("Осень")
    else:
        print("Неверный номер месяца")
number_of_month = int(input())
month_to_season(number_of_month)

