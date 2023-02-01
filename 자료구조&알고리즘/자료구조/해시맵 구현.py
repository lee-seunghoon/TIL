"""
LeetCode url : https://leetcode.com/problems/design-hashmap/
내장 라이브러리 사용 없이 해시맵 구현하기
"""
import collections


class ListNode:
    """
    연결 리스트
    """
    def __init__(self, key: int=None, value: int=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap(object):
    """
    초기화 : size, table 구성
    put(key: int, value: int) : 키와 값 맵핑으로 데이터를 삽입할 때 키가 이미 있다면 해당 키에 주어진 \
         값으로 업데이트한다.(연결 리스트 활용) - 개별 체이닝 방식 활용
    get(key: int) : 입력으로 받은 키와 맵핑된 값을 출력한다. 만약, 주어진 키에 맵핑된 값이 없다면 -1을 반환한다.
    remove(key: int) : 입력으로 받은 키와 함게 맵핑된 값까지 모두 제거한다.(맵핑된 값이 있을 경우)
    """
    def __init__(self):
        self.size = 1000
        self.table=collections.defaultdict(ListNode)


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        idx = key % self.size
        h_data = self.table[idx]

        # 만약 key값으로 추출한 idx의 값이 None이라면
        # 해당 값의 ListNode를 삽입
        if h_data.value is None:    # ==> 일반 dictionary 데이터에 없는 key값을 조회하면 에러발생.
                                    # ==> defaultdict 자료구로를 사용하면 없는 key 값을 조회했을 때, 기존 설정한 데이터 타입으로 자동 생성
                                    # ==> 현재는 ListNode로 돼 있고, ListNode의 default값은 None 
            self.table[idx] = ListNode(key, value)
            return
        
        # idx의 값이 들어있다면
        while h_data:
            # ! 기존 key값이 있다면, value만 업데이트하고 빠져나가라고 하는데 이해가 안됨...
            if h_data.key == key:
                h_data.value = value    # ==> 값을 새로운 값으로 업데이트
                return
            # 다음 값이 없다면 루프 빠져나가기
            # >> 왜? : 다음 데이터에 값을 넣어주기 위해
            if h_data.next is None:
                break
            # 다음 값이 있다면 다음 값을 탐색할 수 있도록 현재값 업데이트
            h_data = h_data.next
        
        # 가장 끝 연결리스트까지 h_data가 갱신되어 있기에
        # 다음 데이터에 추가
        h_data.next = ListNode(key, value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        idx = key % self.size
        h_data = self.table[idx]

        if h_data.value is None:
            return -1

        while h_data:
            if h_data.key == key:
                return h_data.value
            h_data = h_data.next
        # 위 while문에서 h_data.next 값이 None인데 h_data.value로 return 되지 않았다면, 연결리스트 끝까지 갔는데 값이 없다는 의미이기에 -1 반환
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx = key % self.size
        h_data = self.table[idx]

        if h_data.value is None:
            return -1

        # 첫번째 Node에 해당 값이 있을 경우
        if h_data.key == key:
            # 연결 리스트 Node가 없을 경우 : 빈 ListNode()를 부여
            # 연결 리스트 Node가 있을 경우 : 다음(next) 값으로 대체
            self.table[idx] = ListNode() if h_data.next is None else h_data.next
            return
        
        # 연결 리스트에 해당하는 Node를 삭제 해야 할 경우
        # 이전 연결 리스트 정의
        pre_hdata = h_data
        while h_data:
            if h_data.key == key:
                # 이전 연결리스트의 다음 Node 즉, 현재 지우려는 Node
                pre_hdata.next = h_data.next
                return
            pre_hdata, h_data = h_data, h_data.next
