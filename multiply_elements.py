# Given an array of positive integers and maybe 0
# Mutate the array such that every element becomes
# the product of the other elements

# runs in O(n) time
def solution(nums):
    product = 1
    zeroes = 0

    for num in nums:
        if num == 0:
            zeroes += 1
        else:
            product *= num
    
    # go through list again
    for i in range(len(nums)):
        # if zeroes > 1 everything is 0
        if zeroes > 1:
            nums[i] = 0
        # if zeroes <= 1, just check for it
        elif zeroes == 1:
            if nums[i] == 0:
                nums[i] = product
            else:
                nums[i] = 0
        else:
            nums[i] = product // nums[i]

    return nums

# this also runs in O(n) but no division (in progress)
def solution2(nums):
    product = 1
    result = []
    for i in range(len(nums)):
        result.append(product)
        product *= nums[i]
    
    product = 1
    for i in range(len(result) - 1, -1, -1):
        result[i] = result[i] * product
        product *= nums[i]
    
    return result

print(solution([1,2,3,4]))
print(solution([1,2,3,0]))
print(solution([1,0]))
print(solution([1,2,0,4,0]))

print(solution2([1,2,3,4]))
print(solution2([1,0,3,4]))
print(solution2([1,0]))
print(solution2([1,2,0,4,0]))
