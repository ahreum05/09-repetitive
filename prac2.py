tot = 0
for i in range(1, 101):  
    tot += i    
    if i%10 ==0 :  
        print('%2d ~ %3d = %3d' %(i-9, i, tot))
        tot = 0
        
