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
        # 초기 값이 [0, None] 이 상태로 들어가겠네
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장한다
        for i, lst in enumerate(lists):
            # 이 말은 lists 노드의 i번째 값이 있으면(None이 아니면)
            if lists[i]:
                # heappush의 인자값이 중복이 있다면, 에러를 발생하기 때문에
                # 중복된 값을 구분할 수 있는 추가 인자값이 필요하다.
                heap.heappush(heap, (lists[i].val, i, lists[i]))


if __name__ == "__main__":
    first_node = ListNode(1)
    first_node.next = ListNode(4)
    first_node.next.next = ListNode(5)
    print(first_node.next.next.val)

    test = [[1,4,5],[1,3,4],[2,6]]
    obj = Solution()
    # print(result)