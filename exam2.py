tot = 0

# 1~100 사이의 5의 배수의 합 구하기
for i in range(1, 101) :
    if i%5 == 0: tot += i
    
print("tot =", tot)    

