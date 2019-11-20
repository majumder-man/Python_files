d=int(input("Total Distance: "))
m1=int(input("Maximum Leaping distance: "))
m2=int(input("Minimum Leaping distance: "))
#maximum leaps
if d%m2==0:
    n1=d//m2
    print("Maximum leaps: ",n1)
else:
    print("Maximum Leaps : Not Applicable")
#minimum leaps
if d%m1==0:
    n2=d//m1
    print("Minimum leaps: ",n2)
else:
    print("Minimum Leaps : Not Applicable")
