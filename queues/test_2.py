from circular_queue import CircularQueue

queue = CircularQueue(5)

# Enqueue elements ------------------------------------------------------------
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
queue.enqueue('D')
queue.enqueue('E')

print(" 1) Enqueue  | ", queue)

# Dequeue elements ------------------------------------------------------------
assert queue.dequeue() == 'A'
assert queue.dequeue() == 'B'

print(" 2) Dequeue  | ", queue)

# Peek elements ---------------------------------------------------------------
assert queue.peek() == 'C'

print(" 3) Peek     | ", queue)

# Search elements -------------------------------------------------------------
index = queue.search('C')
if index != -1:
    print(f" 4) Search   | {queue} | {queue.elements[index]} is in index {index}")
else:
    print(" 4) Search   | ", queue)

index = queue.search('E')
if index != -1:
    print(f"    Search   | {queue} | {queue.elements[index]} is in index {index}")
else:
    print("    Search   | ", queue)

index = queue.search('A')
if index != -1:
    print(f"    Search   | {queue} | {queue.elements[index]} is in index {index}")
# else:
#     print("    Search   | ", queue)

