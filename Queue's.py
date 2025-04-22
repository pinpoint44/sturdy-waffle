class Queue:
    def __init__(self):
        self.queue = []
   
    def enqueue(self, element):
        """Add an element to the end of the queue"""
        self.queue.append(element)
    
    def dequeue(self):
        """Remove and return the first element of the queue"""
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.queue) == 0
    
    def __str__(self):
        """String representation of the queue"""
        return str(self.queue)

def main():
    myQueue = Queue()
    
    # Enqueue elements
    for i in range(1, 4):
        element = input(f"Enter item {i}: ")
        myQueue.enqueue(element)
    
    print("Current Queue:", myQueue)
    
    # Dequeue elements
    while not myQueue.is_empty():
        input("Press Enter to dequeue an item...")
        dequeued = myQueue.dequeue()
        print("Dequeued:", dequeued)
        print("Updated Queue:", myQueue)
    
    print("Queue is now empty")

if __name__ == "__main__":
    main()

#FERNANDEZ, CLINT ALLAN C.
#IT1R7

#Array-Based Queue
#Implementation: Use a fixed-size array with front and rear pointers.
#Space Complexity: O(n), where n is the size of the array.
#Pros and Cons: Simple to implement but It wastes space unless circular buffer is used

