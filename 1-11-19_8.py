#find: false, python,104,9,10.44,10.33,1002
list1=[1,2,3,4,[5,6,7,8,9],10,11,12,['a','b','z','m',False],[1001,1002,[10.23,10.33,10,33,10.43,['Python','Bgi']]],2003,10.44]
print(list1)
print(list1[8][4])#finding False
print(list1[9][2][5][0]) #finding Python
#104 is not present in the list
print(list1[4][4]) # finding 9
print(list1[-1]) #finding 10.44
print(list1[9][2][-5]) #finding 10.33
print(list1[9][1])#finding 1002
