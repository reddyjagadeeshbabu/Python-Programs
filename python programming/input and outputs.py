
'''
#using .split() function:
x, y, z = input("enter the value:").split()
print(x)
print(y)
print(z)

'''
#Using map() for Multiple Integer Inputs
'''
If you need to collect multiple inputs in a single line and convert them into integers
(or another data type), the map() function is useful. The map() function applies a
specified function to each item in an iterable.

a = map(int, input().split())
b = list(a)
print(b)

'''
'''
#input formatting in print() function:
print("helo world")


#using (sep="")parameter:
a=12
b=4
c=2003
print(a,b,c,sep="-")

#using (end="")parameter:
print("jagadeesh",end=" ")
print("babu")
'''


'''#output formatting print() functions:

# using  format() method :
name="jagadhee"
age=22
print("Name:{},Age: {}".format(name,age))


#using  f-strings method:
name="parvathi"
age=56
print(f"name:{name},age:{age}")


#using modulus operator(%) method:
name="nagendra"
age=23
print("name:%s,age:%d"%(name,23))



#formating output using string method:

#1) using str.center() method
str="i love jagadeesh"
print("center aligned:")
print(str.center(40,'#'))


#2) using str.ljust() method:
str="i love jagadeesh"
print("left aligned")
print(str.ljust(30,'-'))

'''
'''
#3)using str.rjust() method:
str="i love"
print("right aligned")
print(str.rjust(30,'-'))
'''