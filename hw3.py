def get_fixed_price(disrate,disprice):
    price=disprice/(1-disrate/100)
    return price

disrate=int(input('할인율은? '))
disprice_a=int(input('A 상품의 할인된 가격은?'))
disprice_b=int(input('B 상품의 할인된 가격은?'))
price_a=get_fixed_price(disrate,disprice_a)
price_b=get_fixed_price(disrate,disprice_b)
print('A 상품의 정가는',price_a)
print('B 상품의 정가는',price_b)
