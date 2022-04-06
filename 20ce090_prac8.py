from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def is_empty(self):
        return len(self.stack)==0

    def size(self,val):
        return len(self.stack)


s=Stack()
s.push('nobita')
s.push('maitrey')
s.push('aditya')
s.push('utkarsh')
s.push('harsh')
s.push('manan')

s.pop()

print(s.is_empty())
print(type(s.stack))
print(s.stack)