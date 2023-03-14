# name = str(input('Введите название: '))
# name_len = len(name)
# if name_len == 0:
#     print('Вы ничего не ввели попробуйте ещё раз')
# elif name_len > 0 and name_len < 4:
#     print(f'Слишком короткое название {name_len}-{name}')
# elif name_len > 3 and name_len < 8:
#     print(f'Идеальное название {name_len}-{name}')
# else:
#     print(f'Слишком длинное название {name_len}-{name}')
n = 0
a = '*__*_'
for i in a:
    if i == "*":
        n += 1

print(n)