#  Given a string s = "Hello World", extract the substring "World".
s='Hello world'
print(s[6:])

# Count how many times the letter 'l' appears in the string "Hello World".
b='Hello world'
print(b.count('l'))

# Convert the string "python programming" to uppercase.
c="python programming"
print(c.upper())

# Check if the string "Data" starts with "Da"
p= "Data" 
print("Da" in p )

# Replace all spaces in "Hello World" with underscores.
w="Hello World"
print(w.replace(" ","_"))

# Check if the string "Data" starts with "Da"
g= "Data" 
print(g.startswith("Da"))

# . Split the string "apple,banana,cherry" into a list of fruits.
q="apple,banana,cherry"
fruits=q.split(" ")
print(fruits)

# Find the index of substring "prog" in "python programming"
k="python programming"
print(k.index("prog"))

# Check if "12345" contains only digits.
nums="12345"
print(nums.isdigit())

# Strip leading and trailing spaces from " hello ".
d=" hello "
print(d.strip())

#  Join a list of words ["Python", "is", "fun"] into a sentence separated by spaces.
e=["Python", "is", "fun"]
print(" ".join(e))

#  Convert "PYTHON" to lowercase.
f="PYTHON"
print(f.lower())

# Check if the string "Hello123" is alphanumeric.
c= "Hello123"
print(c.isalnum())

# Format the string "Name: {}, Age: {}" with values "Alice" and 30.
l="Name:{},Age:{}"
print(l.format("Alice",30))

# Capitalize the first letter of "hello world".
m="hello world"
print(m.capitalize())

# Check if "abc" is lowercase.
z= "abc"
print(z.islower())

# Check if "ABC" is uppercase.
y="ABC"
print(y.isupper())

#  Given a multiline string, split it into lines.
o = "Line1\nLine2\nLine3"
print(o.splitlines())

# Q18. Remove all vowels from "Hello World".
r="Hello World"
results="".join([ch for ch in r if ch.lower()not in "aeiou"])
print(results)

# Reverse the string "Python".
b= "Python"
print(b[::-1])

# Check if " " (space) is considered whitespace.
j=" "
print(j.isspace())











