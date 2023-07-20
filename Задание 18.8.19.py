sum_tickets = 0
quantity_tickets = int(input("Введите количество билетов:"))
for age in range(quantity_tickets):
    age = int(input("Введите возраст посетителя:"))
    if age <18:
        sum_tickets += 0
    elif 18 <= age <= 25:
        sum_tickets += 990
    elif age > 25:
        sum_tickets += 1390
print("Стоимость белетов-", sum_tickets, "Рублей")
if quantity_tickets > 3:
    print("Сумма к оплате с учетом скидки-", (sum_tickets-(sum_tickets/100)*10), "Рублей")
