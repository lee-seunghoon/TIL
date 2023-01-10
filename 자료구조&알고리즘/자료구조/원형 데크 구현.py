class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        # 왼쪽(head), 오른쪽(tail) index 역할을 할 연결리스트 정의
        self.head, self.tail = ListNode(None), ListNode(None)
        self.head.right, self.tail.left = self.tail, self.head
        
        # 최대 길이와 현재 길이 정보를 담을 변수 정의
        self.maxlen, self.length = k, 0


    def _add(self, node: ListNode, new: ListNode):
        """
        이중 연결 리스트의 삽입 메서드
        """
        # 삽입할 연결 리스트의 기존 오른쪽 값을 정의한다
        # 아마 None 값일 것으로 예상한다.
        # front : n --> self.head.right.right --> self.tail.right
        # last  n --> self.tail.left.right  --> self.head.right
        n = node.right 
        
        # 연결 리스트의 오른쪽 값을 새로운 값으로 업데이트한다.
        # front : self.head.right.right == ListNode(value)
        # last  : self.tail.left.right  == ListNode(value)
        node.right = new
        
        # 새로운 노드의 left 값은 기존 node의 값으로 정의하고 (즉, head 역할)
        # right 값은 위에서 따로 정의한 None 값으로 정의해준다
        # head - new - None
        new.left, new.right = node, n
        
        # 그리고 n의 left 값을 새로운 값으로 정의한다.
        # front : n = self.head.right.right
        # last  : n = self.tail.left.right
        n.left = new


    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        # 현재 길이 정보를 확인한다
        # 현재 길이가 최대 길이와 같다면 더이상 삽입할 수 없기에 False를 return
        if self.length == self.maxlen:
            return False
        
        # 현재 길이가 아직 최대 길이에 도달하지 않았다면 데이터를 삽입할 것이기에
        # 현재 길이를 업데이트 해준다
        self.length += 1
        
        # value값을 원형 데크 자료구조에 추가해준다.
        # 내장 함수 _add 메서드를 사용할 예정
        # value 값을 연결리스트 자료구조 형태에 담아서 추가한다.
        self._add(self.head, ListNode(value))