"""
Egor and the Card Rounds

Return the maximum number of rounds won.
"""


def solve(cards, l, r):
    curr = 0
    count = 0

    for card in cards:
        curr += card

        if l <= curr <= r:
            count += 1
            curr = 0
        elif curr > r:
            curr = 0

    return count


if __name__ == "__main__":

    cards = [2, 1, 3, 2, 2]

    l = 3
    r = 5

    print(solve(cards, l, r))