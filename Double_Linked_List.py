class Node:

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)
        if self.head:
            self.head.prev = node
        self.head = node

        if self.tail is None:
            self.tail = self.head

    def insert_at_end(self, data):
        node = Node(data, None, self.tail)
        if self.tail:
            self.tail.next = node
        self.tail = node

        if self.head is None:
            self.head = self.tail

    def insert_values(self, data_list):
        self.head = None
        self.tail = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        runner = self.head
        while runner:
            count += 1
            runner = runner.next

        return count

    def __check_index(self, index):
        if index < 0 or index >= self.get_length():
            raise IndexError('Invalid index')

    def remove_at(self, index):
        self.__check_index(index)

        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
        else:
            count = 0
            runner = self.head
            while runner:
                if count == index:
                    runner.prev.next = runner.next
                    if runner.next:
                        runner.next.prev = runner.prev
                    else:
                        self.tail = runner.prev
                    break

                runner = runner.next
                count += 1

    def insert_at(self, index, data):
        self.__check_index(index)
        runner = self.head

        if index == 0:
            self.insert_at_beginning(data)
        else:
            count = 0
            while runner:
                if count == index - 1:
                    node = Node(data, runner.next, runner)
                    if node.next:
                        node.next.prev = node
                    runner.next = node
                    break

                runner = runner.next
                count += 1

    def insert_after_value(self, data_after, data_to_insert):
        runner = self.head
        count = 0
        while runner:
            if runner.data == data_after:
                self.insert_at(count + 1, data_to_insert)
                break

            count += 1
            runner = runner.next

    def remove_by_value(self, data):
        runner = self.head
        count = 0
        while runner:
            if runner.data == data:
                self.remove_at(count)
                break

            count += 1
            runner = runner.next

        # runner = self.head
        # if self.head and runner.data == data:
        #     self.head = self.head.next
        # else:
        #     while runner.next:
        #         if runner.next.data == data:
        #             runner.next = runner.next.next
        #             break
        #
        #         runner = runner.next

    def print_forward(self):
        self.print('next')

    def print_backward(self):
        self.print('prev')

    def print(self, attrName='next'):
        if self.head is None:
            print('Linked List is empty')
        else:
            runner = self.tail if attrName == 'prev' else self.head
            llstr = ''

            while runner:
                llstr += '<--' + str(runner.data) + '-->'
                runner = runner.__dict__[attrName]

            print('None' + llstr + 'None')



ll = DoubleLinkedList()
ll.insert_at_beginning(3)
ll.insert_at_beginning(3)
ll.insert_at_beginning(3)
ll.print_backward()
ll.insert_at(0, 10)
ll.print_forward()
ll.insert_after_value(10,7)
ll.print_forward()
ll.remove_by_value(3)
ll.print_forward()
ll.print_backward()
ll.insert_values([3,4,5,3])
ll.remove_at(3)
ll.print_backward()
ll.print_forward()
print(ll.get_length())