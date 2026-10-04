import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input("How many letters you wnat in your password ?"))
num_symbols = int(input("How many symbols you want to use in your password ? "))
num_numbers = int(input("How many numbers you want to use in your password ? "))

# password = ""
# if we want to print all the letter from 1 to 5 we have to put a range of 
# (1,6) but if we start from 0 then we can write (0,5)

# for char in range(0, num_letters):
#     random_letter = random.choice(letters)
#     password = password + random_letter

# for char in range(0, num_symbols):
#     random_symbol = random.choice(symbols)
#     password = password + random_symbol

# for char in range(0, num_numbers):
#     random_number = random.choice(numbers)
#     password = password+ random_number

# print(password)

#it will print the password in this way JWZbH+!!*%54735
#it is predictable because it is generating in a fix order of (letters, symbols, numbers)
# to make it unpredictable we have to shuffle the password

password_list = []

for char in range(0, num_letters):
    password_list += random.choice(letters)

for char in range(0, num_symbols):
    password_list += random.choice(symbols)

for char in range(0, num_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)
# print(password_list)

password = ""
for i in password_list:
    password = password + i

print(password)
    