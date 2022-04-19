"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(items)


def get_all_evens(nums):

    evenNums = []

    for num in nums:
        if num % 2 == 0:
            evenNums.append(num)

    return evenNums



def get_odd_indices(items):
    
    result = []

    for i, item in enumerate(items):
        if i % 2 == 0:
            result.append(item[i])
    
    return result


def print_as_numbered_list(items):
    
    for i, item in enumerate(items):
        print(f"{i}. {item}")


def get_range(start, stop):
    
    nums = []

    for i in range(1, 3):
        nums.append(i)
    
    return nums

    # # Alternate method
    # return list(range(start, stop))


def censor_vowels(word):
    
    censored = []

    for letter in word:
        if letter in "aeiou":
            censored.append("*")
        else:
            censored.append(letter)
    
    return "".join(censored)


def snake_to_camel(string):
    
    camel_case = []

    for word in string.split("_"):
        camel_case.append(word.capitalize())
    
    return "".join(camel_case)


def longest_word_length(words):
    
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    
    return longest


def truncate(string):
    
    result = []

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)
    
    return "".join(result)


def has_balanced_parens(string):
    
    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
        
        if parens < 0:
            return False
    
    return parens == 0


def compress(string):
    
    compressed = []

    last_char = ""

    last_char_count = 0

    for char in string:
        if char != last_char:

            if last_char_count > 1:
                compressed.append(str(last_char_count))

            compressed.append(char)
            
            last_char = char
            last_char_count = 1
        else:
            last_char_count += 1
    

    if last_char_count > 1:
        compressed.append(str(last_char_count))
    
    return "".join(compressed)

