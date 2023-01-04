class MyQueue(object):

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        # input 값을 재정렬하는 과정 거친 후
        self.peek()
        # 제일 처음에 들어온 값을 추출
        return self.output.pop()

    def peek(self):
        """
        :rtype: int
        """
        # 출력값이 아무것도 없다면 입력값 확인해서 값 재정렬
        if not self.output:

            # 새로 들어온 값이 있다면
            # 해당 값은 output으로 queue 구조로 재입력 돼야 함
            while self.input:

                # 우선 input값에서 마지막 값을 빼고
                # 해당 값을 output에 집어 넣는다
                self.output.append(self.input.pop())

        # 결과값이 맨 마지막 위치한 값이 제일 처음 들어온 값으로 위에서 세팅했음
        return self.output[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        # 입력값과 결과값 stack을 모두 확인해야 함
        # 입력값에 값이 들어온 후 결과값에 재정령 안 돼 있을 수도 있기 때문
        return self.input == [] and self.output == []


if __name__ == '__main__':
    myQueue = MyQueue()
    myQueue.push(1) # queue is: [1]
    myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
    print(myQueue.peek()) # return 1
    print(myQueue.pop()) # return 1, queue is [2]
    print(myQueue.empty()) # return false