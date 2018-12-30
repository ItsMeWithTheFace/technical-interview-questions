# Given a text find the number of occurrences of each word
# You need to strip out special characters in the result and
# if multiple words have the same occurrence, order them by
# their occurrence in the text

import re

# linear time, make multiple passthroughs, counting occurrences
# and using bucket sort to order things properly
# terrible space complexity
def word_count_engine(document):
  words = list(filter(None, document.split(' ')))
  unique_words = []
  counts = dict()
  res = []
  biggest_count = 0
  
  # get all the counts of each word, clean and keep track of order of occurrences
  for word in words:
    cleaned_word = re.sub('[^a-z]', '', word.lower())
    if cleaned_word not in counts.keys():
      counts[cleaned_word] = 1
      unique_words.append(cleaned_word)
    else:
      counts[cleaned_word] += 1
      if counts[cleaned_word] > biggest_count:
        biggest_count = counts[cleaned_word]
  
  # using bucket sort for linear time, add words in respective count buckets
  word_freq = [None] * (biggest_count + 1)
  for word in unique_words:
    count = counts[word]
    bucket = word_freq[count]
    
    if bucket == None:
      bucket = []
    bucket.append(word)
    word_freq[count] = bucket

  # go backwards (highest freq elements) and go through each bucket in order
  for j in range(len(word_freq) - 1, 0, -1):
    bucket = word_freq[j]
    if bucket is not None:
      for word in bucket:
        res.append([word, str(counts[word])])
  return res
