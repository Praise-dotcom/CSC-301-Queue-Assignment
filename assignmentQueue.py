# Name: ADEOLU PRAISE ADENIKE
# Matric Number: 240502012
# Course of Study: Computer Science
# CSC301 - Data Structures and Algorithms
# Assignment: Queue Implementation

# Queue follows FIFO (First-In, First-Out)

queue = []
max_size = 5

def is_empty():
    return len(queue) == 0

def is_full():
    return len(queue) == max_size

def enqueue(item):
    if is_full():
        print("Queue is Full! Cannot add:", item)
    else:
        queue.append(item)
        print(item, "has been added to the queue.")

def dequeue():
    if is_empty():
        print("Queue is Empty! Nothing to remove.")
    else:
        removed = queue.pop(0)
        print(removed, "has been removed from the front of the queue.")

def front():
    if is_empty():
        print("Queue is Empty!")
    else:
        print("Front element is:", queue[0])

def rear():
    if is_empty():
        print("Queue is Empty!")
    else:
        print("Rear element is:", queue[-1])

def size():
    print("Current queue size is:", len(queue))

def display():
    if is_empty():
        print("Queue is currently empty: []")
    else:
        print("Current Queue (Front to Rear):", queue)


# ========== Testing ==========
print("--- Starting Queue Operations ---")
print("Is the queue empty right now?", is_empty())

print("\n--- Adding items (Enqueue) ---")
enqueue("Student 1")
enqueue("Student 2")
enqueue("Student 3")
enqueue("Student 4")
enqueue("Student 5")
enqueue("Student 6")

print("\n--- Checking Queue Details ---")
display()
front()
rear()
size()
print("Is the queue full?", is_full())

print("\n--- Removing items (Dequeue) ---")
dequeue()
dequeue()

print("\n--- Final Queue State ---")
display()
front()
rear()
size()