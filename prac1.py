num = int(input('1~100사이의 배수를 구할 숫자 입력 : '))
cnt=0   # 카운트 저장

for i in range(1, 101):
    if i%num == 0 : 
        print(i, end=' ') 
        cnt += 1
    
print()
print('1~100 사이의 7의 배수 개수 = %s' %cnt)