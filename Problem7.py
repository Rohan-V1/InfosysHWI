"""
Rod Cutting

Given:
n = Length of rod
price[i] = Price of rod of length i+1

Return the maximum obtainable profit.

Example:
n = 8
price = [1,5,8,9,10,17,17,20]

Output:
22
"""

def solve(n, price):

    dp = [0]*(n+1)

    for length in range(1, n + 1):

        maximum = 0

        for cut in range(1, length + 1):

            maximum = max(
                maximum,
                price[cut - 1] + dp[length - cut]
            )

        dp[length] = maximum

    return dp[n]


if __name__ == "__main__":

    n = 8
    price = [1,5,8,9,10,17,17,20]

    print(solve(n, price))