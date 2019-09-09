t=int(input())
while(t):
    sum=0
    ne=int(input())
    nc=int(input())
    e=list()
    for i in range(ne):
        e.append(int(input()))
        sum+=e[i]
    if sum > nc:
        print("No")
    else:
        print("Yes")
    t=t-1
