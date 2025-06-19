from itertools import combinations

def solution(relation):
    n_col = len(relation[0])
    n_row = len(relation)
    candidates = []

    # 1. 모든 컬럼 조합의 부분집합(1개 이상)을 탐색
    for i in range(1, n_col + 1):
        for comb in combinations(range(n_col), i):
            # 2. 유일성 확인
            projection = [tuple(item[c] for c in comb) for item in relation]
            if len(set(projection)) != n_row:
                continue

            # 3. 최소성 확인
            is_minimal = True
            for key in candidates:
                if set(key).issubset(set(comb)):
                    is_minimal = False
                    break
            if is_minimal:
                candidates.append(comb)

    return len(candidates)
