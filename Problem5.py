"""
Enemy Army Minimisation

Given N soldiers, reduce the army to exactly 1 soldier.

Allowed moves:
1. N -> N - 1
2. N -> ceil(N / 2)
3. N -> ceil(N / 3)

Return the minimum number of moves.
"""


def solve(n):

    dp = [0] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):

        dp[i] = 1 + min(
            dp[i - 1],
            dp[(i + 1) // 2],
            dp[(i + 2) // 3]
        )

    return dp[n]



if __name__ == "__main__":

    n = 10

    print(solve(n))