import numpy as np
import random
# password = 'python123'
#
# while True:
#     user_input = input("Введите пароль: ")
#     check = str(user_input)
#     if check == password:
#         print("Пароль введён верно ")
#         break
#     else:
#         print("Неправильный пароль! \n")
#         continue

# Создаю словарь

first_men = {
    'First name': 'Ivan',
    'Last name': 'Petrov',
    'City': 'Arhangelsk',
    'Age': 29,
}

# Добавляю интересы
# first_men['Interests'] = 'He likes go for a walk, visiting theatres, museums, listening hard rock music'
# print(first_men['First name'] + ". His interests: " + first_men['Interests'])
#
# first_men['City'] = 'Moscow'
# del first_men['Interests']
# print(first_men)

# for k, v in first_men.items():
#     print("\n" + k + ":")
#     print(v)
#
# print('\n')

# for name in first_men.keys():
#     print(name)
#
# if 'Interests' not in first_men:
#     print("This word doesn't exist!")
#
# print("\n")
#
# for name in sorted(first_men.keys()):
#     print(name)


# for name in sorted(first_men.values()):
#     print(name)

d_ar = {'a': None,
        'b': 1,
        'c': 2,
        'd': None,
        'e': 3}

for i in d_ar.copy():
    # print(i)
    if d_ar[i] is None:
        d_ar.pop(i)
print(d_ar)

print(d_ar["b"])


def to_dict(lst):
    arr = np.random.sample(lst)
    dicti = {}
    for i in arr:
        dicti[i] = i
    return dicti


print(to_dict(4))


def to_dict_1(*lst):
    return {element: element for element in lst}


print(to_dict_1(1, 2, 3, 4))
print(to_dict_1('grey', (2, 17), 3.11, -4))
