"""
#creating a list
a=["jagadeesh","bananna"]
b=[1,3,4,5,6,6]
c=[2,"apple",2.00,"true"]
print(a)
print(b)
print(c)

#uisng list constructor
a=list(("bananna","apple","mango"))
print(a)

#accessing a list
a=[12,43,5,6,7]
print(a[0])
print(a[-1])
print(-5)

a=[4,5,7]
a.append(2)
print("after the append:",a)
a.extend([])
print("after  the extend:",a)
a.insert(0,4)
print("after the insert:",a)
a.remove(7)
print("after the deletion:",a)         
poped_value=a.pop(4)
print("after the element:", poped_value)

l=["dfg","jaaga","navee","prasanth",1,3,5,"duyia",6]
print(l[2:12:3])

#also using this method:
print(l[2::3])

l=[9,8,"hi",12,"hello",15.55,"programming",100,125.5]
print(l[2:9:3])
print(l[-2:-5:-1])
print(l[5:-2])

#using delete method or remove method:
l=["python","jagadeesh","coding"]
del l[0]
print(l)
l.remove("jagadeesh")
print(l)

t=(10,3,5,64,10,10)
print(t.index(10))
"""
#using updating and append:
t=[2,4,56,77,87]
t[1]=333
print(t)

t.append(45)
print(t)

#Extend List
#To append elements from another list to the current list, use the extend() method.
thislist = ["apple","banana","mango"]
tropical = ["green","yellow"]
thislist.extend(tropical)
print(thislist)