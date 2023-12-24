# login = str(input("Введите логин: "))
# password = str(input("Введите пароль: "))
# 
# if (login == 'user') and (password == '3830000'):
#     print("Рады вас приветствовать")
# else:
#     print("Неправильно введенный логин или пароль.")
imya = str(input("ваше имя и фамилия: "))
old = int(input("сколько лет: "))
if old <= 17:
    print("ты еще мал")
if imya == "Микордий Пармезанов":
    print("ты в черном списке")
else:
    print("заходи")