year = input("год ")
month = input("месяц ")
day = input("число рождения ")

message_template = "%s.%s.%s"

message = message_template % (year, month, day)

print (message)