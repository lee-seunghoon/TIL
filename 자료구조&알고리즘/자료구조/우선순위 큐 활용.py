from heapq import heappush, heappop

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 초기 값이 [None, None] 이 상태로 들어간다
        root = result = ListNode(None)
        """
        print(result.val)   # ==> None
        print(result.next)  # ==> None
        """
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장한다
        for i, lst in enumerate(lists):
            print(lst.val)
            print(type(lst))
            # 이 말은 lists 노드의 i번째 값이 있으면(None이 아니면)
            if lists[i]:
                # heappush의 인자값이 중복이 있다면, 에러를 발생하기 때문에
                # 중복된 값을 구분할 수 있는 추가 인자값이 필요하다.
                # heappush 활용해서 값을 추가할 때 heap 정렬의 구조에 따라 들어가는걸 확인할 수 있음
                heappush(heap, (lists[i].val, i, lists[i]))
                """
                Input : [ListNode([1,4,5]),ListNode([1,3,4]),ListNode([2,6])]

                Output :
                [([1, 3, 4], 1, <__main__.ListNode object at 0x0371A590>), 
                 ([1, 4, 5], 0, <__main__.ListNode object at 0x0371A570>), 
                 ([2, 6], 2, <__main__.ListNode object at 0x0371A1F0>)]
                """
        
        # heap 자료구조 안에 데이터가 다 없어질때까지 로직 구현
        while heap:

            # heappop으로 값을 가져오면 가장 작은 노드의 연결 리스트부터 차례대로 나온다.
            # 여기서 node는 tuple type  ex) ([2, 6], 2, <__main__.ListNode object at 0x0371A1F0>)
            node = heappop(heap)
            # 위에서 설정한 연결 리스트의 index값
            idx = node[1]
            # 연결 리스트로 정의된 객체 자체를 정답 값으로 업데이트
            result.next = node[2]   # => ex) <__main__.ListNode object at 0x0371A1F0>
            
            # result 값 갱신
            result = result.next
            
            if result.next:
                # heap 자료구조에 다시 추가한다.
                heappush(heap, (result.next.val, idx, result.next))

        print(root.next.val)
        return root.next


if __name__ == "__main__":
    first_node = ListNode([1,4,5])
    first_node.next = ListNode(4)
    first_node.next = ListNode(5)
    # print(first_node.val)
    # print(first_node.next.val)
    # print(first_node.next.next)

    test = [ListNode([1,4,5]),ListNode([1,3,4]),ListNode([2,6])]
    sol = Solution()
    sol.mergeKLists(test)
    # print(result)