jango = 0    # 잔고 저장

while True :
    print()
    print('1.예금 2.출금 3.잔고 4.종료')
    num = int(input('번호 선택 : '))
    
    if num==1 :
        jango += int(input('예금액 : '))        
    elif num==2 :
        money = int(input('출금액 : '))  
        if jango - money >= 0 :
            jango -= money
        else : print("잔고가 부족합니다.")
    elif num==3 :
        print('%s원' %jango)        
    elif num==4 : 
        print('프로그램을 종료합니다.')
        break