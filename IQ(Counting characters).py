m=input()
list1=list(m)
list2=list(set(list1))
for i in list2:
    d=list1.count(i)
    print(i,d)
