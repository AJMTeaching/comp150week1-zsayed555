# week 1: Introduction to Data Structures in Python

## Introduction

Welcome to week 1 of COMP150! This week, we are diving into two of the cornerstones of Python programming: data structures and algorithms. A data structure is a way of organizing and storing data so that it can be accessed and modified efficiently. An algorithm is a sequence of steps used to solve a problem. Understanding when to use which data structures is crucial for writing efficient and well-organized code.

In Python, there are both linear and non-linear types of data structures:

### Linear Data Structures
1. **Strings**: Immutable sequences of characters.
2. **Lists**: Ordered, mutable collections that allow duplicates.
3. **Tuples**: Ordered, immutable collections that allow duplicates.

### Non-Linear Data Structures
1. **Dictionaries**: Unordered collections of key-value pairs that are mutable.
2. **Sets**: Unordered collections that are mutable but do not allow duplicate elements.

Let's explore each of these data structures in more detail, focusing on their characteristics, common use-cases, and how to work with them.

---

## Linear Data Types

### Strings

#### Characteristics:

- **Immutable**: Once created, individual elements cannot be changed.
- **Ordered**: Characters have a defined sequence.

#### Common Uses:

- Text representation and manipulation.

#### Example:

```python
example_string = "Hello, World!"
first_char = example_string[0]  # 'H'
```

### Lists

#### Characteristics:

- **Ordered**: Elements have a defined order that will not change unless you explicitly change them.
- **Mutable**: Elements can be added, removed, or changed.
- **Allow Duplicates**: Multiple identical elements can exist.

#### Common Uses:

- Storing ordered data like scores, names, or coordinates.
- When you need to add, remove, or change elements frequently.

#### Example:

```python
example_list = [1, 2, 3, 4, 5]
example_list[0] = 0  # [0, 2, 3, 4, 5]
```

### Tuples

#### Characteristics:

- **Ordered**: Elements have a defined order that will not change.
- **Immutable**: Elements cannot be added, removed, or changed after the tuple is created.
- **Allow Duplicates**: Multiple identical elements can exist.

#### Common Uses:

- Storing data that should not be changed, like coordinates or RGB color values.
- Using as keys for dictionaries, as they are hashable and immutable.

#### Example:

```python
example_tuple = (1, 2, 3, 4, 5)
# example_tuple[0] = 0  # TypeError
```

---

## Non-Linear Data Types

### Sets

#### Characteristics:

- **Unordered**: The order of elements is not guaranteed.
- **Mutable**: Elements can be added or removed.
- **No Duplicates**: All elements must be unique.

#### Common Uses:

- Removing duplicates from a collection.
- Membership testing, to quickly check if an element exists in a collection.

#### Example:

```python
example_set = {1, 2, 3, 4, 5}
example_set.add(6)  # {1, 2, 3, 4, 5, 6}
```

### Dictionaries

#### Characteristics:

- **Unordered**: The order of the elements is not guaranteed.
- **Mutable**: Elements (key-value pairs) can be added, removed, or changed.
- **Keys Must Be Unique**: Each key must be unique.

#### Common Uses:

- Storing data in key-value pairs, like a phone book or a glossary.
- Caching or memoization, to quickly look up precomputed values.

#### Example:

```python
example_dict = {'key1': 'value1', 'key2': 'value2'}
example_dict['key1'] = 'new_value1'  # {'key1': 'new_value1', 'key2': 'value2'}
```
---

# week 1: Diving Deeper into Lists

## Introduction to Lists

In this section, we'll delve deeper into one of Python's most commonly used data structures: lists. Understanding lists is crucial in Python programming.

### Characteristics of Lists:

Lists in Python are ordered, mutable collections that allow duplicate elements.

---

## Creating Lists

Creating a list is straightforward. You can initialize an empty list or one with initial values.

```python
# Creating an empty list
empty_list = []

# Creating a list with initial values
initial_values_list = [1, 2, 3, "hello", True]
```

---

## General Uses of Lists

Lists are versatile and have a variety of uses, including:

- **Data Collection**: Storing survey responses, test scores, etc.
- **Data Analysis**: Sorting, filtering, or manipulating data.

---

## Common Operations on Lists

Here are some common operations that you can perform on lists:

### 1. Adding Elements

You can add elements to a list using methods like `append()`, `insert()`, and `extend()`.

### 2. Removing Elements

Elements can be removed using methods like `remove()`, `pop()`, and `clear()`.

### 3. Accessing Elements

You can access elements by index, and you can also use slicing to get multiple elements.

