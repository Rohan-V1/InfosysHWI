"""
Saying Hello in a Chat

Return:
YES -> if "hello" is a subsequence
NO  -> otherwise
"""


def solve(s):
    word = 'hello'
    j = 0
    i = 0
    while i < len(s):
        if s[i] == word[j]:
            j += 1
            i += 1
            if j == len(word):
                return 'YES'
        else:
            i+=1

    return 'NO'



if __name__ == "__main__":

    s = "ahhellllloou"

    print(solve(s))