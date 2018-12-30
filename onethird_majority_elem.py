# Given a list of positive integers, find a 1/3 majority element, if it exists
# You only have the == operator for comparisons

# Divide and conquer solution (we could've done this in linear time)
# This runs in nlogn + n + nlog_3(n) time
def solution(nums):
    return solution_helper(sorted(nums))
def solution_helper(nums):
    if len(nums) <= 0:
        return -1
    elif len(nums) == 1:
        return nums[0]
    else:
        third = int(round(len(nums)/3))
        l_num = solution_helper(nums[:third])
        m_num = solution_helper(nums[third:2*third])
        r_num = solution_helper(nums[2*third:])

        counts = {
            l_num: 0,
            m_num: 0,
            r_num: 0
        }

        for key in counts:
            counts[key] += nums.count(key)

        print(counts)
        max_occ = -1

        for key in counts:
            if (key > 0) and (counts[key] > len(nums) / 3):
                max_occ = key
        
        return max_occ

# Tests
# print(solution([1,1,2]))
# print(solution([1,3,2]))
# print(solution([1,2,3,4,5]))
# print(solution([1,1,3,4,5]))
# print(solution([1,1,1,1,5,6,7,8,9]))
print(solution([2,1,2,1,1,2,1,3]))
# print(solution([1,1,2,3,5,6,1,1,9,10,11,1,13,14]))
