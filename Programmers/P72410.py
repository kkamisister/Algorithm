def solution(new_id):
    # 1단계 : 소문자 치환
    new_id = new_id.lower()

    # 2단계 : 유효하지 않은 문자 제거
    result = ''
    valid = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.'
    for string in new_id:
        if string in valid:
            result += string
    new_id = result

    # 3단계 : 마침표 치환
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계 : 앞뒤 마침표 제거
    while new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5단계 : 빈 문자열 'a'대입
    if not new_id:
        new_id += 'a'

    # 6단계 : 길이 줄이고 마지막 마침표 제거
    if 16 <= len(new_id):
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 7단계 : 길이 맞추기
    while len(new_id) < 3:
        last = new_id[-1]
        new_id += last

    answer = new_id
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))