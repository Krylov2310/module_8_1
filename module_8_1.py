print('\033[30m\033[47mДомашнее задание по теме "Try и Except".\033[0m')
print('\033[30m\033[47mЗадание "Программистам всё можно":\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()


def add_everything_up(a, b):
    try:
        a + b
    except TypeError:
        a = str(a)
        b = str(b)
        return a + b
    else:
        a = float(a)
        b = float(b)
        return round(a + b, 3)


# Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print()
print(thanks)
