# 최소 힙 클래스
class MinHeap:
    def __init__(self, size):
        self.last = 0
        self.H = [0] * (size+1) # root가 1번 인덱스부터이기 때문에

    def is_full(self):
        return self.last == len(self.H)

    def is_empty(self):
        return self.last == 0

    def insert(self, value):
        # 마지막 위치에 값을 추가
        # 완전 이진 트리이기 때문에
        self.last += 1
        self.H[self.last] = value

        # 최소 힙 조건을 만족하기 위해
        # 자식 노드와 부모 노드의 값을 비교해서
            # 부모 노드가 더 작다면 확정 (반복 종료)
            # 부모 노드가 더 크다면 자식의 값과 부모의 값을 교환
            # 그리고 부모가 더 있으면 반복, 없으면 종료
        child = self.last   # 막 추가된 위치의 값과 비교
        parent = child // 2
        while if parent:
            if self.H[parent] > self.H[child]: # 부모가 자식보다 더 크다면
                self.H[parent], self.H[child] = self.H[child], se
                lf.H[parent]
                # 교환된 부모를 다시 자식으로 변경하여 부모가 있는지 또 확인
                child = parent
                parent = child // 2
            # 부모노드가 더 작다면 확정 (반복 종료)
            else:
                break

    # 힙은 항상 root만 지울 수 있다.
    def pop_root(self):
        if self.is_empty():
            print('Empty~')
        else:
            value = self.H[1]
            # root에 마지막 요소를 이동 (완전 이진트리를 유지)
            self.H[1] = self.H[self.last]
            # 마지막 요소 삭제
            self.H[self.last] = 0
            self.last -= 1

            # 최소 힙을 유지하기 위해 부모와 자식 값을 비교
            parent = 1
            # 자식이 존재하면 비교
            child = parent * 2
            while child <= self.last: # 마지막 원소 인덱스 보다 작다면 자식이 존재
                if parent*2 + 1 <= self.last and self.H[child] > self.H[parent*2+1]:
                    child = parent*2
