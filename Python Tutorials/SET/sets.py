set={10,20,30,40,50,60}
print(set)
print(type(set))
print(10 in set)
set.add(60)
set.add(70)
set.add(80)         #add element into the list
print(set)
set1={80,90,100}
set.update(set1)
print(set)
set.remove(100)     # remove the wanted element from the list
print(set)
set.pop()       #no need of argument tp give by default it remove the first element
print(set)
set.discard(90)       #remove particular item of list
print(set)
set.clear()     #remove all the elements
print(set)

