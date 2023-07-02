class TreeNode:
    def __init__(self, x):
        self.val = x
        self.cnt = 1
        self.left = None
        self.right = None


class KthLargest:
    def __init__(self, k, nums):
        self.root = None
        self.k = k
        for num in nums:
            self.root = self.insertNode(self.root, num)

    def insertNode(self, root, num):
        if not root:
            return TreeNode(num)
        if root.val < num:
            root.right = self.insertNode(root.right, num)
        else:
            root.left = self.insertNode(root.left, num)
        root.cnt += 1
        return root

    def searchKth(self, root, k):
        m = root.right.cnt if root.right else 0
        if k == m + 1:
            return root.val
        if k <= m:
            return self.searchKth(root.right, k)
        else:
            return self.searchKth(root.left, k - m - 1)

    def add(self, val):
        self.root = self.insertNode(self.root, val)
        return self.searchKth(self.root, self.k)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
