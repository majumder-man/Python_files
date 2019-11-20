d=int(input("Total Distance: "))
m1=int(input("Maximum Leaping distance: "))
m2=int(input("Minimum Leaping distance: "))
#maximum leaps
if d%m2==0:
    n1=(d//m2)
else:
    n1=(d//m2)+1
print("Maximum leaps: ",n1)
#minimum leaps
if d%m1==0:
    n2=d//m1
else:
    n2=(d//m1)+1
print("Minimum leaps: ",n2)
