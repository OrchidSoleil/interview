# interview tasks

# 1. check if list contains integer x
def check_for_item_in_list(an_item, your_list):
    if an_item in your_list:
        print(f"{an_item} in a list.")
        return True
    else:
        print(f"{an_item} not in a list.")
        return False


my_list = [1, 2, 2, 3, 4, 5]
item1 = 6
item2 = 2

check_for_item_in_list(item1, my_list)
check_for_item_in_list(item2, my_list)


# 2. find duplicate number in integer list
def find_duplicate_number_in_list(your_list):
    for i in your_list:
        if your_list.count(i) > 1:
            return print(f"Duplicate number in a list is {i}.")
    return print("No duplicates in this list.")


find_duplicate_number_in_list(my_list)


# 3. check if two strings are anagrams
def is_anagram(string1, string2):
    if set(string1) == set(string2):
        print(f"'{string1}' and '{string2}' are anagrams.")
        return True
    else:
        print("Not anagrams.")
        return False


anagram1 = "kaban"
anagram2 = "bakan"
anagram3 = "arkan"
is_anagram(anagram1, anagram2)
is_anagram(anagram1, anagram3)


# 4. remove all duplicates from list
def remove_duplicates_from_list(your_list):
    your_list = set(your_list)
    print(f"Duplicates removed from the list {your_list}")
    return your_list


remove_duplicates_from_list(my_list)


# 5. check if a string is a palindrome
def is_palindrome(string1):
    word = list(string1)
    if word == word[::-1]:
        print(f"{string1} is a palindrome.")
    else:
        print(f"{string1} is not a palindrome.")


palindrome1 = 'mom'
palindrome2 = 'palindrome'
is_palindrome(palindrome1)
is_palindrome(palindrome2)


# 6. find pairs of integers in list so that their sum is equal to integer x
def sum_pairs(list_of_integers, integer_x):
    for i in list_of_integers:
        for j in list_of_integers:
            if i+j == integer_x:
                print(f"{i} + {j} == {x}")
    return True


integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 6
sum_pairs(integers, x)


# 7. use list as a stack (last in, first out) and queue (first in, first out)
def list_as_stack(your_stack):
    your_stack.append(4)
    return your_stack.pop()


def list_as_queue(your_queue):
    your_queue.append(2)
    return your_queue.pop(0)


print(f"List as stack LIFO: {list_as_stack(integers)}")
print(f"List as queue FIFO: {list_as_queue(integers)}")


# 8. Find missing number in [1...100]
def get_missing_number(your_list):
    for i in range(1, 101):
        if i not in your_list:
            print(f"Missing number is {i}")
    return True


a_hundred = list(range(1, 101))
a_hundred.remove(13)
get_missing_number(a_hundred)


# 9. Compute the intersection of two lists
def lists_intersection(list1, list2):
    intersected = set()
    for i in list1:
        if i in list2:
            intersected.add(i)
    return intersected


lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [3, 4, 5, 7, 8]
print(f" Intersection of {lst1} and {lst2} is: {lists_intersection(lst1, lst2)}")


# 10. Find max and min in assorted list. This is obvious to use min() and max(), so I'll skip.

# 11. Reverse string using recursion
def reversed_string(your_string):
    if len(your_string) <= 1:
        return your_string
    return reversed_string(your_string[1:]) + your_string[0]


print(f"Reversed 'ifan' to {reversed_string('ifan')}")


# 12. Sort list with quicksort algorithm.

# 13. Find all permutations of a string.

# def get_permutations(your_string):
#     if len(your_string) <= 1:
#         return set(your_string)
#     shorter = get_permutations(your_string[1:])
#     permutations = set()
#     for s in shorter:
#         for i in range(1, len(s) + 1):
#             permut = s[:i] + your_string[0] + s[i:]
#             permutations.add(permut)
#     return permutations
#
#
# print(get_permutations('abc'))


# 14. Linked list in Python (single)
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return None
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
#
#     def display(self):
#         current = self.head
#         while current is not None:
#             print(current.data, end='->')
#             current = current.next
#         print('None')


# 15. Distribute array of integers into a hash table
def hash_index(key):
    index = (3 * key + 4) % 7
    return index


hash_table_1 = [None] * 7
nums = [1, 3, 8, 10]


def hash_it(your_array, your_hash_table):
    for i in your_array:
        index = hash_index(i) % len(your_hash_table)
        # index = 0 if hash >= len(your_hash_table) else hash
        while your_hash_table[index] is not None:
            index = (index + 1) % len(your_hash_table)
        your_hash_table[index] = i
    return your_hash_table


print(hash_it(nums, hash_table_1))


# 16. Convert infix expression to postfix
class InfixConverter:
    def __init__(self):
        self.operator_precedence = {'+': 1, '-': 1, '/': 2, '*': 2, '^': 3}

    def convert(self, infix):
        operators_stack = []
        output_stack = []

        for i in list(infix):
            if i == '(':
                operators_stack.append(i)
                continue
            elif i.isalpha():
                output_stack.append(i)
                continue
            elif i == ')':
                for operator in operators_stack[::-1]:
                    if operator == '(':
                        operators_stack.pop()
                    else:
                        output_stack.append(operators_stack.pop())
            elif i in self.operator_precedence:
                if len(operators_stack) == 0:
                    operators_stack.append(i)
                    continue
                elif operators_stack[-1] == '(' and len(operators_stack) >= 1:
                    operators_stack.append(i)
                else:
                    # compare i to last operator in stack
                    for operator in operators_stack[::-1]:
                        if self.operator_precedence[i] < self.operator_precedence[operator]:
                            output_stack.append(operators_stack.pop())
                            operators_stack.append(i)
                            continue
                        if self.operator_precedence[i] > self.operator_precedence[operator]:
                            operators_stack.append(i)
                            continue
                        else:
                            operators_stack.append(i)
        if len(operators_stack) > 0:
            output_stack.extend(operators_stack)
        return f"{infix} => {' '.join(output_stack)}"


converter = InfixConverter()
print(converter.convert('a^b+c*(d-e)'))
print(converter.convert('a*(b+c)/d'))
print(converter.convert('((a+b)*c-d)/e'))
print(converter.convert('(a+(b-c))*(d/e)'))


# 17. Check for matching parentheses
class ParenthesesMatchChecker:
    def __init__(self):
        self.parentheses = {')': '(',  '}': '{', ']': '['}

    def find_unmatched(self, text):
        parentheses_stack = []
        unmatched_parentheses = []
        for i in text:
            if i in {'(', '[', '{'}:
                parentheses_stack.append(i)
            elif i in {')', ']', '}'}:
                if  len(parentheses_stack) > 0:
                    if parentheses_stack[-1] == self.parentheses[i]:
                        parentheses_stack.pop()
                else:
                    unmatched_parentheses.append(i)
            else:
                continue
        unmatched_parentheses.extend(parentheses_stack)
        return unmatched_parentheses

text = "ОДНОСТВОЛКА одностволка] -и, ж.‘тс, що ОДИНОЧКА:-. Ходиу на охдту з одностволкойу. 166, 421, 465; ОДПАДІ одпаді -у, ч. велика смертність серед тварин 2. ОДРИГАТИСЬ [одригатис\"]]"
parentheses = ParenthesesMatchChecker()
print(f"Unmatched parentheses: {parentheses.find_unmatched(text)}")      