### 4. Searching for Elements

The `index()` method can be used to find the index of an element.

### 5. Other Operations

You can also sort a list, reverse it, and find its length.

Let's dive into some example functions that demonstrate these operations:

### Code Example:

```python
1   def add_elements(lst: list[int]) -> list[int]:
2       """Adding elements to the list."""
3       lst.append(10)
4       lst.insert(0, 0)
5       lst.extend([11, 12, 13])
6       return lst

7   def remove_elements(lst: list[int]) -> list[int]:
8       """Removing elements from the list."""
9       lst.remove(10)
10      if 99 in lst:
11          lst.remove(99)
12      lst.pop(0)
13      lst.clear()
14      return lst

15  def access_elements(lst: list[int]) -> list[int]:
16      """Accessing elements in the list."""
17      first_element = lst[0]
18      last_element = lst[-1]
19      sliced_lst = lst[1:4]
20      return [first_element, last_element, sliced_lst]

21  def search_elements(lst: list[int]) -> int:
22      """Searching for an element in the list."""
23      if 10 in lst:
24          return lst.index(10)
25      else:
26          return -1

27  def other_operations(lst: list[int]) -> tuple:
28      """Other common operations."""
29      lst.sort()
30      lst.reverse()
31      length = len(lst)
32      return (lst, length)
```

### Line-by-Line Explanation:

1. **Line 1-6**: `add_elements` function demonstrates how to add elements to a list. It uses `append()` to add an element at the end, `insert()` to add an element at a specific index, and `extend()` to add multiple elements.

2. **Line 7-14**: `remove_elements` function shows how to remove elements. It uses `remove()` to remove a specific element, `pop()` to remove an element by its index, and `clear()` to remove all elements.

3. **Line 15-20**: `access_elements` function shows how to access elements by their index and how to slice a list to get multiple elements.

4. **Line 21-26**: `search_elements` function demonstrates how to search for an element and find its index using `index()`.

5. **Line 27-32**: `other_operations` function performs other common operations like sorting the list using `sort()`, reversing it using `reverse()`, and finding its length using `len()`.

---

Your current section on lists is comprehensive and well-organized. To continue in the same vein, how about we add some example usage of these functions along with unit tests? This will help students understand not only how these functions work but also how to test their code.

Here's how you can extend the existing text:

---

### Example Usage and Unit Tests:
As we saw in week 0, understanding how to test your code is crucial in programming. Below are some example usages of the functions we defined, along with some unit tests to ensure they work as expected. In this case, we're using the unittest library which just defines the `assertEqual` function which just checks in the two arguments to the function are the same.

#### Example Usage:

```python
# Example usage of add_elements function
print(add_elements([1, 2, 3]))  # Output should be [0, 1, 2, 3, 10, 11, 12, 13]

# Example usage of remove_elements function
print(remove_elements([10, 0, 1]))  # Output should be []

# Example usage of access_elements function
print(access_elements([1, 2, 3, 4]))  # Output should be [1, 4, [2, 3]]

# Example usage of search_elements function
print(search_elements([1, 10, 3]))  # Output should be 1

# Example usage of other_operations function
print(other_operations([3, 2, 1]))  # Output should be ([3, 2, 1], 3)
```

#### Unit Tests:

```python
import unittest

class TestListFunctions(unittest.TestCase):
    
    def test_add_elements(self):
        self.assertEqual(add_elements([1, 2, 3]), [0, 1, 2, 3, 10, 11, 12, 13])
        
    def test_remove_elements(self):
        self.assertEqual(remove_elements([10, 0, 1]), [])
        self.assertEqual(remove_elements([99, 10, 0]), [])
        
    def test_access_elements(self):
        self.assertEqual(access_elements([1, 2, 3, 4]), [1, 4, [2, 3]])
        
    def test_search_elements(self):
        self.assertEqual(search_elements([1, 10, 3]), 1)
        self.assertEqual(search_elements([1, 2, 3]), -1)
        
    def test_other_operations(self):
        self.assertEqual(other_operations([3, 2, 1]), ([3, 2, 1], 3))

if __name__ == "__main__":
    unittest.main()
```

---

By using these unit tests, we can easily verify that our functions behave as expected for the given inputs. This is a best practice that helps you ensure the reliability of your code.

---

### Questions:

1. What are the three main characteristics of a list in Python?
2. How do you create an empty list?
3. Name two general uses for lists.
4. What method would you use to add an element to the end of a list?
5. How do you remove a specific element from a list?
6. What is slicing in the context of lists?
7. How can you find the index of a specific element in a list?
8. What does the `clear()` method do to a list?
9. Can a list contain elements of different data types?
10. What would be the output of the `access_elements` function if passed `[1, 2, 3, 4]` as an argument?

