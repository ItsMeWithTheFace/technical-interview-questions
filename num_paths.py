# Given a number 1 <= n <= 100 which represents a grid size of n-1 x n-1
# Find the number of paths from (0,0) to (n-1,n-1)
# You can't go across the diagonal of the grid as shown below (can't land on O's)
# O O O X
# O O X X
# O X X X
# X X X X
# n = 4 example

def num_of_paths_to_dest(n):
  # paths = [] # [“EEENNN”, “EENENN”, “ENEENN”, “ENENEN”, “EENNEN”]
  count = 0
  def num_of_paths_helper(i, j):
    if i == 0 and j == 0:
      nonlocal count  # python 3 feature, if we're in python 2 we'll need to keep a list 
      count += 1
    else:
      if j <= i:
        # if we're here, we're on a diagonal space, can only go down
        if i - 1 < j:
          num_of_paths_helper(i, j - 1)
        else:
          # check if we can go up
          if j > 0:
            num_of_paths_helper(i, j - 1)
          # check if we can go right
          num_of_paths_helper(i - 1, j)

  num_of_paths_helper(n-1, n-1)
  return count

# Tests
print(num_of_paths_to_dest(6))
print(num_of_paths_to_dest(17))
print(num_of_paths_to_dest(1))
