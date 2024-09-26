# ------------------------------------------------------------------------

# Lab 1
# Problem 1
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.
my_list = [1, 5, 'apple', 20.5]
# Problem 2
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.
print(my_list[2])
# Problem 3
my_list.append(10)
print(my_list)
# Problem 4
my_list.remove(20.5) 
print(my_list)
# Problem 5
my_list.reverse()
print(my_list)

# Lab 2
# Problem 1
person = {
     'name': 'John',
     'age': 30,
     'job': 'teacher'
}
# Problem 2
print(person['job'])
# Problem 3
person['city'] = "Paris"
print(person['job'])
# Problem 4
del person['age']
print(person)
# Problem 5
for key, value in person.items():
    print(f'{key}: {value}')
# -----------------------------------------------------------------------------


# Importing sys for test function
import sys


# Custom Test Function
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    msg = f"Test at line {linenum} {'PASSED' if did_pass else 'FAILED'}."
    print(msg)


# Function 1: count_vowels
def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a string.

    Parameters:
    - s (str): The input string

    Returns:
    - int: The number of vowels in the string
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

    # TODO: Implement this function



# Unit Tests for count_vowels
def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)


# Function 2: merge_lists
def merge_lists(list1: list, list2: list) -> list:
    """
    Merge two sorted lists into a single sorted list.

    Parameters:
    - list1 (list): The first sorted list
    - list2 (list): The second sorted list

    Returns:
    - list: A new sorted list containing all elements from list1 and list2
    """
    # for loop
    
    how_many_times = len(list1) + len(list2) 
    merged_list = [0]*how_many_times
    index1 = 0
    index2 = 0
    while len(merged_list) != how_many_times:
        if list1 == []:
            for n in list2 : merged_list.append(n)
        if list2 == []:
            for n in list1 : merged_list.append(n)
            return add_remaining_items_to_merged_list(index2, list1, merged_list) # type: ignore
        if list1[index1] < list2[index2]:
            merged_list[index1+index2] = list1[index1]
            index1 += 1
        else:
            merged_list[index1+index2] = list2[index2]
            index2 += 1
    print(merged_list)
    return merged_list
    # TODO: Implement this function
    pass


# Unit Tests for merge_lists
def test_merge_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merge_lists(list1, list2)
    test(merged == [1, 2, 3, 4, 5, 6])
    test(merge_lists([], []) == [])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merge_lists([1, 3, 5], []) == [1, 3, 5])
    test(merge_lists([], [2, 4, 6]) == [2, 4, 6])
    test(merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merge_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])


# Function 3: word_lengths
def word_lengths(words: list) -> list:
    """
    Get the lengths of words in a list.

    Parameters:
    - words (list): The list of words

    Returns:
    - list: A list containing the lengths of the words
    """
 
    return [len(word) for word in words]
    
    # TODO: Implement this function
      
    pass


# Unit Tests for word_lengths
def test_word_lengths():
    words = ["hello", "world", "python"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 10])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])


# Function 4: reverse_string
# def reverse_string(s: str) -> str:
    """
    Reverse a string.

    Parameters:
    - s (str): The input string

    Returns:
    - str: The reversed string
    """
def reverse_string(s: str) -> str:
    return s[::-1]
    # TODO: Implement this function
    pass


# Unit Tests for reverse_string
def test_reverse_string(): 
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")


# Function 5: intersection
def intersection(list1: list, list2: list) -> list:
    """
    Find the intersection of two lists.

    Parameters:
    - list1 (list): The first list
    - list2 (list): The second list

    Returns:
    - list: The intersection of the two lists
    """
    # step 0: create an intersection list
    intersection_list = []
    # step 1: pick a list
    # step 2: iterate over the list 
    for number in list1:
        # step 3 : for each item check if it is in the other list
        if number in list2: 
        # step 4: if it is add it into the other intersection list, oh wait, we need that, let's add a step 0
            intersection_list.append(number)
    intersection_list = list(set(intersection_list))
    return intersection_list
# step 5: return the intersection list 
# step 6: how did we remove duplicates?
    
    # TODO: Implement this function
    pass 

# Unit Tests for intersection
def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])


# Test Suite
def test_suite():
    print(f"Count Vowels Test Results:")
    test_count_vowels()
    print(f"Merge Lists Test Results:")
    test_merge_lists()
    print(f"Word Lengths Test Results:")
    test_word_lengths()
    print(f"Reverse String Test Results:")
    test_reverse_string()
    print(f"Intersection Test Results:")
    test_intersection()


test_suite()
