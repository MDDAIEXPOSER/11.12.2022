# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que, result_block = [root], []
        while len(que): 
            qq_of_len, row = len(qq_of_len), 0
            for element in range(qq_of_len):
                current = que.pop(0)
                row += current.val
                if current.left:
                    que.append(current.left)
                if current.right:
                    que.append(current.right)
            result_block.append(row/qq_of_len)
        return result_block