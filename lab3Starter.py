# Ariana Fayehun
# Date: 9/3/24
# This completes the challenge for "lab3Starter"

"""

2. You must prompt the user to supply you their name, age,
    and their major to complete the introduction message

3. You will ensure that the message you print at the end of the file,
    aside from the user input, matches the exact spelling and format of
    the example output that has been provided to you.

4. After completing above 3 steps, remove all comments in this file that are
    not your own and do not forget to rename this file from lab3Starter.py
    to variables.py

"""


print("To generate your introduction, I will need some information from you...")
name = input("What's your name? ")
age = input("How old are you? ")
major = input("What is your major? ")

print("Thank you for providing that information!")

print(f"| {name.title()}'s Inputted Information! |\n--------------------\nUser's Name: {name.title()}\nUser's Age: {age.title()}\nUser's Major: {major.title()}\n--------------------")

