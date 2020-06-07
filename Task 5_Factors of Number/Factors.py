
"""
Program to find the Factors of any number
"""

num = int(input("Enter the number: "))
factor=[]
index=0

for i in range(1,num+1):
    if num % i == 0:
        factor.insert(index, i)
        index=index+1
        
print("The factors of number "+ str(num)+"are: " + str(factor))