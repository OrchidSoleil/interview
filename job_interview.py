# interview tasks

print('1. check if list contains integer x')


def check_for_item_in_list(an_item, your_list):
    if an_item in your_list:
        print(f"  '{an_item}' in a list {your_list}.")
        return True
    else:
        print(f"  '{an_item}' not in a list {your_list}.")
        return False


my_list = [1, 2, 2, 3, 4, 5]
item1 = 6
item2 = 2

check_for_item_in_list(item1, my_list)
check_for_item_in_list(item2, my_list)


print(f'\n2. find duplicate number in integer list {my_list}')


def find_duplicate_number_in_list(your_list):
    for i in your_list:
        if your_list.count(i) > 1:
            return print(f"  Duplicate number in a list is {i}.")
    return print("  No duplicates in this list.")


find_duplicate_number_in_list(my_list)


print('\n3. check if two strings are anagrams')


def is_anagram(string1, string2):
    if set(string1) == set(string2):
        print(f"  '{string1}' and '{string2}' are anagrams.")
        return True
    else:
        print(f"  '{string1}' and '{string2}' are not anagrams.")
        return False


anagram1 = "kaban"
anagram2 = "bakan"
anagram3 = "arkan"
is_anagram(anagram1, anagram2)
is_anagram(anagram1, anagram3)


print(f'\n4. remove all duplicates from list {my_list}')


def remove_duplicates_from_list(your_list):
    your_list = set(your_list)
    print(f"  Duplicates removed from the list {your_list}")
    return your_list


remove_duplicates_from_list(my_list)


print('\n5. check if a string is a palindrome')


def is_palindrome(string1):
    word = list(string1)
    if word == word[::-1]:
        print(f" '{string1}' is a palindrome.")
    else:
        print(f" '{string1}' is not a palindrome.")


palindrome1 = 'mom'
palindrome2 = 'palindrome'
is_palindrome(palindrome1)
is_palindrome(palindrome2)


print('\n6. find pairs of integers in list so that their sum is equal to integer x')


def sum_pairs(list_of_integers, integer_x):
    for i in list_of_integers:
        for j in list_of_integers:
            if i+j == integer_x:
                print(f"  {i} + {j} == {x}")
    return True


integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 6
sum_pairs(integers, x)


print(f'\n7. Use list {integers} as a stack (last in (4), first out(4)) and queue (first in ({integers[0]}), first out ({integers[0]}))')


def list_as_stack(your_stack):
    your_stack.append(4)
    return your_stack.pop()


def list_as_queue(your_queue):
    from collections import deque
    queue = deque(your_queue)
    queue.append(2)
    return queue.popleft()


print(f"  List as stack LIFO: {list_as_stack(integers)}")
print(f"  List as queue FIFO: {list_as_queue(integers)}")


print('\n8. Find missing number in [1...100]')


def get_missing_number(your_list):
    for i in range(1, 101):
        if i not in your_list:
            print(f"  Missing number is {i}")
    return True


a_hundred = list(range(1, 101))
a_hundred.remove(13)
get_missing_number(a_hundred)


print('\n9. Compute the intersection of two lists')


def lists_intersection(list1, list2):
    intersected = set()
    for i in list1:
        if i in list2:
            intersected.add(i)
    return intersected


lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [3, 4, 5, 7, 8]
print(f" Intersection of {lst1} and {lst2} is: {lists_intersection(lst1, lst2)}")


# 10. Find max and min in assorted list.

print('\n11. Reverse string using recursion')


def reversed_string(your_string):
    if len(your_string) <= 1:
        return your_string
    return reversed_string(your_string[1:]) + your_string[0]


print(f"  Reversed ifan to {reversed_string('ifan')}")


# 12. Sort list with quicksort algorithm.

# 13. Find all permutations of a string.

# 14. Linked list in Python (single)


print('\n15. Distribute array of integers into a hash table')


def hash_index(key, length):
    index = (3 * key + 4) % length
    return index


hash_table_1 = [None] * 7
nums = [1, 3, 8, 10]


def hash_it(your_array, your_hash_table):
    length = len(nums)
    for i in your_array:
        index = hash_index(i, length) % len(your_hash_table)
        # index = 0 if hash >= len(your_hash_table) else hash
        while your_hash_table[index] is not None:
            index = (index + 1) % len(your_hash_table)
        your_hash_table[index] = i
    return your_hash_table


print(f'  {nums} => {hash_it(nums, hash_table_1)}')


print('\n16. Convert infix expression to postfix')


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
print(f'  1.) {converter.convert('a^b+c*(d-e)')}')
print(f'  2.) {converter.convert('a*(b+c)/d')}')
print(f'  3.) {converter.convert('((a+b)*c-d)/e')}')
print(f'  4.) {converter.convert('(a+(b-c))*(d/e)')}')


print('\n17. Check for matching parentheses')


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
print(f"  Unmatched parentheses: {parentheses.find_unmatched(text)}")


print('\n18. Create Binary Tree with level order insertion.')


from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.count = 1


class BinaryTree:
    def __init__(self):
        self.root = None

    def level_order_insertion(self, data):
        if data is None:
            return
        if not self.root:
            self.root = Node(data)
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if data == node.data:
                node.count += 1
                return
            if node.left is None:
                node.left = Node(data)
                return
            queue.append(node.left)
            if node.right is None:
                node.right = Node(data)
                return
            queue.append(node.right)


print('\n19. Build value order insertion into a Binary Search Tree')


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def value_order_insertion(self, data):
        if data is None:
            return
        if not self.root:
            self.root = Node(data)
            return
        node = self.root
        while True:
            if data == node.data:
                node.count += 1
                return
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                    return
                node = node.left
            elif data > node.data:
                if node.right is None:
                    node.right = Node(data)
                    return
                node = node.right
