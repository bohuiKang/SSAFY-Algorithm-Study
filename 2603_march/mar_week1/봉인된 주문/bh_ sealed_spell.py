# 알파벳 소문자 11글자 이하
# a: 1번, z: 26번 26^1

def solution(n, bans): # n번째 주문 찾기, 삭제된 주문 담은 bans

    bans_num = []
    for ban in bans:
        bans_num.append(str_to_num(ban))

    bans_num = sorted(bans_num) # 오름차순 정렬

    find_n = n
    for b_n in bans_num:
        if b_n <= find_n:
            find_n += 1 # 앞의 숫자가 사라졌으니 찾는 숫자는 사라진 숫자 만큼 뒤로 이동
        else: 
            break

    return num_to_str(find_n)

# 문자를 숫자로
def str_to_num(ban):
    num = 0
    for s in ban:
        num = num * 26 + (ord(s) - ord('a') + 1) # 아스키 코드 변환
    return num

# 숫자를 문자로
def num_to_str(n):
    char = []
    while n > 0:
        n -= 1
        char.append(chr(ord('a') + (n % 26))) # 나머지를 변환
        n //= 26 # 몫을 남김

    return "".join(reversed(char))


print(solution(30, ["d", "e", "bb", "aa", "ae"]))
print(solution(7388, ["gqk", "kd    n", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"]))
