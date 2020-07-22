N = int(input())
c=0
r=N
while True :
    s=int(r/10)+r%10
    r=10*(r%10)+s%10
    c=c+1
    if r==N :
        break
print(c)
