# list_1 = [1, 2, "wheels", "bike", "apple" , [34, 45]]  
# li_str = list("chips")
# print("wheels" in list_1)
# print("i" not in li_str)    

# artic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
# del artic_animals[4]
# artic_animals.remove("elephant")
# artic_animals.append("artic fox")
# print(artic_animals)
# artic_animals.insert(2, "snowy owl")
# artic_animals.sort()
# print(artic_animals.index("reindeer"))
# print(artic_animals)
# print(artic_animals.pop())

import copy
a = [1, 2, 3, 4, 5]
b = copy.deepcopy(a)
b[3] = 7
print(a)
print(b)