---

### Questions and Answers:

1. **What are the three main characteristics of a list in Python?**
    - Answer: The three main characteristics of a list in Python are that it is ordered, mutable, and allows duplicates.

2. **How do you create an empty list?**
    - Answer: You can create an empty list by using empty square brackets: `[]`.

3. **Name two general uses for lists.**
    - Answer: Two general uses for lists are data collection, such as storing survey responses, and data analysis, where you might sort, filter, or manipulate data.

4. **What method would you use to add an element to the end of a list?**
    - Answer: You would use the `append()` method to add an element to the end of a list.

5. **How do you remove a specific element from a list?**
    - Answer: You can use the `remove()` method to remove a specific element from a list.

6. **What is slicing in the context of lists?**
    - Answer: Slicing is used to access a specific range of elements in a list. It is done by specifying the start and end indices separated by a colon, like this: `list[start:end]`.

7. **How can you find the index of a specific element in a list?**
    - Answer: You can use the `index()` method to find the index of a specific element in a list.

8. **What does the `clear()` method do to a list?**
    - Answer: The `clear()` method removes all elements from a list, making it empty.

9. **Can a list contain elements of different data types?**
    - Answer: Yes, a list can contain elements of different data types, including integers, strings, and booleans.

10. **What would be the output of the `access_elements` function if passed `[1, 2, 3, 4]` as an argument?**
    - Answer: The output would be `[1, 4, [2, 3]]` as it returns the first element, the last element, and a slice from index 1 to 3.

---

# week 1: Lists vs Strings - A Comparative Analysis

## Introduction

While we've focused on lists so far, you may have noticed that some of the operations on lists look familiar. That's because Python strings and lists share several similarities, but they also have key differences. Understanding these can help you decide when to use a list and when a string would be more appropriate.

## Similarities between Lists and Strings

### 1. Ordered Collections

Both lists and strings are ordered collections, meaning the elements have a specific order that is maintained.

**List Example**: `[1, 2, 3]`

**String Example**: `"abc"`

### 2. Indexing

You can access individual elements of both strings and lists using indexing.

**List Example**:

```python
my_list = [1, 2, 3]
print(my_list[0])  # Output: 1
```

**String Example**:

```python
my_string = "abc"
print(my_string[0])  # Output: 'a'
```

### 3. Slicing

Both lists and strings can be sliced to create new lists or strings.

**List Example**:

```python
my_list = [1, 2, 3]
print(my_list[0:2])  # Output: [1, 2]
```

**String Example**:

```python
my_string = "abc"
print(my_string[0:2])  # Output: 'ab'
```

## Differences between Lists and Strings

### 1. Mutability

**Lists are mutable**, meaning you can modify their elements.

```python
my_list[0] = 10  # Valid
```

**Strings are immutable**, meaning once a string is created, you cannot change its elements.

```python
my_string[0] = 'z'  # TypeError
```

### 2. Element Types

**Lists can store multiple data types**, including other lists.

```python
my_list = [1, 'a', [2, 3]]
```

**Strings can only contain characters**.

```python
my_string = "abc"  # All elements must be characters
```

### 3. Methods

While both lists and strings have a variety of useful methods, **lists have methods for adding or removing elements**, such as `append()`, `insert()`, and `remove()`, which strings lack due to their immutability.

**List Example**:

```python
my_list.append(4)
```

**String Example**:

```python
# Strings don't have append() method
```

### 4. Concatenation and Repetition

Both lists and strings support concatenation and repetition, but **lists use methods like `extend()` for multiple-element concatenation**.

**List Example**:

```python
my_list.extend([5, 6, 7])
```

**String Example**:

```python
new_string = my_string + "def"
```

---

Understanding the similarities and differences between lists and strings can help you make more informed decisions when writing Python programs.

Certainly! Let's create a set of questions that delve into the similarities and differences between lists and strings, helping students to solidify their understanding of when to use each. After that, I'll provide the corresponding answers.

---

### Questions:

1. What is a common feature between lists and strings regarding the order of their elements?
2. How do you access the first element of a list and a string?
3. Can you slice a string the same way you slice a list? Give an example.
4. What is a key difference between lists and strings concerning mutability?
5. Can a list contain elements of different data types? What about a string?
6. Name a method that is available for lists but not for strings.
7. How would you concatenate multiple elements to a list?
8. How would you concatenate additional characters to a string?
9. What happens if you try to change an individual character in a string?
10. Why might you choose a list over a string for certain operations?

