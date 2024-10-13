# -*- coding: utf-8 -*-

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

ans = 0
for i in range(months):
    ans += spend - salary
    spend *= (1+increase)
ans = round(ans)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", ans)
