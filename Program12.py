"""
Suneet and Slavic's Card Game

Return the number of games
where Suneet wins.
"""


def solve(a1, a2, b1, b2):

    suneet = [
        [a1, a2],
        [a2, a1]
    ]

    slavic = [
        [b1, b2],
        [b2, b1]
    ]

    answer = 0

    for s in suneet:
        for t in slavic:

            suneetWins = 0
            slavicWins = 0

            # Round 1
            if s[0] > t[0]:
                suneetWins += 1
            elif s[0] < t[0]:
                slavicWins += 1

            # Round 2
            if s[1] > t[1]:
                suneetWins += 1
            elif s[1] < t[1]:
                slavicWins += 1

            if suneetWins > slavicWins:
                answer += 1

    return answer

    


if __name__ == "__main__":

    a1 = 8
    a2 = 9

    b1 = 2
    b2 = 6

    print(solve(a1, a2, b1, b2))