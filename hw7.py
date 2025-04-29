shopping_bag={}
while True:
    item=input('상품명? ')
    if item=='':
        break
    amount=int(input('수량은? '))
    print('장바구니에',item,amount,'개가 담겼습니다.')
    print()
    shopping_bag[item]=amount
 
print()
print('>>> 장바구니 보기:', shopping_bag)
print()
print("[검색]")
find=input('장바구니에서 확인하고자 하는 상품은?')
amt=shopping_bag.get(find)
print(f'{find}은(는) {amt}개 담겨 있습니다.')