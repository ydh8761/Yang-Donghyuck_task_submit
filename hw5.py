def read_single_digit(digit):
    n=['영','일','이','삼','사','오','육','칠','팔','구']
    return n[int(digit)]

def read_number(num):
    return read_single_digit(num[0])+' '+read_single_digit(num[1])+' '+read_single_digit(num[2])

num=input('세 자리 정수 입력: ')
print(read_number(num))