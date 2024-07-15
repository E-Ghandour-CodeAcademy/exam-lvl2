# Implement a Circular Queue
# Objective: Design a class `CircularQueue` that implements a circular queue with fixed size using a list.
# Parameters:
# - size: An integer representing the maximum number of elements the queue can hold.
# Returns:
# - None; methods handle the queue operations.
# Details:
# - Methods include `enqueue`, `dequeue`, `peek`, and `is_empty`.
# - `enqueue` should add an element to the queue if not full; otherwise, raise an exception.
# - `dequeue` should remove and return the element from the front if not empty; otherwise, raise an exception.
# - `peek` returns the front element without removing it.
# - `is_empty` checks whether the queue is empty.
# - Handle overflow and underflow appropriately with exceptions.

class CircularQueue:
    pass

# Examples:
# cq = CircularQueue(3)
# cq.enqueue(1)
# cq.enqueue(2)
# print(cq.peek())  # Expected: 1
# print(cq.dequeue())  # Expected: 1
# print(cq.is_empty())  # Expected: False
# cq.enqueue(3)
# cq.enqueue(4)
# print(cq.dequeue())  # Expected: 2
# print(cq.dequeue())  # Expected: 3
