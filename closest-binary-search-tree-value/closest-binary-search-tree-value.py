class Solution:
    def closestValue(self, root, target):
        closest = root.val
        while root:
            if abs(target - root.val) < abs(target - closest) or (abs(target - root.val) == abs(target - closest) and root.val < closest):
                closest = root.val
            root = root.left if target < root.val else root.right
        return closest

