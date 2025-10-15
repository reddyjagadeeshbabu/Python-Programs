"""
# 1. pattern 
for i in range(1,6):
    for j in range(1,6):
        print("*", end="")
    print()
    
    
   
    # 2. pattern
for i in range(1,6):
    for j in range(1,6):
        print(i, end="") 
    print()
    
     # 3. pattern
for i in range(1,6):
    for j in range(1,6):
        print(j, end="")
    print()  
    
     # 4. pattern
for i in range(1,6):
    for j in range(1,6):
        print(j%2, end="")
    print()
    
    # 5. pattern
for i in range(1,6):
        for j in range(1,6):
            print(i%2, end="")
        print()
        
    # 5. pattern
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(i, end="")
    print()
    
     # 6. pattern
for i in range(ord('a'), ord('e')+1):    
    for j in range(ord('a'), ord('e')+1):      
        print(chr(j)), end="")
    print()    
    
      # 7. pattern
for i in range(ord('a'), ord('e')+1):
    for j in range(ord('a'), ord('e')+1):
        print(chr(i), end="")
    print() 
    
    # 8. pattern
for i in range(ord('e'),ord('a')-1,-1):
        for j in range(ord('e'),ord('a')-1,-1):
            print(chr(i),end="")
        print()
        
        
        
    
    ************ patterns    


#1 right angle triangle pattern  *,**,***,****,*****


n = int(input("enter the number: "))
for row in range(1, n + 1):
    for _ in range(row):
        print("*", end=" ")
    print()
    
#2 Triangle 
    
n= int(input("enter the number of rows"))
for rows in range(1,n+1):
    print(" " * (n - rows), end="")
    print("* " * rows)    
    """
"""
#3 right triangle - growing numbers   1,12,123,1234,12345


n = int(input("enter the number"))
for row in range(1,n+1):
    for num in range(1, row+1):
        print(num, end="")
    print()  

   
    
    
    #1  number pattern 1,22,333,4444,55555
    
    
n= int(input("enter the number"))
for rows in range(1,n+1):
    for clos in range(1, rows+1):
         print(rows,end=" ")
    print()
           #(or)
n = int(input("enter the number: "))
for row in range(1, n + 1):
    for _ in range(row):
        print(row, end=" ")
    print()
   
    #3 Right triangle - continuous counting
    
    
n = int(input("enter the number of rows"))
count = 1
for rows in range(1,n+1):
    
    for _ in range(rows):
        print(count, end=" ")
        count= count + 1
    print()
   
    #4. Inverted Number Triangle
    
n= int(input("enter the rows"))
for rows in range(n,0,-1):
    for num in range(1,rows+1):
        print(num,end="")
    print()
   
     
#  6. Centered Number Pyramid

n = int(input("enter the number"))
for rows in range(1,n+1):
    print(" " * (n-rows), end="")
    for num in range(1, rows+1):
        print(num, end="")
    print()
   
      
       # 6. Palindrome Number Pyramid
n= int(input("enter the rows"))
for rows in range(1,n+1):
    print(" " * (n-rows), end="")        #spacing cneter
    for num in range(rows,0,-1):
        print(num,end="")
    for num in range(2, rows+1):
        print(num, end="")
    print()
   
    
# 8. Diamond of Numbers

n= int(input("enter the rows"))

# Upper pyramid:

for rows in range(1, n+1):
    print(" " * (n-rows), end="")
    for num in range(1, rows+1):
        print(num, end="")
    for num in range(rows-1, 0, -1):
        print(num, end="")
    print()
        
        #Lower pyramid:
        
for rows in range(n-1, 0, -1):
    print(" " * (n-rows),end="")
    for num in range(1, rows+1):
            print(num, end="")
    for num in range(rows-1, 0, -1):
            print(num, end="")
    print()
        
"""