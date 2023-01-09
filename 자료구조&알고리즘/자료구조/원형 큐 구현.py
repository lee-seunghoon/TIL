class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [None] * k     # 원형 큐 정의 (배열 활용)
        self.maxlen = k         # 최대 길이 정의
        self.fp = 0             # front pointer
        self.rp = 0             # rear pointer
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        # 값을 추가할 때는 rear pointer를 활용한다
        # rear 포인터 위치에 있는 큐 값이 없으면 입력된 value를 넣어준다
        if self.q[self.rp] is None:
            self.q[self.rp] = value
            # 입력해준 후 rear 포인터이 값을 업데이트 한다
            self.rp = (self.rp + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self):
        """
        :rtype: bool
        원형 큐의 첫 번째 값이 제거되도록
        """
        # 값을 삭제할 때는 front pointer를 활용한다.
        # front pointer의 값이 아무것도 없으면 삭제할 값이 없다는 의미
        if self.q[self.fp] is None:
            return False
        # 값이 있으면, 그 값을 삭제하되 출력(반환)되지 않도록 세팅 필요
        else:
            self.q[self.fp] = None
            # front pointer를 업데이트한다.
            self.fp = (self.fp + 1) % self.maxlen
            return True
        

    def Front(self):
        """
        :rtype: int
        원형 큐의 맨 앞에 있는 값을 반환
        값이 없을 경우 -1 반환
        """
        return -1 if self.q[self.fp] is None else self.q[self.fp]
        

    def Rear(self):
        """
        :rtype: int
        원형 큐의 맨 뒤에 있는 값을 반환
        값이 없을 경우 -1 반환
        """
        # rear pointer 에서 1을 빼준 위치에서 값을 가져와야 한다.
        return -1 if self.q[self.rp - 1] is None else self.q[self.rp - 1]
        

    def isEmpty(self):
        """
        :rtype: bool
        값이 비어 있을 경우 True, 아닐 경우 False
        """
        return self.fp == self.rp and self.q[self.fp] is None
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.fp == self.rp and self.q[self.fp] is not None
        

if __name__ == '__main__':
    # Your MyCircularQueue object will be instantiated and called as such:
    obj = MyCircularQueue(3)
    
    param_1 = obj.enQueue(1)
    print(param_1)
    print(obj.q)

    param_2 = obj.enQueue(2)
    print(obj.q)

    param_3 = obj.enQueue(3)
    print(obj.q)

    param_4 = obj.enQueue(3)
    print(obj.q)
    print(param_4)

    param_4 = obj.Rear()
    print(param_4)

    param_5 = obj.deQueue()
    print(param_5)
    print(obj.q)

    param_6 = obj.Front()
    print(param_6)
    param_7 = obj.isEmpty()
    print(param_7)
    param_8 = obj.isFull()
    print(param_8)