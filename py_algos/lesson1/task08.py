"""
Определить, является ли год, который ввел пользователь, високосным или не високосным.
"""
# написал в одну строчку, чтобы избежать дублирования строк вывода
year = int(input('Введите год: '))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Год високосный')
else:
    print('Год не високосный')
