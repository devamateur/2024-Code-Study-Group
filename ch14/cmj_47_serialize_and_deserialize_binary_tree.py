import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    i=0
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def bfs(node):
            queue = [node]
            serialized = []
            while queue:
                new_node = queue.pop(0)
                if new_node:
                    queue.append(new_node.left)
                    queue.append(new_node.right)

                    serialized.append(str(new_node.val))
                else:
                    serialized.append('#')

            return serialized
        
        result = bfs(root)
        
        return ' '.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not any(s.isdigit() for s in data):     # 숫자가 하나도 없으면
            return None

        nodes = data.split()
        root = TreeNode(int(nodes[0]))
        queue = collections.deque([root])
        index = 1    # 현재 노드의 왼쪽 자식

        # 자식 노드 결과 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':       # 왼쪽 자식
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':       # 오른쪽 자식
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root
    
    # 방법2. dfs
    def serialize2(self, root):

        result = []
        def dfs(root):
            if(root is None):
                result.append("N")
                return
            result.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ' '.join(result)
        

    def deserialize2(self, data):

        vals = data.split()
        
        def dfs():
            if(vals[self.i] == "N"):
                self.i += 1
                return
            node = TreeNode(vals[self.i])
            self.i += 1         # 자식 노드 탐색을 위한 인덱스 증가
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()