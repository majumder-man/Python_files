n=int(input("Enter the Number: "))
m=[]
for i in range(n):
    d=n%(i+1)
    m.append(d)
if n==1:
    print("What's wrong with you? It is 1!!!!")
elif n==2:
    print("Seriously? You wanna check whether 2 is prime number or not?")
elif n%n==0 and m.count(0)==2:
    print("It is a prime Number")
else:
    print("It is not a prime Number")
