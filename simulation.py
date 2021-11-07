"""
A simple use of Queue and Stack.
"""

from queue import Queue
from stack import Stack

# Set 2 stacks and 1 queue with max size of 10
s1 = Stack(10)
s2 = Stack(10)
q = Queue(10)

lst = [5, 7, -4, 1]

for i in lst:
    s1.push(i)

print(repr(s1))

# Using to stacks to simulate a queue.
while True:
    if s1.is_empty():
        break

    s2.push(s1.pop())

print(repr(s1))
print(repr(s2))
print(repr(q))

while True:
    if s2.is_empty():
        break

    print(s2.pop(), end='')

while True:
    if q.is_empty():
        break

    print(q.pop(), end='')
