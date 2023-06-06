year = input("год ")
month = input("месяц ")
day = input("число рождения ")

message_template = "%s.%s.%s"

message = message_template % (year, month, day)

print (message)

'''
год 2010
месяц 3
число рождения 3
2010.3.3

Должно быть: 03.03.2010
т.е. формат  дд.мм.гггг
'''