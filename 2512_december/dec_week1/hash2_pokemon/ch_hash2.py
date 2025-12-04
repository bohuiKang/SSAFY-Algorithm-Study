def solution(nums):
    hsh = set()
    length = len(nums)/2
    for pokemon in nums:
        hsh.add(pokemon)
    if len(hsh) >= length:
        return length
    else:
        return len(hsh)