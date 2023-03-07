Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl'

# Paste your code into this box 
counter = 0
for i in range(len(s)):
    if s[i] == 'b':
        if i+1 < len(s) and i+2 < len(s):
            if s[i+1] == 'o' and s[i+2] == 'b':
                counter += 1
print("Number of times bob occurs is: " + str(counter))