---

### Questions and Answers:

1. **What is a common feature between lists and strings regarding the order of their elements?**
    - Answer: Both lists and strings are ordered collections, meaning the elements have a specific order that is maintained.

2. **How do you access the first element of a list and a string?**
    - Answer: You can access the first element of a list using `list[0]` and the first character of a string using `string[0]`.

3. **Can you slice a string the same way you slice a list? Give an example.**
    - Answer: Yes, you can slice both strings and lists using the same syntax. For example, `my_list[0:2]` will give `[1, 2]`, and `my_string[0:2]` will give `'ab'`.

4. **What is a key difference between lists and strings concerning mutability?**
    - Answer: Lists are mutable, meaning you can modify their elements, while strings are immutable, so you cannot change their elements once created.

5. **Can a list contain elements of different data types? What about a string?**
    - Answer: A list can contain elements of different data types, including other lists. A string can only contain characters.

6. **Name a method that is available for lists but not for strings.**
    - Answer: Methods like `append()`, `insert()`, and `remove()` are available for lists but not for strings.

7. **How would you concatenate multiple elements to a list?**
    - Answer: You can concatenate multiple elements to a list using the `extend()` method.

8. **How would you concatenate additional characters to a string?**
    - Answer: You can concatenate additional characters to a string using the `+` operator, like `new_string = my_string + "def"`.

9. **What happens if you try to change an individual character in a string?**
    - Answer: If you try to change an individual character in a string, you'll get a `TypeError` because strings are immutable.

10. **Why might you choose a list over a string for certain operations?**
    - Answer: You might choose a list over a string when you need a collection that is mutable, when you need to store elements of different data types, or when you need to frequently add or remove items.

---

Certainly! The `split()` and `join()` methods are powerful tools for manipulating strings and lists in Python. They're particularly useful for breaking down strings into list components, applying list manipulations, and then reassembling them back into strings. Here's how you could structure a section on these topics:

---

# week 1: Working with `split()` and `join()`

## Introduction

When working with strings, there are scenarios where you'll find it easier to convert the string into a list, manipulate it, and then convert it back into a string. Python provides two convenient methods, `split()` and `join()`, which make these operations straightforward.

## The `split()` Method

### Description:

The `split()` method divides a string into a list where each word is a separate element.

### Syntax:

```python
string.split(separator, maxsplit)
```

- **separator**: (Optional) The delimiter on which to split the string. Default is whitespace.
- **maxsplit**: (Optional) The maximum number of splits. Default is `-1`, which means "all occurrences."

### Example:

```python
text = "apple banana cherry"
list_of_words = text.split(" ")
print(list_of_words)  # Output: ['apple', 'banana', 'cherry']
```

## The `join()` Method

### Description:

The `join()` method takes a list of strings and concatenates its elements into a single string separated by a specified character.

### Syntax:

```python
separator.join(list)
```

### Example:

```python
list_of_words = ['apple', 'banana', 'cherry']
text = " ".join(list_of_words)
print(text)  # Output: 'apple banana cherry'
```

## A Practical Example: `split()` then `join()`

Sometimes you might want to split a string, perform some operations on the list, and then join it back into a string.

### Example:

```python
text = "apple banana cherry"
words = text.split(" ")
words.reverse()
reversed_text = " ".join(words)
print(reversed_text)  # Output: 'cherry banana apple'
```

## Other Related Methods

1. **`splitlines()`**: This method splits a string at line breaks and returns a list.
2. **`partition()`**: This method splits a string into a tuple with three elements: the part before the separator, the separator itself, and the part after the separator.

---

### Questions:

1. What is the default separator for the `split()` method?
2. How do you specify a maximum number of splits using `split()`?
3. What does the `join()` method do?
4. Can you use `join()` on a list containing numbers?
5. Describe a scenario where you'd use both `split()` and `join()`.
6. What is the `splitlines()` method used for?
7. How does the `partition()` method differ from `split()`?

---

### Questions and Answers:

1. **What is the default separator for the `split()` method?**
    - Answer: The default separator for the `split()` method is whitespace.

2. **How do you specify a maximum number of splits using `split()`?**
    - Answer: You can specify a maximum number of splits by providing the `maxsplit` parameter. For example, `string.split(" ", 1)` will split the string at the first occurrence of a space.

3. **What does the `join()` method do?**
    - Answer: The `join()` method takes a list of strings and concatenates its elements into a single string, separated by a specified character or string.

