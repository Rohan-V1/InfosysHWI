"""
Chef and Happy String

Return:
Happy -> if there are 3 or more consecutive vowels
Sad   -> otherwise
"""


def solve(s):
    vowels = ['a','e','i','o','u']

    for i in range(len(s)-2):
        if s[i] in vowels:
            if s[i+1] in vowels and s[i+2] in vowels:
                return 'HAPPY'
    
    return 'SAD'


if __name__ == "__main__":

    s = "abcdeeafg"

    print(solve(s))