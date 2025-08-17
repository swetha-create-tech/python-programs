num=int(input("enter num: "))
for i in range(2,num):
    if num%i==0:
        print("Not prime")
        break
    else:
        print("Prime")
        break