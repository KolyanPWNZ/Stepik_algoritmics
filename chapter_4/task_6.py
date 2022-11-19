from math import floor

class MaxHeap:
    def __init__(self):
        self._heap = list()
        self._numberChildNode = 2

    def ExtractMax(self):
        value_out = self._heap[0]
        self._heap[0] = self._heap[-1]
        del self._heap[-1]
        self._siftDown()
        return value_out


    def insert(self, value):
        self._heap.append(value)
        self._siftUp()


    def _siftDown(self):
        i = 0
        status, i_c = self._getIndexChildWithMaxValue(i)

        while status and self._heap[i] < self._heap[i_c]:
            self._swapValuePosition(i, i_c)
            i = i_c
            status, i_c = self._getIndexChildWithMaxValue(i)


    def _siftUp(self):
        i_ne = len(self._heap) - 1
        i_p = self._getParentIndex(i_ne)
        if i_p == i_ne or i_p == -1 or i_ne == -1:
            return
        while self._heap[i_p] < self._heap[i_ne]:
            self._swapValuePosition(i_ne, i_p)
            i_ne = i_p
            i_p = self._getParentIndex(i_ne)

    def _swapValuePosition(self, indx1, indx2):
        self._heap[indx1], self._heap[indx2] = self._heap[indx2], self._heap[indx1]


    def _getParentIndex(self, index):
        if self._numberChildNode:
            pi = (index + 1) // self._numberChildNode - 1
            if pi < 0:
                pi = 0
            return pi
        else:
            return -1


    def _getIndexChildWithMaxValue(self, index_parent):
        index_child1 = (index_parent + 1) * self._numberChildNode - 1
        index_child2 = (index_parent + 1) * self._numberChildNode
        value_child1 = -1
        value_child2 = -1

        if index_child1 < len(self._heap):
            value_child1 = self._heap[index_child1]
        if index_child2 < len(self._heap):
            value_child2 = self._heap[index_child2]

        if value_child1 == -1 and value_child2 == -1:
            return False, -1

        if value_child1 >= value_child2:
            return  True, index_child1
        else:
            return True, index_child2




n = int(input())
my_heap = MaxHeap()
while n > 0:
    n -= 1
    in_data = input().split(' ')
    if len(in_data) > 1:
        if in_data[0] == 'Insert':
            my_heap.insert(int(in_data[1]))
    else: # ExtractMax
        print(my_heap.ExtractMax())
