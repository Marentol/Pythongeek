p = 1.1
d = 1
start = int(input('Введите сколько пробежали за первый день - '))
finish = int(input('Укажите сколько км собираетесь пробежать - '))
while (start < finish):
    d += 1
    start *= p
print(f'Указанную дистанцию пробежите за {d} дней')