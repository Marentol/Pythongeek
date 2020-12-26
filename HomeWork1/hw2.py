time_s = int(input('Введите время в секундах - '))
if (time_s >= 3600):
    h = time_s // 3600
    o = time_s % 3600  # Остаток секунд
    m = o // 60
    s = o % 60
    print(f"{h}:{m}:{s}")
elif(time_s >= 60):
    m = time_s // 60
    s = time_s % 60
    print(f"0:{m}:{s}")
else:
    print(f"0:0:{time_s}")