first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second == third:
    print('Все числа совпадают!')
elif first == second or first == third or second == first:
    print('Два числа совпадают!')
else: print('Cовпадений не найдено!')