usd = float(input("Введите количество USD: "))
currency = input("Выберите валюту для конвертации (EUR, UAN, AZN): ")

if currency == "EUR":
    converted_amount = usd * 0.93
    print("Сумма в EUR:", converted_amount)
elif currency == "UAN":                                                                     #Это же юань?
    converted_amount = usd * 7,13
    print("Сумма в UAN:", converted_amount)
elif currency == "AZN":
    converted_amount = usd * 1,7
    print("Сумма в AZN:", converted_amount)
else:
    print("Выбранная валюта недоступна")