4. **Can you use `join()` on a list containing numbers?**
    - Answer: No, the `join()` method only works on lists where all elements are strings. If the list contains numbers, you'd need to convert them to strings first.

5. **Describe a scenario where you'd use both `split()` and `join()`.**
    - Answer: You might use both `split()` and `join()` when you need to manipulate a string by its individual words or characters. For example, you could split a sentence into words, reverse the order of the words, and then join them back together into a new string.

6. **What is the `splitlines()` method used for?**
    - Answer: The `splitlines()` method is used to split a string at line breaks (`\n`) and returns a list of lines in the string.

7. **How does the `partition()` method differ from `split()`?**
    - Answer: The `partition()` method splits a string into a tuple containing three elements: the part before the separator, the separator itself, and the part after the separator. Unlike `split()`, it only splits at the first occurrence of the separator.

---

# week 1: In-Place vs. Non In-Place Operations

## Introduction

As you begin to work with Python lists and other mutable data structures, you'll come across operations that modify the object directly and others that return a new object while leaving the original unchanged. These operations are commonly referred to as "in-place" and "non in-place" operations, respectively.

## What Are In-Place Operations?

### Definition

In-place operations modify the content of the variable directly without creating a new object.

### Characteristics

- **Memory-Efficient**: Since they modify the existing object, they don't require additional memory for a new object.
- **No Return Value**: Typically, in-place methods don't return a new object; they return `None`.

### Common In-Place Operations on Lists

- `append()`
- `extend()`
- `remove()`
- `pop()`
- `sort()`
- `reverse()`

**Example**:

```python
my_list = [1, 2, 3]
my_list.append(4)  # Modifies `my_list` in-place
```

## What Are Non In-Place Operations?

### Definition

Non in-place operations create a new object with the modified content, leaving the original object unchanged.

### Characteristics

- **Memory-Intensive**: Requires additional memory for the new object.
- **Returns New Object**: Always returns a new object.

### Common Non In-Place Operations on Lists

- Slicing
- Concatenation
- Repetition
- Built-in `sorted()` function

**Example**:

```python
my_list = [1, 2, 3]
new_list = my_list + [4]  # Creates a new list, leaves `my_list` unchanged
```

## Why Does This Matter?

Understanding the difference between in-place and non in-place operations is crucial for:

1. **Memory Management**: In-place operations are generally more memory-efficient.
2. **Data Integrity**: In-place operations modify the original data, which may or may not be what you intend.
3. **Debugging**: Knowing whether an operation changes the original object or creates a new one can help in debugging.

---
### Questions for "In-Place vs. Non In-Place Operations":

1. What is the main difference between in-place and non in-place operations?
2. Name two common in-place operations on lists.
3. What is a potential advantage of using in-place operations?
4. Can non in-place operations modify the original list?
---
### Questions and Answers:

#### In-Place vs. Non In-Place Operations:

1. **What is the main difference between in-place and non in-place operations?**
    - Answer: In-place operations modify the original object directly, while non in-place operations create a new object with the modified content and leave the original object unchanged.

2. **Name two common in-place operations on lists.**
    - Answer: Two common in-place operations on lists are `append()` and `sort()`.

3. **What is a potential advantage of using in-place operations?**
    - Answer: One potential advantage of using in-place operations is that they are generally more memory-efficient since they modify the existing object rather than creating a new one.

4. **Can non in-place operations modify the original list?**
    - Answer: No, non in-place operations do not modify the original list; they create a new object with the modified content.
---


Now that you have a good understanding of in-place and non in-place operations, let's explore how this knowledge can be applied to one of the most fundamental programming tasks: sorting.

---

# week 1: Sorting Algorithms and Their Complexities

## Introduction

Sorting is one of the most fundamental problems in computer science. There are various algorithms to sort a list of elements. Each algorithm has its own set of advantages and disadvantages, commonly expressed in terms of time and space complexity.


## Understanding Time and Space Complexity

### Time Complexity

Time complexity is a measure of the amount of computational time taken by an algorithm to run as a function of the size of the input to the program.

- **O(1)**: Constant Time
- **O(log n)**: Logarithmic Time
- **O(n)**: Linear Time
- **O(n^2)**: Quadratic Time

### Space Complexity

Space complexity is a measure of the amount of memory an algorithm uses in relation to the size of the input.

- **O(1)**: Constant Space
- **O(n)**: Linear Space

Understanding these complexities helps you choose the most efficient algorithm for your specific needs.

## Common Sorting Algorithms

