#program to take the length of queue from user add elements using enque method and print the
# elements present in the queue and remove the elements one by one from queue and check whether 
# the queue is empty or not and print the front peek and rare peek
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty."

    def is_empty(self):
        return len(self.queue) == 0

    def front_peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty."

    def rear_peek(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            return "Queue is empty."

    def display(self):
        return self.queue
queue=Queue()
n = int(input("Enter number of elements to enqueue: "))
for i in range(n):
    item = input(f"Enter element {i+1}: ")
    queue.enqueue(item)
queue.dequeue()
queue.is_empty
queue.front_peek()
queue.rear_peek()
queue.display()
