def degree_of_number(a, b):
    if (b == 1):
        return a
    if (b == 0):
        return (1)
    if (b != 1):
        return (a * degree_of_number(a, b - 1))


print(f"Результат:", degree_of_number(
    a=int(input("Введите число: ")), b=int(input("Cтепень числа: "))))
