# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.

# Paste your code into this box 
alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = []

for i in s:
  numbers.append(alphabet.index(i))
  
highest_count = 0
current_count = 0
highest_arrangement = []
current_arrangement = []
for i in range(len(numbers)):
  for j in range(i+1, len(numbers)):
    if numbers[j] >= numbers[i]:
      current_count += 1
      if current_count == 1:
        current_arrangement.append(alphabet[numbers[i]])
      current_arrangement.append(alphabet[numbers[j]]) 
      break
    else:
      if current_count > highest_count:
        highest_count = current_count
        highest_arrangement = current_arrangement
      current_count = 0
      current_arrangement = []
      break

if current_count > highest_count:
  highest_count = current_count
  highest_arrangement = current_arrangement
current_count = 0
current_arrangement = []

if highest_count == 0:
  highest_arrangement.append(alphabet[numbers[0]])

highest_arrangement_string = ''.join(highest_arrangement)
print("Longest substring in alphabetical order is: " + highest_arrangement_string)
