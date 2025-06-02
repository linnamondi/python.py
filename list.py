# 1. Inventory Tracker
# You are managing a shop’s inventory. The items are stored in a list:
# Question: Add 'butter' to the inventory and then check if 'eggs' is still available.
inventory = ['milk', 'bread', 'eggs']
inventory.append("butter")
print("eggs" in inventory)

# . Student Attendance
# # A list holds names of students present in class:
#  Remove 'John' from the list and insert 'Aisha' at the second position.

students = ['Ali', 'Mary', 'John', 'Fatima']
students.remove("John")
students.insert(1,'Aisha')
print(students)

# You have a list of your 5 favorite movies.
# Question: Replace 'Titanic' with 'Interstellar' and print the updated list.
movies = ['Inception', 'Matrix', 'Avatar', 'Titanic', 'Gladiator']
movies[3]='Interstellar'
print(movies)


# # 4. Monthly Sales
# # Sales for January to June are stored as:
# Calculate the total and average sales.
sales = [2200, 1850, 1990, 2100, 1980, 2300]
total=sum(sales)
average=total/len(sales)
print("total:",total,"Avarage:",average)

# # . Shopping List
# # You have the following shopping list:
# Ask the user for an item, check if it's in the list, and add it if not.
shopping = ['sugar', 'salt', 'soap']
item=input("enter an item").strip().lower()
if item in shopping:
    print(f"{item} already in the shopping list")
else:
    shopping.append(item)
    print(F"{item} has been added to the shopping list")

print("updated shopping list:" ,shopping)

# 6. Duplicate Removal
# Given:
# Question: Write code to remove the duplicates.
nums = [1, 2, 2, 3, 4, 4, 5]
nums2=[]
for num in nums:
    if num not in nums2:
        nums2.append(num)
print(nums2)

nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))
print(unique_nums)

# Reversing a List
# You’re given a list:
# Question: Reverse the list without using the .reverse() method.
colors = ['red', 'green', 'blue', 'yellow']
print(colors[::-1])

#  Each student’s grades are stored as a nested list:
# Question: Print each student’s average score.
grades = [[80, 90], [70, 60], [85, 95]]
for i ,g in enumerate(grades):
    Avaragegrade=sum(g)/len(g)
    print(f"Student {i+1} average: {Avaragegrade}")

# Two lists of users:
# Question: Combine them into a single list called all_users and sort alphabetically.
admins = ['alice', 'bob']
users = ['charlie', 'dave']
all_users=admins +users
all_users.sort()
print(all_users)

# 10. Index Tracking
# List of tasks:
# Question: Find the index of 'meeting' and replace it with 'presentation'.

tasks = ['email', 'call', 'meeting', 'report']
i=tasks.index('meeting')
tasks[i]='presentation'
print(tasks)

# 11. List Slicing - Weekly Logs
# Given a list of log messages from 7 days:
# Question: Print only the weekdays (Mon–Fri) using slicing.
logs = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(logs[0:5])

# 12. Even Number Filter
# List of integers:
# Question: Create a new list of only even numbers using list comprehension.

numbers = [10, 15, 20, 25, 30, 35]
even=[number for number in numbers if number%2==0]
print(even)

# 13. Insert and Pop
# List of fruits:
# Question: Insert 'orange' at position 1 and remove the last item.

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1,"orange")
fruits.pop(-1)
print(fruits)

# 14. Longest Word
# Given:
# Question: Find the longest word in the list.
words = ['data', 'science', 'machine', 'learning']
word=max(words,key=len)
print(word)

# Sort and Reverse Scores
# List of scores:
# Question: Sort them in descending order.
scores = [65, 89, 78, 90, 55]
scores.sort(reverse=True)
print(scores)

# Prices:
# Question: Calculate the sum of prices greater than 120.
prices = [99, 150, 120, 175, 200]
high_prices=[price for price in prices if price>120]
print(sum(high_prices))

# 17. Common Elements Between Lists
# Two customer order lists:
orders_day1 = ['apple', 'banana', 'milk']
orders_day2 = ['banana', 'bread', 'milk']
common_list=list(set(orders_day1) & set(orders_day2))
print(common_list)

# 18. Palindrome Checker with Lists
# Given a word from user input, check if it's a palindrome using list slicing.

word =input("enter a word:")
if list(word)==list(word)[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# 19. Dynamic List Builder
# Ask a user to input 5 numbers and store them in a list. Then return the max and min values.
numbers=[]
for n in range(5):
    n=input("enter number")
    numbers.append(n)
print("max:", max(numbers))
print("min:", min(numbers))

# Question: Flatten this into a single list: [1, 2, 3, 4, 5, 6].
matrix = [[1, 2], [3, 4], [5, 6]]
flattenlist=[i for g in matrix for i in g]
print(flattenlist)












