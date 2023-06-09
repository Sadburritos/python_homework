purchase = float(input("Введите сумму покупки: "))

discount = 0

if purchase >= 200 and purchase < 300:
# VN: ещё вариант:  200 <= purchase < 300
    discount = 0.03
elif purchase >= 300 and purchase < 500:
    discount = 0.05
elif purchase >= 500:
    discount = 0.07

discount_amount = purchase - (purchase * discount)
print("Сумма к оплате co скидкой: ", discount)
