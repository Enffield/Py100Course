salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

money_capital = 0
i = 0
while True:
    money_capital += spend - salary
    spend *= 1 + increase
    if i < 9:
        i += 1
        continue
    break

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
