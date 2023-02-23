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
