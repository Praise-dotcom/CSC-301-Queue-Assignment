Assignment: Queue Data Structure

Name: ADEOLU PRAISE ADENIKE
Matric Number: 240502012
Course of Study: Computer Science

A Queue works on the FIFO (First-In, First-Out) principle. 
It works just like a line of people waiting — the first person to join the line is the first person to leave.

### Simple Algorithm for Queue Operations

**Initialize Queue:**  
Create an empty list called `queue` and set a maximum size `max_size`.

**isEmpty Operation:**  
Check if `len(queue) == 0`. If yes, the queue is empty.

**isFull Operation:**  
Check if `len(queue) == max_size`. If yes, the queue is full.

**Enqueue Operation (Add item to the rear):**  
1. Check if the queue is full.  
2. If full → print "Queue is Full (Overflow)"  
3. If not full → add the item to the end of the queue.

**Dequeue Operation (Remove item from the front):**  
1. Check if the queue is empty.  
2. If empty → print "Queue is Empty (Underflow)"  
3. If not empty → remove and return the item at index 0.

**Front / Peek Operation:**  
Show the first item (`queue[0]`) without removing it.

**Rear Operation:**  
Show the last item (`queue[-1]`) without removing it.

**Display Operation:**  
Print all items currently in the queue from front to rear.