# 3. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# Пример:
# Иван Иванов 1846 года рождения, проживает в городе Москва,
# email: jackie@gmail.com, телефон: 01005321456

def user_data(name, surname, year_of_birth, city_of_residence, email, phone_namber):
    print(f"{name} {surname} {year_of_birth} года рождения, проживает в городе {city_of_residence}, "
          f"email: {email}, телефон: {phone_namber}")
    
user_data(name = 'Иван', surname = 'Иванов', year_of_birth = '1846', city_of_residence = 'Москва',
          email = 'jackie@gmail.com', phone_namber = '01005321456')