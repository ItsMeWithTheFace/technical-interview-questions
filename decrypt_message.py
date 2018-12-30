# def decrypt(word):
#   frst = first ascii char
#   prev_char = None
#   prev_char += frst
  
#   res = ""
#   for each subsequent char:
#     new_char = char's ascii - prev_char ascii
#     while new_char ascii not in range(97, 123):
#       new_char += 26
#     res += new_char
#     prev_char += new_char
#   return res # your code goes here

def decrypt(word):
  first = ord(word[0])
  prev_char = first
  
  res = ""
  
  if first == 97:
    res.append(chr(122))
  else:
    res.append(chr(first - 1))
  
  for char in word[1:]: # runs in n * (b1 + b2 + ... + bn)
    new_char = ord(char) - prev_char
    while new_char not in range(97, 123): # run b times
      new_char += 26
    res.append(chr(new_char))
    prev_char += new_char

  return res


# space complexity-> O(n)
# time complexity-> O(n * b)