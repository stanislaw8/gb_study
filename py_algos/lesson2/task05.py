"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32
и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ"
в каждой строке.
"""


def show(x, y):
    for i in range(x, x + 10):
        if i > y:
            return
        print(f'{i} - {chr(i)}', end='\t')
    print('\n')
    show((x+10), y)


first = 32
last = 127
show(first, last)
