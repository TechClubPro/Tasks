""" Program to Display Info about States in South India"""
#Info of States
"""
"kerala": "God's own Creation, Full of Natural beauty",
"karnataka": "It has India's biggest IT Hub",
"Tamilnadu":"It is rich in cultural heritage, beautiful temples",
"Andhra Pradesh":"It is known for Kuchipudi Dance",
"Telangana":"It is famous for Hydrabadi Pearls"
"""

#Storing Info in Dictionary

stateInfo={"Kerala":"God's own Creation, Full of Natural beauty",
           "Karnataka":"It has India's biggest IT Hub",
           "TamilNadu":"It is rich in cultural heritage, beautiful temples",
           "Andhra Pradesh": "It is known for Kuchipudi Dance",
           "Telangana":"It is famous for Hydrabadi Pearls"}
#Take the user Input


state= input("Please enter the state name: ")

if state in stateInfo.keys():
    print(stateInfo[state])
else:
    print("State not in South India")


