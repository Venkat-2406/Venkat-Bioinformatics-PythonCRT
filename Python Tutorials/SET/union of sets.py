set={1,2,3}
set1={3,4,5}
print(set|set1) #union---removing duplicates

print(set&set1) #intersection----return the common elements

set={1,2,3}   #difference---items only present in 1st set
set1={2,3,4}
print(set-set1)
print(set.intersection(set1))
print(set.union(set1))
print(set.difference(set1))

set1={4,6,8}
set2={2,4,6,8,10,12,14,16}
print(set1.issubset(set2))  #set1 elements should be present in set2
print(set2.issuperset(set1)) #set2 contain all elements of set1 including other elements