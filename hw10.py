import os
import pickle

def input_scores():
    s=[]
    i=1
    while True:
        n=int(input(f'#{i}? '))
        if n<0:
            break
        s.append(n)
        i+=1
    return s

def get_average(s):
    total=0
    for n in s:
        total+=n
    return total/len(s)

def show_scores(s):
    print('개인점수:', end=' ')
    for n in s:
        print(n,end=' ')

    print()

filename='scores.bin'

if os.path.exists(filename):
    print('[파일 읽기]')
    with open(filename,'rb') as file:
        scores=pickle.load(file)
else:
    print('[점수 입력]')
    scores=input_scores()
    with open(filename,'wb') as file:
        pickle.dump(scores,file)

print()
print('[점수 출력]')
show_scores(scores)
avg=get_average(scores)
print(f'평균: {avg:.1f}')
