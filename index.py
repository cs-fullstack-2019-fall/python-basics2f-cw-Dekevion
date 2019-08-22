import random
# Write some Python code that has three variables called greeting, my_name, and my_age.
# Intialize each of the 3 variables with an appropriate value,
# then print out the example below using the 3 variables and two different approaches for formatting Strings.
# Using concatenation and the + and 2) Using an f-string. Sample output:
#
# greeting = 'Hello'
# my_name = 'Dekevion'
# my_age = 20
#
# intro = print(greeting + ", my name  is " + my_name + ' and my age is ' + str(my_age))
#
#
# intro2 = print(f'{greeting} my name is {my_name}  and my age is {my_age}')

#Write some Python code that asks the user for a secret password. Create a loop that quits with the user's quit word.
# If the user doesn't enter that word, ask them to guess again.

# ask4word = input('what is the secret word')
# abc = ''
# while abc != ask4word:
#     abc = input('what is the secret word again?')
#     if abc == ask4word:
#         print('correct')
#     else:
#         print('ask again')


#Write some Python code using f-strings that prints 0 to 50 three times in a row (vertically).

# for loop in range(0, 51, 1):
#     print(f'{loop, loop, loop}')

#
# string = 'banana'
# for x in string:
#     print(x)

#Write some Python code that create a random number and stores it in a variable.
# Ask the user to guess the random number.
# Keep letting the user guess until they get it right, then quit.


numRandom2 = random.randint (1, 5)
guess_something = 6

while guess_something != numRandom2:
    guess_something = int(input('enter num'))
    if guess_something != numRandom2:
        print('wrong, try again')
    else:
        print('correct')



