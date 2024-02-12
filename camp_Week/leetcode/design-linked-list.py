class Node:

    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = Node()

    def getNode(self , index: int):

        dum = self.head

        while(dum and index >= 0):
            dum = dum.next
            index -= 1
        return dum

    def get(self, index: int) -> int:

        if(index < 0):
            return -1

        node = self.getNode(index)
        print(node)
        if(node):
            return node.val
        return -1


    def addAtHead(self, val: int) -> None:
        node = Node(val , self.head.next)
        self.head.next = node


    def addAtTail(self, val: int) -> None:
        dum = self.head.next
        while(dum and dum.next):
            dum = dum.next
        node = Node(val)
        if(not dum):
            self.head.next = node
        else:
            dum.next = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        node = self.getNode(index - 1)

        if(node):
            new_node = Node(val , node.next)
            node.next = new_node
        


    def deleteAtIndex(self, index: int) -> None:

        node = self.getNode(index - 1)

        if node:
            if(node.next):
                node.next = node.next.next
            else:
                node.next = None

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)