test_phone_strs = [
    "Call me at 123-456-7890 or 9876543210",
    "My numbers are one two three four five six seven eight nine zero",
    "Here's another format: (123) 456-7890"
]

test_expected_strs = [
    ["1234567890", "9876543210"],
    ["1234567890"],
    ["1234567890"]
]

s = '''
   Hello here's a random number 323-4321234blah
   crap formatting 3 21318 3068 and many other features
   for example 4six1-213-fivenine83
'''

expected_nums = [
    '3234321234',
    '3213183068',
    '4612135983'
]
