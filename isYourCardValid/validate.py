def fun(n):
    n=2*n
    n=n//10+n%10
    return n
    
num=list(map(int,[i for i in input("Enter card number: ")]))
even=[num[i] for i in range(0,len(num),2)]
even1=[]
for i in even:
    if (2*i)>9:
        even1.append(fun(i))
    else:
        even1.append(2*i)
t=[]
for i in zip(even1,num[1:len(num):2]):
    t.append(int(i[0]))
    t.append(int(i[1]))
if sum(t)%10==0:
    print("Card is Valid")
else:
    print("Card Not Valid")
    

        