'''
297. Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

[time] failed
[문제] 이진트리를 직렬화(배열)하고 반대로 역직렬화하기
[Note]
- 
'''
# re solve
class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = [root]
        result = ''

        while q :
            node = q.pop(0)

            if node :
                q.append(node.left)
                q.append(node.right)
                result += str(node.val) + '*'
            else :
                result +='None*'
        
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'None*' : return []

        nodes = data.split('*')
        root = TreeNode(int(nodes[0]))
        q = [root] 
        idx = 1

        while q :
            node = q.pop(0)

            if nodes[idx] !='None':
                node.left = TreeNode(int(nodes[idx]))
                q.append(node.left)
            idx+=1

            if nodes[idx] !='None':
                node.right = TreeNode(int(nodes[idx]))
                q.append(node.right)
            idx+=1

        return root

# solution
class Codec:
    # 직렬화
    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result = ['#']                                  # Null값을 '#'으로 표현
        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)                 # popleft활용하기 때문에 left부터 삽입
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)                         # 띄어쓰기로 값구분 ex) '12 1 2'

    # 역직렬화
    def deserialize(self, data: str) -> TreeNode:
        # 예외 처리
        if data == '# #':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))                  # result = ['#'] >> nodes[0]은 빈값
        queue = collections.deque([root])
        index = 2
        # 빠른 런너처럼 자식 노드 결과 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root



# failed code
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