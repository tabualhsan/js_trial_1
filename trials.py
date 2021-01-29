"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    pass  # TODO: replace this line with your code
    for item in items:
        print(item)


def get_all_evens(nums):
    pass  # TODO: replace this line with your code 
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums



def get_odd_indices(items):
    pass  # TODO: replace this line with your code
    result =[]
    for idx in range(len(items)):
        if idx % 2 != 0:
            result.append(items[idx])
    return result


def get_odd_indices_enum(items):
    result = []
    for i, item in enumerate(items):
        print(f"i is {i}, item is {item}")
        if i % 2 != 0:
            result.append(item)

    return result


def print_as_numbered_list(items):
    pass  # TODO: replace this line with your code
    i = 1 
    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    pass  # TODO: replace this line with your code
    nums = []

    for i in range(start,stop):
        nums.append(i)
    return nums

# def get_range_while(start, stop):
    # num = start
    # while num < stop:
    #     nums.append(num)
    #     num += 1

def get_range_while_true(start, stop):
    counter = start
    nums = []
    while True:
        if counter == stop:
            break 
        else:
            nums.append(counter)
            counter += 1
           
    return nums
    

def censor_vowels(word):
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
