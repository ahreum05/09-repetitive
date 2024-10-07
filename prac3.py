while True:
    dan = int(input('몇 단을 출력할지 입력하시오 : '))
    for i in range(1, 10) :   # 1~9
        print('%d * %d = %2d' %(dan, i, dan*i))
        
    print()
    ans = input('선택하시오(y:계속) : ')
    print()
    if ans == 'y' : continue
    else : 
        print('종료')
        break