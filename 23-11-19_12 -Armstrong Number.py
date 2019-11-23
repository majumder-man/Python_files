m=int(input("Enter the number: "))
n=list(str(m))
o=[]
for i in n:
    d=int(i)
    o.append(d**3)
if m==sum(o):
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")
