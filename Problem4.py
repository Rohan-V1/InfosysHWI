"""
Problem:
Given a stripe consisting of 'W' and 'B',
find the minimum number of white cells that
must be recoloured so that there are k
consecutive black cells.

Example:
stripe = "WBBWWBBWBW"
k = 7

Output:
3
"""


def solve(stripe, k):

    n = len(stripe)

    # Count whites in first window
    white = 0

    for i in range(k):
        if stripe[i] == 'W':
            white += 1

    ans = white

    # Slide the window
    for i in range(k, n):

        # Remove left character
        if stripe[i - k] == 'W':
            white -= 1

        # Add right character
        if stripe[i] == 'W':
            white += 1

        ans = min(ans, white)

    return ans


if __name__ == "__main__":

    stripe = "WBBWWBBWBW"
    k = 7

    print(solve(stripe, k))