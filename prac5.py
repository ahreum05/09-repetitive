for i in range(1, 6):               # 층
    print(' ' * (5 - i), end='')    # 공백문자
    for j in range(2 * i - 1):      # 별문자
        print('*', end='') 
    print()
    
print('-' * 20)

for i in range(1, 6):               # 층
    for j in range(5-i) :           # 공백문자
        print(' ', end='')
    for j in range(2 * i - 1):      # 별문자
        print('*', end='') 
    print()
