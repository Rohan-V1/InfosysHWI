"""
Problem:
Check whether the string "hello" is a subsequence of s.

Return:
YES -> if "hello" is present as a subsequence
NO  -> otherwise

Example:
s = "ahhellllloou"

Output:
YES
"""


def solve(s, target):
    
    j = 0

    for ch in s:
        if j < len(target) and ch == target[j]:
            j += 1

    return j == len(target)


if __name__ == "__main__":
    s = "ahhellllloou"
    target = "hello"

    print(solve(s, target))