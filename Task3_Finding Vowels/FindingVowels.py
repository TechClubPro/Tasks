"Program to Find Vowels in the Name Entered"

name = input("Enter the Name: ").lower()

VowelFound = ['','','','','']
count=0

if 'a' in name:
    VowelFound[count]='a'
    count=count+1
    
if 'e' in name:
    VowelFound[count]='e'
    count=count+1
    
if 'i' in name:
    VowelFound[count]='i'
    count=count+1
    
if 'o' in name:
    VowelFound[count]='o'
    count=count+1
    
if 'u' in name:
    VowelFound[count]='u'
    count=count+1
    
print("The vowels in the name "+ name +" are" + str(VowelFound))