class MyHashSet:

    def __init__(self):
        self.keyRange = 769
        self.bucketArray = [bucket() for i in range(self.keyRange)]

    def add(self, key: int) -> None:
        bucketIdx = key % self.keyRange
        self.bucketArray[bucketIdx].insert(key)

    def remove(self, key: int) -> None:
        bucketIdx = key % self.keyRange
        self.bucketArray[bucketIdx].delete(key)

    def contains(self, key: int) -> bool:
        bucketIdx = key % self.keyRange
        return self.bucketArray[bucketIdx].exists(key)
class Node:
    def __init__(self, val, nextNode = None):
        self.val = val
        self.next = nextNode

class bucket:
    def __init__(self):
        self.head = Node(0)

    def insert(self, key):
        if not self.exists(key):
            new_node = Node(key, self.head.next)
            self.head.next = new_node 
        
    def delete(self, key):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.val == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, key):
        curr = self.head.next
        while curr is not None:
            if curr.val == key:
                return True
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)