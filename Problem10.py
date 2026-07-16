"""
Missing Couple Registration ID

Every ID appears twice except one.

Return the missing ID.
"""


def solve(arr):

    for id in arr:
        if arr.count(id) < 2:
            return id


if __name__ == "__main__":

    arr = [2, 5, 2, 8, 8]

    print(solve(arr))