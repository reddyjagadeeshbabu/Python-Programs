#Scope of a Variable
#There are two methods how we define scope of a variable in python which are local and global.

#Local Variables:
#Variables defined inside a function are local to that function.
 #Example
'''
def jagadeesh():
    a="i am local"
    print(a)
jagadeesh()
    
'''

#Global Variables:
#Variables defined outside any function are global and can be accessed inside functions using the global keyword.
a="jagadesh"
def f():
  global a
  a="modified globally"
  print(a)
f()
print("hello", a)


