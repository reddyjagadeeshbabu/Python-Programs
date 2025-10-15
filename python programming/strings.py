'''#string indexing:
s="jagadeesh"
print(s[0])

#string slicing:
s="jagadeesh"
print(s[1:5])
print(s[:3])
print(s[1:])

#string reverse:
s="jagadeesh"
print(s[::-1])


#string deletion:
s="gfg"
del s


#string replacing:
s1="hello world"

s2=s1.replace("hello","jagadeesh")
print(s1)
print(s2)


#string methods:
s="jagadeesh"
print(len(s))
print(s.lower())
print(s.upper())

# string strip(): strip() removes leading and trailing whitespace from the string
s="   haripriya   "
print(s.strip())
'''
#for loop using reverse mehtod:
s="geeksforgeeks"
rev=""
for ch in s:
    rev= ch + rev
print(rev)