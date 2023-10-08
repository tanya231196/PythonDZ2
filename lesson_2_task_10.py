def bank(x,y):
    rate = 0.10
    result = x * (1 + rate) ** y
    return result
x = float(input("Введите сумму вклада: "))
y = int(input("Введите количество лет: "))
final_amount = bank(x, y)
print(f"Через {y} лет на вашем счету будет: {final_amount:.2f} рублей")
