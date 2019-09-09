n=int(input())
temp=n
order=1
while(temp):
    order=order*10
    temp//=10
order=order//10
#print(order)
last=n%10
first=n//order
#print(first)
#print(last)
n=n%order
n=n-last
n=n+first
n=(last*order)+n
print(n)


#a-=last

#a+=first

#n=(last*10)+a
#print(n)

