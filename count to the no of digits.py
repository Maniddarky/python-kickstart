a=int(input("enter a no"))
count=0
while(a):
    n=a%10
    count+=1
    a//=10
print(count)
