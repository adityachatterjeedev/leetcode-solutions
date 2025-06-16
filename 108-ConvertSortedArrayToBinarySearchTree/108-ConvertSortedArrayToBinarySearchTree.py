# Last updated: 6/16/2025, 3:22:52 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(val = nums[0])
        
        middleIndex = len(nums) // 2
        rootNode = TreeNode(val = nums[middleIndex])
        rootNode.left = self.sortedArrayToBST(nums[0:middleIndex])
        rootNode.right = self.sortedArrayToBST(nums[middleIndex + 1:])
        return rootNode
