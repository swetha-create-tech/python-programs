n=int(input("enter n: "))
temp=n
sum=0
while(n>0):
    a=n%10
    sum=sum*10+a
    n//=10
if(temp==sum):
    print("palindrome")
else:
    print("Not Palindrome")
