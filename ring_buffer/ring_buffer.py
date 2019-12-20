from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        # capaacity refers to "size" of structure; this is fixed so newest data will overwrite oldest
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()  # import DLL

    # def _repr__(self):
    #     return(f'capacity: {self.capacity}')

    def __str__(self):
        return self.capacity

    def append(self, item):
        '''
        Adds elements to the buffer.
        '''
        if self.storage.length == self.capacity:
            self.storage.remove_from_tail()
        else:
            self.storage.add_to_head(item)

    def get(self):
        '''
        Returns all of the elements in the buffer in a list in their given order. It should 
        not return any `None` values in the list even if they are present in the ring buffer.
        '''
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        # list_buffer_contents.append(element)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


buffer = RingBuffer(5)
buffer.append('2')
buffer.append('5')
buffer.append('t')
buffer.append('m')
print('buffer: ', buffer)
