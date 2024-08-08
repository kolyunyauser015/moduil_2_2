first = input('Ввведите первое число ')
second = input('Ввведите второе число ')
third = input('Ввведите третье число ')
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
