# 3
# Пример Поступок, поведение или явление, служащее образцом для кого-л., чего-л.
# Задача Цель, к которой стремятся, которую хотят достичь.
# Учёба Процесс действия по значению глаг.: учиться.
# 4
# Пример
# Отличник
# Задача
# Пример

some_dict = {}
N = int(input())
for _ in range(N):
    line = input()
    some_dict[line.split()[0]] = line.split()[1:] # Разделяем строку, первое слово берем как ключ, остальное в строку
M = int(input())
some_list = [input() for _ in range(M)]
for key in some_list:
    if key in some_dict:
        # print(*some_dict[key]) # аналогично следующей строке
        print(' '.join(some_dict[key])) # join к разделителю применяет список
    else:
        print('Нет в словаре')

def arithmetic_operation(operation, x, y):
    if operation == '+':
        return x + y
    elif operation == '*':
        return x * y
    elif operation == '/':
        return x / y
    else:
        return x - y
print(arithmetic_operation('*', 5, 6))

def arithmetic_operation(operation):
    if operation == '+':
        return lambda x, y: x + y
    elif operation == '*':
        return lambda x, y: x * y
    elif operation == '/':
        return lambda x, y: x / y
    else:
        return lambda x, y: x - y
operation = arithmetic_operation('+')
print(operation(5, 6))

def simpl_map(transformation, values: list): # принимает список values (анотация)
    return list(map(transformation, values))
values = [1, 3, 5, 1, 7]
print(simpl_map(lambda x: x + 5, values))


some_list = list(filter(lambda x: x % 9 == 0, range(10, 100)))
some_list = list(map(lambda x: x ** 2, some_list))
print(some_list)
print(list(map(lambda x: x / 9, some_list)))