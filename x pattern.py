g="geeks"
n=len(g)
i=0
k=n*2-1
for i in range(n):
    j=0
    for k in range(i):
        if i==j or i+j==k:
            print(g[i],end='')
    print("\n")
