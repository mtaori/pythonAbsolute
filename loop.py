# num = 10
# while num != 0:
#     print(num)
#     num -= 1
# pnum = int(input("Enter the number : "))
# total = pnum
# sum = 0
# while pnum > 0:
#     sum += pnum
#     pnum -= 1
# print(sum)

# word = "hello world"
# for letter in word:
#     print(letter)

# a = range(5)
# for num in a:
#     print(num)


# string1 = input("enter the string: ")
# count = 0
# for char in string1:
#     count += 1
# print(string1)
# print(count)

# number = range(1, 51)
# for num in number:
#     if num % 3 == 0 and num % 5 == 0:
#         print("fizz buzz")
#     elif num % 5 == 0:
#         print("bizz")
#     else:
#         print(num)

num = int(input("Enter the number:\n"))
def fact_pro(num):
    n = 1
    total = range(num, 1, -1)
    for item in total:
        n *= item
    return n

print(fact_pro(num))





