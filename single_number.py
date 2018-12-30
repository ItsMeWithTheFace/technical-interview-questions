# given a list of integers where each element
# appears twice except for one which appears once,
# find that single element

# runs in linear time with linear space
def singleNumber(nums):
    counts = {}
    
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    for num in counts:
        if counts[num] == 1:
            return num

# runs in linear time with constant space
# if you do elem1 XOR elem2 XOR ... you can cancel
# out the repeats since A XOR A = 0
# leaving you with SINGLE XOR 0 = SINGLE
def singleNumberXOR(nums):
    single = 0
    for num in nums:
        single ^= num
    
    return single

print(singleNumberXOR([2,3,3])) # prints 2
