def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def main():
    a, b = map(int, input("Введите числа a и b (пример: '24 2'): ").split())
    result = gcd(a, b)
    print(f"Наибольший общий делитель чисел {a} и {b} = {result}")
main()