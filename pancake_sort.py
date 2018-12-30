# Pancake sort

def flip(arr, k):
  subarray = arr[:k+1]
  subarray.reverse()
  
  return subarray + arr[k+1:]

def pancake_sort(arr):
  # [1, 5, 4, 6, 2]
  stop_index = 1
  while len(arr) - stop_index > 0:
    max_index = 0
    # gets the max index
    for i in range(len(arr) - stop_index + 1):
      if arr[i] > arr[max_index]:
        max_index = i
    
    # max val at beginning
    intermediate_arr = flip(arr, max_index)
    
    arr = flip(intermediate_arr, len(arr) - stop_index)

    print(f'arr: {intermediate_arr} {arr} {max_index}')
    
    stop_index += 1
   
  return arr

print(pancake_sort([1,5,4,3,2]))
