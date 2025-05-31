# Create a tuple with values (1, 2, 3)
u=(1, 2, 3)
print(u)
# . Access the second element of the tuple t.
t=(1, 2, 3)
print(t[1])
# t[0]=10 python doesnot accept reassignment

# Create a tuple with a single element 5.
single=(3,)
print(type(single))

# Unpack a tuple t into variables a, b, c.

a,b,c=t
print(a,b,c)

# Concatenate two tuples (1, 2) and (3, 4).
k=(1,2)
o=(3,4)
h=k+o
print(h)

# Repeat a tuple (0,) three times.
j=(0,)*3
print(j)

# Check if the value 2 is in tuple t.
print(2 in t)

# Get the length of tuple t.
print(len(t))

# Convert a list [1, 2, 3] to a tuple.
i=[1, 2, 3]
print(tuple(i))

# . Count how many times 2 appears in (1, 2, 3, 2).
e=(1, 2, 3, 2)
print(e.count(2))

# Q14. Slice the tuple (1, 2, 3, 4, 5) to get (2, 3).
q=(1, 2, 3, 4, 5)
print(q[1:3])

# Q15. Unpack tuple t = (1, 2, 3, 4) ignoring the second element.
t=(1, 2, 3, 4) 
a,_,b,c=t
print(a,b,c)

# Q16. Use tuple unpacking with * to get first element and the rest.
q=(6,8,0,11,23)
first, * rest=q
print(first)
print(rest)

a=1
b=2
a,b=b,a
print(a,b)

# Use tuples as dictionary keys.
d={}
key=(1)
d[key]="linn"
print(d) 

# Create a nested tuple (1, (2, 3), 4) and access the value 3.
q=(1, (2, 3), 4)
print(q[1][1])






