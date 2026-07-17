"""
Conference Room Dilemma

Return the minimum number of rooms required.
"""

import heapq

def solve(intervals):
    if not intervals:
        return 0


    intervals.sort()

    heap = []

    heapq.heappush(heap, intervals[0][1])

    for start, end in intervals[1:]:


        if start >= heap[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, end)

    return len(heap)
    


if __name__ == "__main__":

    intervals = [
        [0, 30],
        [5, 10],
        [15, 20],
        [25, 35]
    ]

    print(solve(intervals))