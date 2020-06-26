
"""
Sum of Divisors using Function
"""

def sum_Divisors(num):
    Sum=0
   
    for i in range(1,num+1):
        
        if num % i ==0:
            Sum= Sum+i
            
    return Sum




# With the specific Number

Div_Sum = sum_Divisors(8)


print("Sum of Divisors of 8 is:",Div_Sum)

#Take Input from User

num= int(input("Enter the number to find the Sum of Divisors: "))

Div_Sum = sum_Divisors(num)

print("Sum of Divisors of "+str(num)+" is: ",Div_Sum)

