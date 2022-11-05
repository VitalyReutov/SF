Quantity_tickets = int(input("Введите количество билетов: "))

Total_amount_rub = 0

for i in range(Quantity_tickets):
        age = int(input("Введите ваш возраст: "))
        if age < 18:
            Total_amount_rub += 0
        elif 18 <= age < 25:
            Total_amount_rub += 990
        else:
            Total_amount_rub += 1390
if Quantity_tickets <= 3:
    print(Total_amount_rub)
else:
    print(Total_amount_rub*0.9)

