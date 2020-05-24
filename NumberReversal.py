#User Input Module
Num = int(input("Enter 4 Digit Number: "))

#Number Break Module
#Unit Place Number
UnitPlace = Num % 10 

#Change the Original Number, to get the Ten's place Num

Num= int(Num/10)

#TensPlace Value
TensPlace= Num%10

#Change the Original Number, to get the Hundred's place Num

Num= int(Num/10)

#Hundred's Place Value
HundredPlace= Num%10

#Change the Original Number, to get the Thousand's place Num

Num=  int(Num/10)

#Number Exchange Logic
reverse = UnitPlace*1000 + TensPlace*100+ HundredPlace*10+Num

#Show Result
print("The reversed Number is: " + str(reverse))
