#declaration of dictionaries
dict={101:'python',102:'java',103:'HTML'}
print(type(dict))
print(dict)

dict={1:'venky',2:'pinky',3:'donkey'}
print(dict)

stu={101:'rahul',102:'raj',103:'sonam'}
fees={'rahul':2000,'raj':3000,'sonam':8000}
print(stu[101])
print(fees['sonam'])

stu={101:'rahul',102:'raj',103:'sonam'}
print(stu)
#modification
stu[103]='venkatesh'
print(stu)

jobrole={101:'Full stack developer',102:'Developer',103:'tester'}
print(jobrole)
jobrole[104]='Analyst'
jobrole[105]='tester'
jobrole[106]='soc analyst'
print(jobrole)
#functions
jobrole.pop(101)        #pop function()
print(jobrole)
del jobrole[105]
print(jobrole)
print(len(jobrole))     # len function()
print(jobrole.keys())   # key method() returns all the keys
print(jobrole.values()) # value method returns all the values
print(jobrole.items())
b=jobrole.copy()
print(b)

dict1={1:'a',2:'b',3:'c'}
print(dict)
dict2={4:'d',5:'e'}
print(dict1)
dict1.update(dict2)
print(dict2)