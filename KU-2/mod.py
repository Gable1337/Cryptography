print("Введите два числа для вычисления остатка:")
a = int(input())
b = int(input())
p = a // b
mod_result = a - b * p
print(f"Встроенный оператор %: {a} % {b} = {a % b}")
print(f"Собственная функция mod: {a} % {b} = {mod_result}")