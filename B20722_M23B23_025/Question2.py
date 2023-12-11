#create a class StudentQueue
class StudentQueue:
#create a function to store the data
    def __init__(self):
        self.data = []
#create a function enqueue to add data in the queue
    def enqueue(self, data):
        self.data.append(data)
#create a function denqueue to remove data in the queue
    def dequeue(self):
        if len(self.data) > 0:
            return self.data.pop(0)
#create a function queue_empty to check if the queue is empty
    def queue_empty(self):
        return len(self.data) == 0

queue = StudentQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.data)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(len(queue.data))






         