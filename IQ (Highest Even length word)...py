m=input()
m=m.split()
for i in m:
    d=len(i)
    if d%2==0:
        dict1={d:i}
d=max(dict1.keys())
print(dict1[d])
