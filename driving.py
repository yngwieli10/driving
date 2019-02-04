country = input('請問你是哪國人:')
age = int(input('您的年齡:'))
if country == '台灣':
    if age >= 18:
        print('可以考駕照')
    else:
        print('無法考駕照')