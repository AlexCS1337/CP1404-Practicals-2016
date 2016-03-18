__author__ = 'Alex'

""" Password Checker written by Alex, 18 March 2016

"""

MINIMUM_LENGTH = 6
MAXIMUM_LENGTH = 15


print("Please enter a valid password")
print("Your password must be between 6 and 15 characters, and contain:\n"
      "1 or more uppercase characters\n"
      "1 or more lowercase characters\n"
      "1 or more number/s\n"
      "and 1 or more special characters: !@#$%^^&*()_[]")

password = input(">")
while len(password) < MINIMUM_LENGTH or len(password) > MAXIMUM_LENGTH:
    print("Invalid password!")
    password = input(">")

print("Your 10 character password is valid:", password)