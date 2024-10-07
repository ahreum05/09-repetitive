for i in range(2, 10) :     # 2~9단
    for j in range(1, 10) : # 1~9
        print("%d*%d=%2d" %(i, j, i*j), end="  ")
    print()

print('-' * 20)

for j in range(1, 10) : # 1~9
    for i in range(2, 10) :     # 2~9단
        print("%d*%d=%2d" %(i, j, i*j), end="  ")
    print()