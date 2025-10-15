"""
#Accessing the dictionary:
d={"name":"jagadee","age":22,"degree":"masters"}
print(d)

#updating the dictionary:
d={"name":"jagadee","age":22,"degree":"masters"}

d["name"]="python"
print(d)


#using delte dictionary:
d={"name":"jagadee","age":23,"clg":"vignan"}
del d["name"]
#del d
#d.clear()
print(d)

#properties of dictionary keys: there are two(2) points:

# 1)if you entered same key in dictionary its gives a output is last one same key is wins:
d={"name":"priya","age":23,"name":"jagadesh"}
print(d)

#2)you can use strings,numbers or tuples as dictioanry keys but some thing like [keys] is not allowed:
d={"[name]":"priya","age":23,"hero":"jagadesh"}
print(d["name"]) 
#thhis output is error

#using dictionary methods:
#dict.copy():
d1={"name":"riya","age":24,"sex":"f"}
d2=d1.copy()
print(d2)

#using fromkeys() method:
seq=("name","age","sex") 
dict=dict.fromkeys(seq)
print(dict)
dict=dict.fromkeys(seq,420)
print(dict)
"""

#using get() method:
d={"name":"riya","age":24,"sex":"f"}
print(d.get("age"))

#using item() method:
d={"name":"riya","age":24,"sex":"f"}
print(d.items())