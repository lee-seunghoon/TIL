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
        cur_val=self.q[self.rp]
        if cur_val is None:
            cur_val = value
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
        cur_val = self.q[self.fp]
        # front pointer의 값이 아무것도 없으면 삭제할 값이 없다는 의미
        if cur_val is None:
            return False
        # 값이 있으면, 그 값을 삭제하되 출력(반환)되지 않도록 세팅 필요
        else:
            cur_val = None
            # front pointer를 업데이트한다.
            self.fp = (self.fp + 1) % self.maxlen
            return True
        

    def Front(self):
        """
        :rtype: int
        """
        

    def Rear(self):
        """
        :rtype: int
        """
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        

    def isFull(self):
        """
        :rtype: bool
        """
        

if __name__ == '__main__':
    # Your MyCircularQueue object will be instantiated and called as such:
    # obj = MyCircularQueue(k)
    # param_1 = obj.enQueue(value)
    # param_2 = obj.deQueue()
    # param_3 = obj.Front()
    # param_4 = obj.Rear()
    # param_5 = obj.isEmpty()
    # param_6 = obj.isFull()