n = int(input("Enter number of strings: "))

strs = []

for i in range(n):
    strs.append(input("Enter string: "))

prefix = strs[0]

for word in strs:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print("Longest Common Prefix:", prefix)