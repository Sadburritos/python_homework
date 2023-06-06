price = int(input("стоимость покупки "))
discount =  int(input("размер скидки "))

discond_num = price / 100 * discount
final_price = price - discond_num

print("Конечная стоимость ", "%.2f" % final_price)