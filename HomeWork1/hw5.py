cost = int(input('Введите издержки вашей фирмы - '))
proceed = int(input('Введите выручку вашей фирмы -'))
profit = proceed - cost
if(profit > 0):
        print('Ваша фирма приносит доход')
        rent = (profit/proceed)*100
        print(f'Рентабельность составляет - {rent}')
        staff = int((input('Введите число сотрудников - ')))
        st_profit = profit/staff
        print(f'Прибыль вашей фирмы на одного сотрудника составляет - {st_profit}')
else:
    print('Вы работаете на убыток')