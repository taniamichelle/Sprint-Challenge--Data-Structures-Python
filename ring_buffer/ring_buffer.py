from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        # capaacity refers to "size" of structure; this is fixed so newest data will overwrite oldest
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()  # import DLL

    # def __repr__(self):
    #     return(f'self.capacity: {self.capacity}, current: {self.current}')

    def __str__(self):
        return(f'self.capacity: {self.capacity}, current: {self.current}')

    def append(self, item):
        '''
        Adds elements to the buffer.
        '''
        if self.storage.length >= self.capacity:  # if our DLL is at capacity:
            self.storage.remove_from_tail()  # remove tail item
        elif self.storage.length < self.capacity:   # if there's still space in our DLL:
            self.storage.add_to_head(item)  # add item to the head of DLL

    def get(self):
        '''
        Returns all of the elements in the buffer in a list in their given order. It should 
        not return any `None` values in the list even if they are present in the ring buffer.
        '''
        # Note:  This is the only [] allowed
        list_buffer_contents = []  # initialize empty list
        self.current = self.storage.tail  # initialize current as the head of the buffer
        while self.current is not None:  # while the element we're on is NOT none:
            # append the value to the empty list
            list_buffer_contents.append(self.current)
            self.current = self.current.prev  # move current pointer to next item in DLL
        return list_buffer_contents  # return list and exit while loop

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass


buffer = RingBuffer(5)
buffer.append('2')
buffer.append('4')
buffer.append('t')
buffer.append('m')
print('buffer: ', buffer.get())
# print('storage', self.buffer.storage)