### Bubble Sort

- **Time Complexity**: \(O(n^2)\)
- **Space Complexity**: \(O(1)\)
- **In-Place**: Yes
- **Stable**: Yes
- **Description**: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

### Quick Sort

- **Time Complexity**: \(O(n \log n)\) average case, \(O(n^2)\) worst case
- **Space Complexity**: \(O(\log n)\)
- **In-Place**: Yes
- **Stable**: No
- **Description**: Divides the original list into smaller lists and sorts them recursively.

### Merge Sort

- **Time Complexity**: \(O(n \log n)\)
- **Space Complexity**: \(O(n)\)
- **In-Place**: No
- **Stable**: Yes
- **Description**: Divides the original list into smaller lists, sorts them, and then merges them back together.

### Insertion Sort

- **Time Complexity**: \(O(n^2)\)
- **Space Complexity**: \(O(1)\)
- **In-Place**: Yes
- **Stable**: Yes
- **Description**: Builds a sorted array one element at a time by repeatedly removing elements from the input data.

### Selection Sort

- **Time Complexity**: \(O(n^2)\)
- **Space Complexity**: \(O(1)\)
- **In-Place**: Yes
- **Stable**: No
- **Description**: Repeatedly selects the smallest (or largest) element from the unsorted list and puts it at the beginning (or end).

---


### Questions for "Sorting Algorithms and Their Complexities":

5. What is time complexity?
6. How does space complexity differ from time complexity?
7. Name a sorting algorithm that operates in-place.
8. Is Merge Sort an in-place algorithm? Why or why not?
9. Which sorting algorithm would you use if memory usage is a concern?
10. Why is understanding sorting algorithms' complexities important?

---

### Questions and Answers:

#### Sorting Algorithms and Their Complexities:

5. **What is time complexity?**
    - Answer: Time complexity is a measure of the amount of computational time taken by an algorithm to run as a function of the size of the input to the program.

6. **How does space complexity differ from time complexity?**
    - Answer: Space complexity measures the amount of memory an algorithm uses in relation to the size of the input, while time complexity measures the computational time required.

7. **Name a sorting algorithm that operates in-place.**
    - Answer: Bubble Sort is an example of a sorting algorithm that operates in-place.

8. **Is Merge Sort an in-place algorithm? Why or why not?**
    - Answer: No, Merge Sort is not an in-place algorithm because it requires additional memory to create new arrays during the merging process.

9. **Which sorting algorithm would you use if memory usage is a concern?**
    - Answer: If memory usage is a concern, an in-place algorithm like Bubble Sort or Quick Sort would be more appropriate.

10. **Why is understanding sorting algorithms' complexities important?**
    - Answer: Understanding the complexities helps you choose the most efficient algorithm for your specific needs, balancing factors like time efficiency and memory usage.
---

# week 1: Understanding Bubble Sort and Complexity Analysis

## Introduction

In this section, we will use Bubble Sort as a case study to dive deeper into the world of algorithms. We'll go through its algorithmic design, write its pseudocode, implement it in Python, and finally analyze its time and space complexity.

## Algorithm Description

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent items, and swaps them if they are in the wrong order.

## Writing Pseudocode

Pseudocode is a way to plan out your program by writing a high-level description of its logic and operations. Here is the pseudocode for Bubble Sort:

```
1. For each element in the list
    1.1 For each adjacent pair in the list
        1.1.1 If the pair is out of order
            1.1.1.1 Swap them
```

## Python Code Example

Here is a Python code example with more descriptive variable names:

```python
1  def bubble_sort(input_list):
2      """Sorts a list using the Bubble Sort algorithm."""
3      list_length = len(input_list)
4      
5      for outer_index in range(list_length):
6          is_sorted = False
7          
8          for inner_index in range(0, list_length - outer_index - 1):
9              if input_list[inner_index] > input_list[inner_index + 1]:
10                 input_list[inner_index], input_list[inner_index + 1] = input_list[inner_index + 1], input_list[inner_index]
11                 is_sorted = True
12                 
13         if not is_sorted:
14             break
15             
16     return input_list
```

### Line-by-Line Explanation:

1. **Line 1-2**: Define a function `bubble_sort` that takes `input_list` as an argument.
2. **Line 3**: Store the length of `input_list` in `list_length`.
3. **Line 5-6**: Start a for-loop with `outer_index`, initializing `is_sorted` as `False`.
4. **Line 8-11**: Another for-loop with `inner_index` compares and swaps adjacent elements and sets `is_sorted` as `True` if a swap is made.
5. **Line 13-14**: If `is_sorted` remains `False` after a full pass, the list is already sorted, and we break out of the loop.

