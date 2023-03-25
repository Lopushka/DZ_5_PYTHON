def summer(a, b):
    if a == 0:
        return b
    return summer(a-1, b+1)


print(f'Результат: ', summer(a=int(input('Введите первое неотрицательное число: ')),
      b=int(input('Введите Второе неотрицательное число: '))))
