"""
Problem 2: Longest Palindromic Subsequence

Given a string s, return the length of the longest palindromic
subsequence.

Example:
Input : "bbbab"
Output: 4
"""


def solve(s):

    n = len(s)

    # DP table
    dp = [[0] * n for _ in range(n)]

    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = 1

    # Fill table
    for length in range(2, n + 1):

        for i in range(n - length + 1):

            j = i + length - 1

            if s[i] == s[j]:

                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 2 + dp[i + 1][j - 1]

            else:

                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


# ---------------- Driver ----------------

if __name__ == "__main__":

    s = "bbbab"

    print(solve(s))