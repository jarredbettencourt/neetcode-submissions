class ListNode:

    def __init__(self, val, next = None):
        self.next = next
        self.val = val

class LinkedList:
    
    def __init__(self):
        self.tail = None
        self.head = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if self.length <= index or not self.head:
            return -1
        cur = self.head
        while index != 0:
            cur = cur.next
            index -= 1
        return cur.val if cur else -1

    def insertHead(self, val: int) -> None:
        if not self.head:
            new = ListNode(val)
            self.tail = new
            self.head = new
            self.head.next = self.tail
        else:
            new = ListNode(val, self.head)
            self.head = new
        self.length += 1

    def insertTail(self, val: int) -> None:
        if not self.tail:
            new = ListNode(val)
            self.tail = new
            self.head = new
            self.head.next = self.tail
        else:
            new = ListNode(val)
            self.tail.next = new
            self.tail = new
        self.length += 1

    def remove(self, index: int) -> bool:
        if index > self.length:
            return False
        cur = ListNode(0, self.head)
        while index != 0:
            cur = cur.next
            index -= 1
        if cur.next:
            cur.next = cur.next.next
        self.length -= 1
        return True
        

    def getValues(self) -> List[int]:
        res = []
        cur = self.head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
