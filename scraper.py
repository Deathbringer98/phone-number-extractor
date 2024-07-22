"""
Formats:
xxx xxx xxxx
xxx-xxx-xxxx
(xxx) xxx-xxxx
xxxxxxxxxx
"""

import re

NUM_WORDS = [
    'zero', 'one', 'two', 'three', 'four', 'five',
    'six', 'seven', 'eight', 'nine'
]

WORD_TO_DIGIT = {word: str(index) for index, word in enumerate(NUM_WORDS)}

SPECIAL_NUMS_1 = "0➊➋➌➍➎➏➐➑➒➓"
SPECIAL_NUMS_2 = "0⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾"

SPECIAL_NUM_MAP = {
    '①': 1, '➊': 1, '❶': 1,
    '➋': 2, '❷': 2, '②': 2,
    '③': 3,
    '➍': 4, '④': 4,
    '⑤': 5,
    '⑥': 6,
    '⑦': 7, '➆': 7,
    '⑨': 9
}

def word_to_digit_string(s: str) -> str:
    words = s.split()
    return ''.join(WORD_TO_DIGIT.get(word.lower(), '') for word in words if word.lower() in WORD_TO_DIGIT)

def extract_phone_numbers(s: str) -> list[str]:
    # First, extract sequences of digits possibly separated by spaces, hyphens, or parentheses
    pattern = re.compile(r'(\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4})')
    matches = pattern.findall(s)
    cleaned_numbers = []

    for match in matches:
        digits = re.sub(r'\D', '', match)
        if len(digits) == 10:
            cleaned_numbers.append(digits)

    # Next, extract numbers from sequences of words
    word_matches = re.findall(r'([a-zA-Z]+(?:\s+[a-zA-Z]+)*)', s)
    for match in word_matches:
        digit_str = word_to_digit_string(match)
        if len(digit_str) == 10:
            cleaned_numbers.append(digit_str)

    return cleaned_numbers

def get_all_nums(s: str) -> list[str]:
    nums = extract_phone_numbers(s)
    return nums
