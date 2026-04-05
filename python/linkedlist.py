
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Singlelinkedlist:
    def __init__(self):
        self.head = None

    #判断链表是否为空
    def is_empty(self):
        return self.head is None

if __name__ == '__main__':
    linkedlist = Singlelinkedlist()
    linkedlist.head = Node(5)
    linkedlist.head.next = Node(6)
    print(linkedlist.head.value)
    print(linkedlist.head.next.value)

    print(linkedlist.is_empty())