## Complexity Analysis

### Time Complexity

To determine the time complexity, we look at the number of basic operations in the algorithm. In Bubble Sort, the inner loop runs \(n - i - 1\) times, and the outer loop runs \(n\) times, giving us a time complexity of \(O(n^2)\).

### Space Complexity

Bubble Sort only uses a constant amount of extra memory for variables like `i` and `j`, so its space complexity is \(O(1)\).

---

### Questions:

1. What is pseudocode and why is it useful?
2. How many loops are in the Bubble Sort algorithm?
3. How do you swap two elements in Python?
4. What is the time complexity of Bubble Sort?
5. What is the space complexity of Bubble Sort?
6. Can Bubble Sort be considered efficient in terms of space? Why or why not?
7. How can you determine the time complexity of an algorithm by looking at its code or pseudocode?
---

### Questions and Answers:

#### Understanding Bubble Sort and Complexity Analysis:

1. **What is pseudocode and why is it useful?**
    - Answer: Pseudocode is a high-level description of an algorithm's logic and operations, written in a way that is easier to understand than actual code. It is useful for planning the program's structure and logic before diving into coding, making it easier to implement and debug.

2. **How many loops are in the Bubble Sort algorithm?**
    - Answer: The Bubble Sort algorithm contains two nested loops: an outer loop that iterates through each element in the list and an inner loop that compares adjacent elements.

3. **How do you swap two elements in Python?**
    - Answer: In Python, you can swap two elements `a` and `b` using tuple unpacking: `a, b = b, a`. In the context of a list, you could swap elements at indices `i` and `j` like so: `arr[i], arr[j] = arr[j], arr[i]`.

4. **What is the time complexity of Bubble Sort?**
    - Answer: The time complexity of Bubble Sort is \(O(n^2)\) because it contains two nested loops that iterate through the list.

5. **What is the space complexity of Bubble Sort?**
    - Answer: The space complexity of Bubble Sort is \(O(1)\) because it only uses a constant amount of extra memory for variables.

6. **Can Bubble Sort be considered efficient in terms of space? Why or why not?**
    - Answer: Yes, Bubble Sort can be considered efficient in terms of space because it sorts the list in-place, requiring only a constant amount of additional memory.

7. **How can you determine the time complexity of an algorithm by looking at its code or pseudocode?**
    - Answer: To determine the time complexity, you examine the number of basic operations the algorithm performs in relation to the size of the input. Count the number of nested loops and consider how many times they run; this will often give you a good indication of the algorithm's time complexity.
---
# week 1: Mastering Dictionaries in Python

## Introduction

Dictionaries are one of Python's most versatile data structures. They allow you to store and manage key-value pairs, making it easy to organize and access data efficiently. This section will deepen your understanding of dictionaries, their properties, and common operations.

## Characteristics of Dictionaries:

- **Unordered**: The data in a dictionary doesn't have a specific order.
- **Mutable**: Dictionaries are dynamic and can be modified after creation.
- **Keys Must Be Unique**: Each key in a dictionary must be unique, and it can map to a single value.

## Common Operations on Dictionaries

### 1. Adding Key-Value Pairs

You can add a new key-value pair to a dictionary using assignment.

```python
1   def add_pair(my_dict: dict[str, int], key: str, value: int) -> dict[str, int]:
2       """Adds a key-value pair to a dictionary."""
3       my_dict[key] = value
4       return my_dict
```

### 2. Removing Key-Value Pairs

Keys and their corresponding values can be removed using the `pop()` method or the `del` statement.

```python
5   def remove_key(my_dict: dict[str, int], key: str) -> dict[str, int]:
6       """Removes a key-value pair from a dictionary."""
7       if key in my_dict:
8           del my_dict[key]
9       return my_dict
```

### 3. Accessing Values

#### Using Square Brackets:

The most straightforward way to access a value is by using its key inside square brackets. However, this method will raise a `KeyError` if the key doesn't exist in the dictionary.

```python
10  def access_value_brackets(my_dict: dict[str, int], key: str) -> int:
11      """Accesses the value associated with a given key using square brackets."""
12      try:
13          return my_dict[key]
14      except KeyError:
15          return "Key not found"
```

#### Using the `get()` Method:

An alternative way to access values is by using the `get()` method. This method returns `None` or a default value if the key doesn’t exist, thereby avoiding a `KeyError`.

