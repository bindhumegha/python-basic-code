n=int(input("enter the value"))
m=n
c=0
s=0
a=0
while m!=0:
    c=c+1
    m=m//10
print(c)
while n!=0:
    r=n%10
    s=r**c
    a=a+s
    n=n//10
print(a)