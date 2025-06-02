# Q1. Use a for loop to print numbers from 1 to 10 but stop the loop once you reach 5 using break.
for number in range (1,11):
    if number==5:
        break
    print(number)

# . Print numbers 1 to 10, but skip number 3 using continue.

for number in range (1,11):
    if number==3:
        continue
    print(number)
# Ask the user to enter numbers until they type 0, using break to exit the loop.
while True:
    num=int(input("Enter number"))
    if num==0:
        break
    print("You entered num",num)

# Q4. Print all letters in a string except vowels, using continue to skip vowels.
# word="programming"
# for i in word:

#     if i in "aeiou":
#         continue
#     print (i,end="")

# Q5. Use a loop to search for the letter 'e' in a list of letters, stop once found using break.
letters = ['a', 'b', 'c', 'd', 'e', 'f']
for letter in letters:
    if letter =='e':
        print("found 'e' ")
        break
# Q6. In a list of numbers, print only odd numbers, skipping even numbers using continue.
numbers = [1, 2, 3, 4, 5, 6]
for nums in numbers:
    if nums%2==0:
        continue
    print(nums)

# 7. Use while loop to print numbers from 1 to 10, but stop if number equals 7 using break.

i=1
while i<10:
    if i==7:
        break
    print(i)
    i+=i

# Q8. Skip printing numbers divisible by 3 between 1 to 10 using continue.
for number in range(1,11):
    if number%3==0:
        continue
    print(number)

# Q9. Ask the user repeatedly for a password, stop asking when the password is correct using break.
correctPassword="open123"
while True:
    pwd=input("enter password:")
    if pwd==correctPassword:
        break
    print("incorrect try again!")
# Q1. Write a program to check if a number is positive, negative, or zero.
number=int(input("Enter a number:"))
if number>0:
    print("It is positive")
elif number<0:
    print("It is negative")
else:
    print("It is zero")

# Use a while loop to print numbers from 1 to 5.
number=1
while number<5:
    print(number)
    number+=1
# Q3. Write a for loop that prints all even numbers between 2 and 10.
for number in range (2,11):
    if number%2 !=0:
        continue
    print(number)
# . Use a for loop to iterate over a list of fruits and print each fruit.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Write a program to find the sum of numbers from 1 to 10 using a loop.
total=0
for i in range(1,11):
    total+=i
print (total)

#  Use a while loop to keep asking the user to enter "yes" to exit.
reponse=" "
while reponse.lower()!="yes":
    reponse=input("Yes to exit:")
print("existed the loop")

#  Write a program using if that checks if a user-entered character is a vowel.

char=input("Enter a character:").lower()
if char in "aeiou":
    print("is vowel")
else:
    print("not a vowel")

#  Use break in a loop to stop printing numbers once it reaches 5.
for i in range(10):
    if i ==5:
        break
    print(i)
# Q9. Use continue to skip printing the number 3 in a loop from 1 to 5.
for i in range (1,6):
    if i==3:
        continue
    print(i)
# Q10. Write a program to find the factorial of a number using a while loop.
num=6
factorial=1
while num>1:
    factorial*=num
    num -=1
print(factorial)

#  Print each character in a string using a for loop.
honey="cookies"
for char in "cookies":
    print(char)

#  Use a nested for loop to print a 3x3 multiplication table.
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

# Write a program that asks for a password and keeps asking until the correct password is entered.
password="secret"
attempt=" "
while attempt !=password:
    attempt=input("enter password:")
print("access granted!")

# . Use else after a for loop to confirm the loop ran without a break.
for i in range(3):
    print(i)
else:
    print("The link the finished without a break")

#  Print only odd numbers from 1 to 10 using a for loop and continue.
for number in range(1,10):
    if number%2==0:
        continue
    print(number)
# Use a while loop to print numbers from 10 down to 1.
i=10
while i>0:
    print(i)
    i -=1
# Use an if to check if a number is divisible by both 3 and 5.
num=15
if num %3 ==0 and num%5==0:
    print("Divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")

#  Use a for loop with range() to print numbers 0 to 4.
for i in range(0,5):
    print(i)
# Write a program that asks the user to enter numbers until the sum exceeds 100.
total=0
while total<=100:
    num=int(input("Enter number :"))
    total+=num
print("Exceeded the total sum:",total)











