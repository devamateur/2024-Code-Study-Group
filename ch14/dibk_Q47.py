'''
297. Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

[time] 5시 42분
[문제] 이진트리를 직렬화(배열)하고 반대로 역직렬화하기
[풀이방식]
- 
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        q = [root]
        
        while q :
            node = q.pop(0)
            if not node : 
                result.append(None)
                continue
            else :
                result.append(node.val)

            if node.left :
                q.append(node.left)
            if node.right :
                q.append(node.right)

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        move = node = TreeNode()

        for d in data :
            



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))