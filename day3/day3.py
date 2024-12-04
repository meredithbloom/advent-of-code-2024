import re

# Open the file in read mode
with open('day3.txt', 'r') as file:
  # Read the contents of the file
  data = file.read()


#print(data)


pattern1 = r'mul\(\d+,\d+\)'

matches = re.findall(pattern1, data)
pattern2 = r'(\d+)'

total = 0

def mul(x,y):
  return x*y

for match in matches:
  m = re.findall(pattern2, match)
  c = list(map(lambda v: int(v), m))
  to_add = mul(c[0], c[1])
  # print(to_add)
  total += to_add

print(total)