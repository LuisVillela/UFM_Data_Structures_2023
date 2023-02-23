class CircularQueue:
    '''
    Circular Queue object, array-based implementation.

    Args:
        size (int): size of underlying array

    Attributes:
        elements (List): array of elements
        front (int): pointer at front
        rear (int): pointer at rear
        max (int): maximum amount of elements in queue
        count (int): current amount of elements in queue
    '''

    def __init__(self, size: int) -> None:
        self.elements = [None] * size
        self.front = -1
        self.rear = -1
        self.max = size
        self.count = 0


    def __repr__(self) -> str:
        return 'Current queue: {} | Front: {} | Rear: {}'.format(self.elements, self.front, self.rear)

#ENQUEUE --------------------------------------------------------------------

    def enqueue(self, value: str) -> None:
        '''
        Inserts element into the queue.

        Args:
            value (str): value to be enqueued

        Returns:
            None
        '''

        if self.count == self.max:
            print("Queue Overflow...")
            return None
        
        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max

        self.elements[self.rear] = value
        self.count += 1

#DEQUEUE --------------------------------------------------------------------

    def dequeue(self) -> str:
        '''
        Deletes element from the queue.

        Args:
            None

        Returns:
            value (str): value of element dequeued
        '''

        if self.count == 0:
            print('Queue Underflow...')
            return None

        value = self.elements[self.front]
        self.elements[self.front] = None # (Optional)
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max
        self.count -= 1
        return value

#PEEK --------------------------------------------------------------------

    def peek(self) -> str:
        '''
        Returns the element at the front of the queue without removing it.

        Args:
            None

        Returns:
            value (str): value of element at front of queue
        '''
        if self.count == 0:
            print('Queue is empty...')
            return None

            print(f"Peeking at element: {self.elements[self.front]}")
        return self.elements[self.front]

#SEARCH --------------------------------------------------------------------
