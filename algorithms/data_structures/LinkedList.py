class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.next=self.head
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def search(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                print("found it")
                return current
            current = current.next
        return None

    def delete(self, data ):
        current = self.head
        while current != None : 
            #remove first one
            if current.data == data :
                tmp = current .next
                self.head  = tmp
            #remove other places
            elif current.next != None and current.next.data == data :
                current.next = current.next.next
            current = current.next

    def print(self):
        current = self.head
        while current != None:
            print(current.data,end="-")
            current = current.next
        print(" ")
        
#example of how to use it
# lk = LinkedList()
# lk.insert("a")
# lk.insert("b")
# lk.insert("c")
# lk.print()
# lk.search("a")
# lk.delete("c")
# lk.print()
# print(lk.size())

