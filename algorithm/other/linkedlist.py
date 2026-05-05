from mimetypes import init

#创建节点类
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
#创建链表类
class Singlelinkedlist:
    def __init__(self):
        self.head = None

    #判断链表是否为空
    def is_empty(self):
        return self.head is None

    #计算长度
    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next

        return count

    #遍历链表
    def travel(self):
        cur = self.head
        while cur is not None:
            print(cur.value)
            cur = cur.next
        return cur

    #在链表头部添加新节点
    def add(self, value):
        #创建一个新的头节点
        new_node = Node(value)
        #将原链表的头节点的地址传递给新节点的地址域
        new_node.next = self.head
        #将新节点设置为头节点
        self.head = new_node

    #在链表尾部添加元素
    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    #在指定位置增加节点
    def insert(self, pos, value):
        if pos <= 0:
            self.add(value)
        elif pos >= self.length():
            self.append(value)
        else:
            cur = self.head
            count = 0
            new_node = Node(value)

            while count < pos-1:
                cur = cur.next
                count += 1

            new_node.next = cur.next
            cur.next = new_node

    #在链表中删除元素
    def remove(self, value):
        cur = self.head
        prev = None
        while cur is not None:
            if cur.value == value:
                if cur == self.head:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                    return

            prev = cur
            cur = cur.next

    #查找节点是否存在
    def search(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return True
            cur = cur.next

        return False

if __name__ == '__main__':
    #创建链表
    linkedlist = Singlelinkedlist()
    #定义链表头节点和第二个节点
    linkedlist.head = Node(5)
    linkedlist.head.next = Node(6)

    #在链表头部添加新节点
    linkedlist.add(9)

    #在链表尾部添加元素
    linkedlist.append(10)

    #在链表指定位置添加节点
    linkedlist.insert(2, 1)

    #在链表指定位置删除元素
    linkedlist.remove(5)

    #在链表中查找元素
    print(linkedlist.search(9))

    #打印链表值
    print(linkedlist.head.value)
    print(linkedlist.head.next.value)
    print("-"*32)
    #检查链表是否为空
    print(linkedlist.is_empty())
    print("-"*32)
    #打印链表长度
    print(linkedlist.length())
    print("-"*32)
    #遍历链表
    print(linkedlist.travel())
    print("-"*32)
    #