# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.

# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень

# month_list = [['Зима', 12, 1, 2], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8], ['Осень', 9, 10, 11]]

month_num = int(input('Введите номер месяца (от 1 до 12): '))
if month_num in range(1, 13):
    month_list = [['Зима', 12, 1, 2], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8], ['Осень', 9, 10, 11]]
    for i, el in enumerate(month_list):
        if month_num in el[1:4]:
            print(f'Результат через список: {el[0]}')
            break
    month_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 
        5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето',
        9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
    i = month_dict[month_num]
    print(f'Результат через словарь: {i}')
else:
    print('Введен некорректный номер месяца!')