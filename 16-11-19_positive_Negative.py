poslist=[]
neglist=[]
list1=[10,11,13,-11,-3,4]
for i in list1:
    if i >0:
        poslist.append(i)
       
    elif i<0:
        neglist.append(i)
        
print(poslist)
print(neglist)
