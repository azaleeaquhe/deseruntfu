dict1 = {'one': 1, 'two': 2, 'three': 3}
dict2 = {'four': 4, 'five': 5}
# Update dict1 with the data in dict2
dict1 |= dict2
print(dict1)  # Output: {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
