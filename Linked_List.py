class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            runner = self.head
            while runner.next:
                runner = runner.next

            runner.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
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
        else:
            count = 0
            runner = self.head
            while runner:
                if count == index - 1:
                    runner.next = runner.next.next
                    break

                runner = runner.next
                count += 1

    def insert_at(self, index, data):
        self.__check_index(index)

        if index == 0:
            self.insert_at_beginning(self, data)
        else:
            count = 0
            runner = self.head
            while runner:
                if count == index - 1:
                    node = Node(data, runner.next)
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

    def print(self):
        if self.head is None:
            print('Linked List is empty')
        else:
            runner = self.head
            llstr = ''

            while runner:
                llstr += str(runner.data) + '-->'
                runner = runner.next

            print(llstr + 'None')



ll = LinkedList()
ll.insert_after_value("mango", "apple")
ll.print()
ll.insert_values(["banana", "mango", "grapes", "orange"])
ll.print()
ll.insert_after_value("mango", "apple")  # insert apple after mango
ll.insert_after_value("grapes", "tomato")  # insert apple after mango
ll.print()
ll.remove_by_value("orange")  # remove orange from linked list
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()