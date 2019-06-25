a1=1
i=9
a0=0
while 1 :
    if i>=1:
        a0=2*(a1+1)
        a1=a0
        i=i-1
        print(a0)
    else:
        break


print(a0)
