# interview tasks

# 1. check if list contains integer x
def check_for_item_in_list(an_item, your_list):
    if an_item in your_list:
        print(f"{an_item} in a list.")
        return True
    else:
        print(f"{an_item } not in a list.")
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
            print(f"Duplicate number in list is {i}")
            return i
        else:
            print('No duplicates found.')


find_duplicate_number_in_list(my_list)


# 3. check if two strings are anagrams
def if_anagram(string1, string2):
    string1 = set(string1)
    string2 = set(string2)
    if string1 == string2:
        print("Anagram.")
        return True
    else:
        print("Not anagram.")
        return False


anagram1 = "kaban"
anagram2 = "bakan"
anagram3 = "arkan"
if_anagram(anagram1, anagram2)
if_anagram(anagram1, anagram3)


# 4. remove all duplicates from list
def remove_duplicates_from_list(your_list):
    your_list = set(your_list)
    print(f"Duplicates removed from the list {your_list}")
    return your_list


remove_duplicates_from_list(my_list)


# 5. check if a string is a palindrome
def is_palindrome(string1):
    make_list = list(string1)
    palindrome = make_list[:]
    palindrome.reverse()
    if make_list == palindrome:
        print(f"{string1} is a palindrome.")
    else:
        print(f"{string1} is not a palindrome.")


palindrome1 = 'palipilap'
palindrome2 = 'earrings'
is_palindrome(palindrome1)
is_palindrome(palindrome2)

# 6. find pairs of integers in list so that their sum is equal to integer x

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 6


def sum_pairs(list_of_integers, integer_x):
    for i in list_of_integers:
        for j in list_of_integers:
            if i+j == integer_x:
                print(f"{i} + {j} == {x}")


sum_pairs(integers, x)

# 7. use list as a stack (insertion and deletion is on one end), array, and queue (first in, first out)


def list_as_stack(your_stack):
    your_stack.append(1)
    your_stack.pop()


def list_as_queue(your_queue):
    your_queue.insert(0, 1)
    print(your_queue.pop(0))


# 8. Get missing number in [1...100]

a_hundred = list(range(1, 101))


def get_missing_number(your_list):
    a_hundred.remove(13)
    for i in range(1, 101):
        if i not in your_list:
            print(f"Missing number is {i}")
            return i


get_missing_number(a_hundred)
