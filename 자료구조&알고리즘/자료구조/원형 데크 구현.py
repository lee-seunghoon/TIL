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
        PEP8 명명 규칙에 따라 메서드명 구성
        이중 연결 리스트의 삽입 메서드
        """
        # 삽입할 연결 리스트의 기존 오른쪽 값을 정의한다
        # 아마 None 값일 것으로 예상한다.
        # front : n --> self.head.right --> self.tail
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
        
        
    def _del(self, node: ListNode):
        
        # ? None 값을 미리 정의하는건가?
        n = node.right.right
        
        # 업데이트
        node.right = n
        
        # ? n의 왼쪽 값을 입력한 포인터의 값으로 정의? 왜?
        n.left = node
         


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
        
    
    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        
        # 현재 길이 확인하여 최대 길이에 도달했다면 False return
        if self.length == self.maxlen:
            return False
        
        # 현재 길이 업데이트
        self.length += 1
        
        # 뒤쪽에 값을 삽입할 때는 self.tail 포인터를 활용
        # self.tail.left == 초기에 self.head로 지정했음
        # 업데이트 될 것으로 예상하면서 작업
        self._add(self.tail.left, ListNode(value))
        
    
    def deleteFront(self):
        # 삭제할 값이 없다면 False return
        if self.length == 0:
            return False
        
        # 현재 길이 업데이터
        self.length -= 1
        
        # 삭제 로직
        self._del(self.head)
        
        return True
    
    
    def deleteLast(self):
        # 삭제할 값이 없다면 False return
        if self.length == 0:
            return False
        
        # 현재 길이 업데이터
        self.length -= 1
        
        # 삭제 로직
        # 뒷 부분을 삭제할 때는 tail 포인터를 활용하는데
        # 왜 left.left의 값을 넣어주는지 궁금함
        self._del(self.tail.left.left)
        
        
    def getFront(self):
        """
        :rtype: int
        맨 앞의 값 반환
        """
        return self.head.right.val if self.length else -1
    
    
    def getRear(self):
        """
        :rtype: int
        """
        return self.tail.left.val if self.length else -1
    
    
    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.length == 0


    def isFull(self):
        """
        :rtype: bool
        """
        return self.length == self.maxlen
    
        
if __name__ == '__main__':
    obj = MyCircularDeque(3)
    obj.insertFront(1)
    obj.insertFront(3)
    obj.insertLast(2)
    obj.insertLast(4)
    print(obj.head.right.right.val)
    print(obj.tail.left)