```python
16  def access_value_get(my_dict: dict[str, int], key: str) -> int:
17      """Accesses the value associated with a given key using the get() method."""
18      return my_dict.get(key, "Key not found")
```

---

### Questions:

1. What makes dictionaries different from lists and tuples?
2. How do you add a new key-value pair to a dictionary?
3. How can you remove a key-value pair from a dictionary?
4. Describe the two methods of accessing values in a dictionary.
5. Can a dictionary have duplicate keys? Why or why not?

---

### Questions and Answers:

1. **What makes dictionaries different from lists and tuples?**
    - Answer: Dictionaries are unordered collections of key-value pairs. Unlike lists and tuples, they are not indexed by integer positions but by unique keys. Lists are ordered and mutable, and tuples are ordered but immutable. Dictionaries are mutable but unordered.

2. **How do you add a new key-value pair to a dictionary?**
    - Answer: You can add a new key-value pair to a dictionary using assignment. For example: `my_dict[key] = value`.

3. **How can you remove a key-value pair from a dictionary?**
    - Answer: You can remove a key-value pair using the `pop()` method or the `del` statement. For instance: `del my_dict[key]` will remove the key and its associated value from the dictionary if the key exists.

4. **Describe the two methods of accessing values in a dictionary.**
    - Answer: Values can be accessed either using square brackets or the `get()` method. Square brackets will raise a `KeyError` if the key doesn't exist, whereas `get()` will return `None` or a default value if the key doesn’t exist.

5. **Can a dictionary have duplicate keys? Why or why not?**
    - Answer: No, a dictionary cannot have duplicate keys. Each key in a dictionary must be unique because keys are used to access their corresponding values. If you try to add a duplicate key, it will overwrite the existing value for that key.

---

# week 1: Advanced Dictionary Operations and Ordering

## Advanced Operations on Dictionaries

### 1. Iterating Through Key-Value Pairs

You can iterate through all key-value pairs in a dictionary using the `.items()` method.

```python
19  def iterate_items(my_dict: dict[str, int]) -> None:
20      """Iterates through key-value pairs."""
21      for key, value in my_dict.items():
22          print(f"Key: {key}, Value: {value}")
```

### 2. Iterating Through Keys

The `.keys()` method allows you to iterate through all the keys in a dictionary.

```python
23  def iterate_keys(my_dict: dict[str, int]) -> None:
24      """Iterates through keys."""
25      for key in my_dict.keys():
26          print(f"Key: {key}")
```

### 3. Iterating Through Values

The `.values()` method lets you iterate through all the values in a dictionary.

```python
27  def iterate_values(my_dict: dict[str, int]) -> None:
28      """Iterates through values."""
29      for value in my_dict.values():
30          print(f"Value: {value}")
```

## Dictionaries are Ordered as of Python 3.7+

Starting from Python 3.7, the insertion order of items in a dictionary is preserved. This means that when you iterate through a dictionary, items will appear in the order they were added.

```python
31  def check_order(my_dict: dict[str, int]) -> None:
32      """Checks the order of items in a dictionary."""
33      for key in my_dict.keys():
34          print(f"Key: {key}")
```

Being "ordered" allows for predictable behavior when iterating through dictionaries, which can be crucial in many applications.

---

### Questions:

6. How can you iterate through all key-value pairs in a dictionary?
7. What method would you use to iterate only through the keys?
8. What method would you use to iterate only through the values?
9. What does it mean for dictionaries to be "ordered" as of Python 3.6?
10. How does the ordered nature of dictionaries affect how you might use them?

---

### Questions and Answers:

6. **How can you iterate through all key-value pairs in a dictionary?**
    - Answer: You can use the `.items()` method to iterate through all key-value pairs in a dictionary. For example: `for key, value in my_dict.items():`.

7. **What method would you use to iterate only through the keys?**
    - Answer: You can use the `.keys()` method to iterate only through the keys in a dictionary. For example: `for key in my_dict.keys():`.

8. **What method would you use to iterate only through the values?**
    - Answer: You can use the `.values()` method to iterate only through the values in a dictionary. For example: `for value in my_dict.values():`.

9. **What does it mean for dictionaries to be "ordered" as of Python 3.7?**
    - Answer: Starting from Python 3.6, dictionaries maintain the insertion order of items. This means that when you iterate through a dictionary, items will appear in the order they were added.

10. **How does the ordered nature of dictionaries affect how you might use them?**
    - Answer: The ordered nature of dictionaries allows for predictable behavior when iterating through them. This can be particularly useful in scenarios where the order of items matters, such as maintaining a sequence of events or tasks.

---
