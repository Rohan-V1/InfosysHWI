"""
Job Sequencing with Deadlines

Return

[jobsDone, maximumProfit]
"""


def solve(deadline, profit):

    jobs = []

    for i in range(len(deadline)):
        jobs.append((profit[i], deadline[i]))

    jobs.sort(reverse=True)

    maxDeadline = max(deadline)

    slots = [-1] * (maxDeadline + 1)

    jobsDone = 0
    totalProfit = 0

    for p, d in jobs:

        for day in range(d, 0, -1):

            if slots[day] == -1:

                slots[day] = p
                jobsDone += 1
                totalProfit += p
                break

    return [jobsDone, totalProfit]



if __name__ == "__main__":

    deadline = [2, 1, 2, 1, 3]
    profit = [100, 19, 27, 25, 15]

    print(solve(deadline, profit))