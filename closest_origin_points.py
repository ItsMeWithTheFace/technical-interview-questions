# Given a set of points on a cartesian plane [(x, y), ...] find the k closest points to origin
import heapq

def solution(points, k):
    heap = []

    # store the distance and coordinates in the heap
    for x, y in points:
        # calculate the distance of each point to the origin
        dist = (x**2 + y**2)**(1/2)
        tuple = (dist, x, y)

        heapq.heappush(heap, tuple)

    # pop k elements from the heap
    k = k if k <= len(points) else len(points)
    result = []
    for i in range(k):
        tup = heapq.heappop(heap)
        result.append((tup[1], tup[2]))

    return result

input = [(21,2),(4,6),(9,0)]
print(solution(input, 9))
print(solution(input, 1))
print(solution(input, 0))
