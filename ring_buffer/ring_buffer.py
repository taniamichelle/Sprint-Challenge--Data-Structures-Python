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
        if self.storage.length < self.capacity:   # if there's still space in our DLL:
            self.storage.add_to_tail(item)  # add item to the tail of DLL
            self.current = self.storage.tail  # set current node to tail
            print('first if current: ', self.current)
        if self.storage.length-1 == self.capacity:  # if our DLL is at capacity:
            # print('second if current', self.current)
            # self.current.value = item
            # print(f" 'curr val:' {self.current.value}")
            if self.current == self.storage.tail:
                self.current = self.storage.head
            # print('first nested if current', self.current)
            else:
                # if self.current != self.storage.tail:
                self.current = self.current.next
            print('else current: ', self.current)

    def get(self):
        '''
        Returns all of the elements in the buffer in a list in their given order. It should 
        not return any `None` values in the list even if they are present in the ring buffer.
        '''
        list_buffer_contents = []  # initialize empty list
        # print('empty list: ', list_buffer_contents)
        self.current = self.storage.head  # initialize current as the head of the buffer
        # print('current in', self.current)
        if self.current is None:
            self.current = self.storage.head
            print('updated current in get: ', self.current)
        while self.current is not None:  # while the element we're on is NOT none:
            # append the value to the empty list
            list_buffer_contents.append(self.current.value)
            self.current = self.current.next  # move current pointer to next item in DLL
            print('list: ', list_buffer_contents, 'current: ', self.current)
        return list_buffer_contents  # return list and exit while loop


# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass


buffer = RingBuffer(3)
buffer.append('A')
buffer.append('B')
buffer.append('C')
print('buffer: ', buffer.get())

buffer.append('D')
print('new buffer: ', buffer.get())
# print('storage', self.buffer.storage)
