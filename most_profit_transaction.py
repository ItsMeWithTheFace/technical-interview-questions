# Given a list of prices of a stock on each day, you are allowed to do one transaction
# (buy and sell). Find a transaction that gives the maximum profit

# Naive way - 2 pointers and check differences in all pairs
# runs in n^2
def solution(prices):
    i = 0
    j = 1

    results = []

    while i < len(prices):
        while j < len(prices):
            if prices[i] <= prices[j]:
                results.append(prices[j] - prices[i])
            j += 1

        i += 1
        j = i + 1
    
    return max(results) if len(results) > 0 else 0

# Reversed counting inversions with mergesort
# runs in nlogn
def solution2(prices):
    def solution2_rec(prices):
        if len(prices) == 1:
            return ([0], prices)
        else:
            half = int(len(prices) / 2)
            (l_inv, left) = solution2_rec(prices[:half])
            (r_inv, right) = solution2_rec(prices[half:])

            invs = []
            combined = []
            while len(left) > 0 and len(right) > 0:
                if left[0] < right[0]:
                    invs.append(right[-1] - left[0])
                    combined.append(left.pop(0))
                else:
                    combined.append(right.pop(0))

            if len(left) > 0:
                combined = combined + left
            elif len(right) > 0:
                combined = combined + right

            return (invs + l_inv + r_inv, combined)

    (diffs, _) = solution2_rec(prices)
    return max(diffs)

# using some variant of Kadane's algorithm (not sure how yet)
def solution3(prices):
    max_so_far = 0
    max_ending_here = 0

    for price in prices:
        max_ending_here += price
        if (max_ending_here < 0):
            max_ending_here = 0
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far

# Tests
print(solution2([7,2,5,6,3]))
print(solution2([6,5,4,3,2,1]))

print(solution3([-3,4,-1]))
