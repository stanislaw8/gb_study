"""
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""


def rec_sum(x):
    if x == 1:
        return x
    else:
        return x + rec_sum(x - 1)


n = int(input('введите количество элементов для проверки: n='))
if rec_sum(n) == n * (n + 1)/2:
    print(f'{rec_sum(n)=}, {n * (n + 1)/2=} : равенство подтверждено')
else:
    print('равенство не выполняется')