# first_dict = { 1:"a", 2:"b", 3:"c", 4:"d" , 5:"e" }
# print(first_dict[3])
# print(6 in first_dict)
# print(4 not in first_dict)


# first1 = {"Queen": "Bohemian Rhapsody", 
#           "Bee Gees": "Stayin' Alive", 
#           "U2": "One", 
#           "Michael Jackson": "Billie Jean", 
#           "The Beatles": "Hey Jude", 
#           "Bob Dylan": "Like A Rolling Stone"
# }
# print(len(first1))
# for key in first1.keys():
#     print(key)
# for value in first1.values():
#     print(value)
# for key, value in first1.items():
#     print(key,value)
# print(first1.get("Promise of the Real", "key is not present"))


# for key, value in {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant").items():
#     print(key, value)

# food_item = {"McDonald's": "Big Mac",
#              "Burger King": "Whopper", 
#              "Chick-fil-A": "Sandwich"
# }
# popped = food_item.pop("Chick-fil-A")
# print(popped)

celebreties =  {"DrDisrespect": "YouTube",
                "ZLaner": "Facebook",
                "Ninja": "Mixer"
}
print(celebreties)
print(len(celebreties))
add = {"shroud": "Twitch"}
celebreties.update(add)
gamers = celebreties.copy()
print(celebreties)
print(gamers)