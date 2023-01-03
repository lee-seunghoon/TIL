import collections

class MyStack(object):

    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Step1. 값을 집어 넣는다
        self.q.append(x)

        # Step2. 데이터를 재정렬한다.
        # 현재 들어 있는 값중 맨 마지막 값은 가만히 있으면 되기 때문에
        # 전체 개수에서 1개 뺀만큼만 이동하면 된다.
        for _ in range(len(self.q)-1):
            # deque 자료구조의 연산중 popleft는 결국 que의 선입선출 연산구조를 의미한다.
            self.q.append(self.q.popleft())
        
    def pop(self):
        """
        :rtype: int
        """
        return self.q.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.q[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q)==0


if __name__ == '__main__':
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    print(myStack.top()) # return 2
    print(myStack.pop()) # return 2
    print(myStack.empty()) # return False