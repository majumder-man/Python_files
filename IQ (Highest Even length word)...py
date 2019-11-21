m=input()
dict1={}
m=m.split()
for i in m:
    d=len(i)
    if d%2==0:
        dict2={i:d}
        dict1.update(dict2)
maximum=max(dict1,key=dict1.get)
print(maximum)
