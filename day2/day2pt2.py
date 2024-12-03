# Open the file in read mode
with open('day2.txt', 'r') as file:
  # Read the contents of the file
  data = file.read()

# Print the contents of the file
data = data.split("\n")
for i in range(0, len(data)):
  data[i] = list(map(int, data[i].split()))
#print(data)

# check if they are all decreasing
def is_decreasing(sequence):
  return all(sequence[i] > sequence[i + 1] for i in range(len(sequence) - 1))

# check if they are all increasing
def is_increasing(sequence):
  return all(sequence[i] < sequence[i + 1] for i in range(len(sequence) - 1))

safe_count = 0

# use this function for rows we already know are all increasing or all decreasing
def check_only_difference(numbers):
  removals = 0
  problems = []
  for i in range(1, len(numbers)):
    difference = abs(numbers[i] - numbers[i-1])
    # if there is a problematic difference between two numbers
    if (difference < 1 or difference > 3):
      # if we've already removed a number, we can't remove another one
      if (removals == 1): 
        return 0
      # now check if removing the current number would make this row safe
      if (i == len(numbers) - 1):
        return 1 # we can just pop if it's the last index
      else: 
        new_dist = abs(numbers[i+1] - numbers[i-1])
        # if removing the bad number still doesn't make the row safe
        if (new_dist < 1 or new_dist > 3):
          return 0
        # if the row is now safe
        removals += 1
        problems.append(numbers[i])
  # if (removals > 0):
  #   print(removals, problems)
  return 1

# use this to immediately disqualify some rows
def how_many_duplicates(numbers):
  set_length = len(set(numbers))
  return len(numbers) - set_length

# this is for rows that have an outlier that's been removed already so we can't have another
def strict_difference(numbers):
  for i in range(1, len(numbers)):
    difference = abs(numbers[i] - numbers[i-1])
    if (difference < 1 or difference > 3):
      return 0
  return 1

def find_outliers(arr):
  n = len(arr)
  outliers = []
  for i in range(n):
    # Create a new sequence without the i-th element
    test_sequence = arr[:i] + arr[i + 1:]
    # print('the row without ', arr[i], 'is', test_sequence)
    if is_increasing(test_sequence) or is_decreasing(test_sequence):
      outliers.append([i, test_sequence])
  # print(outliers)
  return outliers


# need flow for rows with all increasing/decreasing where we only need to check for difference

def count_safe(rows):
  safe = 0
  # loop through rows
  # call function that will return either 1 or 0 if the row is safe
  for row in rows:
    value = check_safety(row) 
    safe += value
    print(row, 'the value is', value)
    print()
  print(safe)


def check_safety(row):
  # if there is more than 1 set of duplicates, the row can never be safe
  if (how_many_duplicates(row) > 1):
    return 0
  # if we know that all numbers are unique and either increasing or decreasing, we just need to check the difference between numbers
  elif (is_increasing(row) or is_decreasing(row)):
    return check_only_difference(row)
  # if we know there is at least one set of duplicate values
  elif (how_many_duplicates(row) == 1):
    return check_only_difference(row)
  # if there are no duplicate values, but we know the row is not all increasing or decreasing
  # find outlier(s)
  else: 
    outliers = find_outliers(row)
    if (len(outliers) == 0):
      return 0
    else:
      return strict_difference(outliers[0][1])

count_safe(data)

# for row in data:
#   if (too_many_duplicates(row) == 0):
#     return
#   direction = check_trend(row)
#   if (direction != 'invalid'):
#     print(row, 'is valid')
#     difference = check_difference(row)
#     safe_count += difference
#   elif (direction == 'invalid'):
#     print('need to check if row can have number removed so all values are increasing/decreasing', row)
#     if (too_many_duplicates(row) == 0):
#       safe_count+=0
#     elif (too_many_duplicates(row) != 0):
#       index = find_first_outlier(row)
#       print(row[index], index, 'is the first outlier we need to check')
#       if (index == len(row)-1):
#         safe_count += 1
#       else:
#         safe_count+= strict_difference(row[index+1], row[index-1])
    # for i in range(len(row)):
    #   test_sequence = row[:i] + row[i + 1:]
    #   if is_increasing(test_sequence) or is_decreasing(test_sequence):
    #     print(row[i], 'is the outlier')
        

        

# print(safe_count)