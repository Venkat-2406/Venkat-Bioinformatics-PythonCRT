from collections import deque
stack=deque()
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack afer pushing:",stack)
top=stack.pop()
print("popped element:",top)
print("Stack after popping :",stack)
if not stack:
  print("stack is empty")
else:
  print("stack in not empty")
print("Front Element:",stack[0])







