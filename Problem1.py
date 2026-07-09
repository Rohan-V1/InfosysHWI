"""
Problem 1: Mobile Game Battery Drain

You are playing a mobile game with B% battery on your phone.

There are N power moves available, where C[i] represents the battery
drained by the ith move.

Each power move can be used at most 2 times.

Find the minimum number of power moves required to reduce the battery
to 0 or below.

If it is impossible, return -1.

Example:
B = 20
N = 3
C = [8, 5, 3]

Output:
3
"""


def solve(B, N, C):

    # Create a list containing each move twice
    moves = []

    for drain in C:
        moves.append(drain)
        moves.append(drain)

    # Sort in descending order
    moves.sort(reverse=True)

    battery = B
    moves_used = 0

    # Pick the largest battery drains first
    for drain in moves:
        battery -= drain
        moves_used += 1

        if battery <= 0:
            return moves_used

    # Battery could not be drained completely
    return -1


# ---------------- Driver Code ----------------

if __name__ == "__main__":

    B = 20
    N = 3
    C = [8, 5, 3]

    print(solve(B, N, C))