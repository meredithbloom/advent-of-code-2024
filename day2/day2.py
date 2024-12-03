# Open the file in read mode
with open('day2.txt', 'r') as file:
  # Read the contents of the file
  data = file.read()

# Print the contents of the file
data = data.split("\n")
for i in range(0, len(data)):
  data[i] = list(map(int, data[i].split()))
# print(data)

def has_duplicates(row):
  return len(row) != len(set(row))

safe_count = 0

def is_increasing(numbers):
  # print(numbers)
  unsafe = 0
  for i in range(1, len(numbers)):
    difference = abs(numbers[i] - numbers[i-1])
    if numbers[i] == numbers[i-1]:
      print(numbers[i], numbers[i-1])
      unsafe+=1
    elif (difference < 1 or difference > 3):
      unsafe+=1
  if (unsafe > 1):
    return False
  return True

def is_decreasing(numbers):
  # print(numbers)
  unsafe = 0
  for i in range(1, len(numbers)):
    difference = abs(numbers[i] - numbers[i-1])
    if numbers[i] == numbers[i-1]:
      print(numbers[i], numbers[i-1])
      unsafe+=1
    elif (difference < 1 or difference > 3):
      unsafe+=1
  if (unsafe > 1):
    print(numbers, 'is too unsafe', unsafe)
    return False
  return True

def check_trend(arr):
  if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
    # print(arr, 'is increasing')
    return 'up'
  elif all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)):
    # print(arr, 'is decreasing')
    return 'down'
  else:
    print(arr, 'is invalid')
    return 'invalid'


def check_direction(numbers):
  if numbers[0] < numbers[1]:
    direction = 'up'
  elif numbers[0] > numbers[1]:
    direction = 'down'
  else:
    direction = check_trend(numbers)
    # print(direction)
  return direction

invalid_count = 0
for row in data:
  direction = check_trend(row)
  # print(direction)
  if direction == 'up':
    if (is_increasing(row) == True):
      # print(row, 'is safe')
      safe_count+=1
  elif direction == 'down':
    if (is_decreasing(row) == True):
      # print(row, 'is safe')
      safe_count+=1
  elif direction == 'invalid':
    invalid_count+=1

print(len(data))
print(invalid_count)
print(safe_count)