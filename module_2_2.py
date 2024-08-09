first = int(input('Ввведите первое число '))
second = int(input('Ввведите второе число '))
third = int(input('Ввведите третье число '))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
