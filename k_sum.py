# Given an array of positive integers find if any subsequence == value k input is array and value k

# This solution runs in O(n^2) and works on continuous subsequences
def solution(nums, k):
    i = 0
    j = i

    result = []
    curr_k = k

    while i < len(nums) and j < len(nums):
        if nums[j] < curr_k:
            result.append(nums[j])
            curr_k -= nums[j]
            j += 1
        elif nums[j] == curr_k:
            result.append(nums[j])
            return result
        else:
            result = []
            curr_k = k
            i += 1
            j = i

    return "No subsequence found"

# this one runs in linear time, sequence has to be continuous though
def solution2(nums, k):
    result = []
    curr_sum = 0

    # run through the numbers
    for num in nums:
        # add num to our result
        result.append(num)
        curr_sum += num
        # if our new sum becomes bigger than k
        while curr_sum > k:
            val = result.pop(0)
            curr_sum -= val
        # remove elements from the beginning until sum <= k
        if curr_sum == k:
            return result
    
    return "No subsequence found"


input = [4,6,9,1]
print(solution(input, 15))
print(solution2(input, 15))
