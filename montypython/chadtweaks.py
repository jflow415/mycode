#!/usr/bin/env python3
round = 0           # integer round initiated to 0
while True:        # sets up an infinite loop condition
    round = round + 1     # increase the round counter
    print('Finish the movie title, "Monty Python\'s The Life of ______"') #.title().strip()
    answer = input("Your guess--> ").title().strip()
    # UUUUGGGGHHHHH
    # just figured it out.
    elif answer == "Shrubbery":
        print("You found the super secret answer!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print('Sorry, the answer was Brian.')
        break             # break statement escapes the while loop
    else:                 # if answer was wrong, and round is not yet equal to 3
        print('Sorry. Try again!')

