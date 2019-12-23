'''
List:[]
append
index
count
remove
pop
insert
'''
chairs=[250,780,120,400,800]
#add
chairs.append(920);chairs.append(650);chairs.append(100);chairs.append(560)
print(chairs)
chairs.insert(2,350)
print(chairs)
chairs.insert(12,350)# but it still stores at the end
print(chairs)
print(chairs.count(350))
print(chairs.index(350))
print(chairs[10])

chairs.pop()
chairs.remove(100)
del chairs[5]
print(chairs)

chairs[6]=chairs[6]+200
print(chairs)
chairs.sort()
chairs.reverse()
print(chairs)
