x = int(input('Введите число - '))
mx = 0
while x > 0:
    if ((x % 10) > mx):
        mx = x % 10
    else:
        x = x // 10
print(f"Максимальна цифра = {mx}")


