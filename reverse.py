a=int(input("enter a no"))
count=0
rev=0
while(a):
    n=a%10
    rev=(rev*10)+n
    a//=10
print(rev)
