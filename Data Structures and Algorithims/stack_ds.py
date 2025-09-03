#STACK
#LIFO - Last In First Out
#python doesn't have stack by default, we can use Lists for similar behaviour however its slower, since it has to shift all components after
stack = []

# Push (add an element)
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)  # Output: [10, 20, 30]

# Pop (remove the top element)
top = stack.pop()
print(top)    # Output: 30
print(stack)  # Output: [10, 20]

# Peek (look at the top without removing)
top = stack[-1]
print(top)    # Output: 20

#to use native stack (its a double linked list but its suposed to be faster)
from collections import deque

stack = deque()

stack.append(10)
stack.append(20)

print(stack)  # Output: deque([10, 20])

top = stack.pop()
print(top)    # Output: 20
print(stack)  # Output: deque([10])
