# -*- coding: utf-8 -*-
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

ans = 0
money_capital -= spend - salary
spend *= (1+increase)
while (money_capital > 0):
    ans+=1
    money_capital -= spend - salary
    spend *= (1+increase)

print("Количество месяцев, которое можно протянуть без долгов:", ans)
