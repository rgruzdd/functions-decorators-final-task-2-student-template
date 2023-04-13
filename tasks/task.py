from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    new_s = [s[i:j] for i, j in zip([0] + indexes, indexes + [None])]
    if '' in new_s:
        new_s.pop()
    return new_s

print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index("no luck", [42]))

