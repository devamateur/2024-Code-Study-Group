'''
147. Insertion Sort List
https://leetcode.com/problems/insertion-sort-list/description/

[time] failed
[문제] linked-list를 정렬하기(삽입정렬 활용)
[풀이방식]
- 값을 저장할 노드 생성 : root,   root에 값을 입력하며 이동할 포인터 : node
- 비교할 노드를 단일 노드로 만들고(val-None 형태 : comp), 현재 노드next와 비교노드를 비교하기
- 비교노드 값이 크면, node.next에 입력하고 비교노드의 next를 현재노드리스트를 삽입
- node의 포인터를 다시 root로 옮겨서 while 실행
'''

# solution
# head = [4,2,1,3]
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        node = root = ListNode(None)                            # node : None-None
        
        while head:
            comp, _ = head, head.next                          
            comp.next = None                                    # comp : 4-None     ## comp : 2-None        #~# 3-None

            while node.next and node.next.val < comp.val:                           ## node : None-"4"-None    #~# None-"1"-2-4-None
                node = node.next                                                    #~# node : 2-"4"-None

            node.next, comp.next = comp, node.next              # node : None-"4"-None  ## None-"2"-4-None      #~# 2-"3"-4-None
            
            head = _
            node = root                                         # node : "None"-4-None  ## "None"-2-4-None      #~# "None"-1-2-3-4-None

        return root.next

# failed
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = result = ListNode()

        while head :
            cur, _ = head, head.next
            cur.next = None

            while node.next and node.next.val < cur.val :
                node = node.next

            if node.next and node.next.val > cur.val :
                cur, node.next = node.next,cur
                node = node.next
                                                            # 여기서 문제
            node.next = cur
            head = _

        return result.next