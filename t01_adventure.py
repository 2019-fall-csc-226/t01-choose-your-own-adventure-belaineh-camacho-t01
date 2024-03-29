######################################################################
# Author: Immanuela Belaineh       TODO: Change this to your names
# Username: belainehi              TODO: Change this to your usernames
#
# Assignment: T01: Choose Your Own Adventure
#
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem
######################################################################
from time import sleep

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False         # You start out not dead, which is good.

# Asks the user to input their name.
username = input("What do they call you, unworthy adversary? ")

#########################################################################################################
# The following is the first part of the story. Don't change this section.
print()
print("Welcome,", username, ", to the labyrinth.")
sleep(delay)
print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print()
sleep(delay)

#########################################################################################################
# This is an example chapter. Your story will follow a similar structure.

# You will learn more by NOT copy and pasting this section. Write your section on your own, and when you get stuck,
# refer to this code to help you get unstuck. Of course, raise your hand if you get really stuck.

direction = input("Which direction would you like to go? [North/South/East/West]" )

if direction == "North":
    # Good choice!
    print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
    sleep(delay)
elif direction == "South":
    # Oh... Bad choice
    print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
    sleep(delay)
    print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
    print("Running seems like a good idea now. But... it's really, really dark.")
    print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
    print("He eats you. You are delicious.")
    dead = True
else:
    # Neutral choice
    print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here! \n")
    sleep(delay)

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. \n ")
    quit()

#########################################################################################################
# TODO Add your part of the story here. Keep in mind you may NOT be coming right after the example above.

print ("Congratulations! You have survived so far. But the journey does not end for the gold still lays undiscovered. \n ")
sleep (delay*2)
direction=input("Which way would you like to go now? Choose wisely North, East, West or South?\n")
if direction =="East":
    print ("You have proven how worthy you are so the gods have decided to reward you with Gold. \n You are rich now go home and spread your wealth! \n")
elif direction == "North":
    print("This trip is only for the worthy. You have been found unworthy and the gods have sacked your soul.\n")
    quit()
elif direction=="West":
    print ("Some wolves come by and urinate all over your stuff, then eat your face off. Tragic, you could have been rich but now you're dead.")
else:
    print ("You were found by a group of robbers. They know you have enough food and gold to last you days. They loot you and leave you for the bears.")
sleep (delay)
print ("You're in the cave, its night time and you began to hear screams from one of two paths.")
direction = input("Which path will you take, East or West? Choose wisely.")
if direction=="East":
    print ("""Congratulation! You have found the exit and havce made it out with only a few scratches and maybe some broken bones, but look on the bright side, atleast you're alive.
     Look on the bright side, you have experienced the deadly cave and came out with your life. Yay!""" )
else:
    print ("You become curious of the screams and follow them. You stumble upon a group of rich cave partiers and they invite you to join them")
    quit()
# TODO Don't forget to check if your user is dead at the end of your chapter!



#########################################################################################################

# The following is the end of the story. Don't change this section, unless you really want to
# (though it may not be used in the final story. Or will it...)
print("Look at that! You made it to the end of the story without dying! ")
print("Congratulations... now go play again and find an interesting way to perish. ")
print("Try again by hitting the green play button.")
