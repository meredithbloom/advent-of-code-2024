# Open the file in read mode
with open('day2.txt', 'r') as file:
  # Read the contents of the file
  data = file.read()

# Print the contents of the file
data = data.split("\n")
for i in range(0, len(data)):
  data[i] = list(map(int, data[i].split()))
# print(data)

safe_count = 0

def is_increasing(numbers):
  # print(numbers)
  for i in range(1, len(numbers)):
    difference = abs(numbers[i] - numbers[i-1])
    if numbers[i] < numbers[i-1]:
      return False
    if (difference < 1 or difference > 3):
      return False
  return True

def is_decreasing(numbers):
  # print(numbers)
  for i in range(1, len(numbers)):
    difference = abs(numbers[i] - numbers[i-1])
    if numbers[i] > numbers[i-1]:
      return False
    if (difference < 1 or difference > 3):
      return False
  return True

def check_direction(numbers):
  if numbers[0] < numbers[1]:
    direction = 'up'
  elif numbers[0] > numbers[1]:
    direction = 'down'
  else: 
    return False
  return direction

for row in data:
  if check_direction(row) == 'up':
    if (is_increasing(row) == True):
      print(row, 'is safe')
      safe_count+=1
  elif check_direction(row) == 'down':
    if (is_decreasing(row) == True):
      print(row, 'is safe')
      safe_count+=1

print(safe_count)