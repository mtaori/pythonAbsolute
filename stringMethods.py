# mixed_case = "A Song of Ice and Fire"
# print(mixed_case.isupper())  
# print(mixed_case.islower())  
# print(mixed_case.upper())  
# print(mixed_case.lower())  
# print(mixed_case.istitle())  
# title_case = mixed_case.title()
# print(title_case)  
# print(mixed_case.startswith("A"))  
# print(mixed_case.endswith("e"))  
# words = mixed_case.split()
# print(words)  
# print("".join(words).isalpha()) 


# the_string = "North Dackota"
# print(the_string.rjust(17))
# print(the_string.ljust(17, "*"))

# center_plus = the_string.center(16, "+")
# print(center_plus)

# print(the_string.lstrip("North"))
# print(center_plus. rstrip("+"))
# print(center_plus.strip("+"))
# print(the_string.replace("North", "South"))

# user_str = input("Enter the string:\n")
# rev = ""
# for item in range(len(user_str) -1, -1, -1):
#     rev += user_str[item]
# print(rev)

# user_str = "James Bond is 007."
# def count(words):
#     space = ""
#     count = 1
#     for w in words:
#         if w.isalnum() or w.isspace() or w == "-" or w == "'":
#             space += w
#     for s in space:
#         if s == " ":
#             count += 1
#     return count

# print(count(user_str))

name = input("enter the name: ")
experience = input("enter work experience: ")
company = input("enter company: ")
print("{} has work experience of {} and worked in {}".format(name, experience, company))
