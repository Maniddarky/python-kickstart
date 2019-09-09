a=int(input("enter a no"))
count=0
while(a):
    n=a%10
    count+=n
    a//=10
print(count)
