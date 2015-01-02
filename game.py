#!/usr/bin/env python

"""Future Improvements:
Have gym leader names, actual move names, random pokemon,
smart AI, multiple pokemon, limited number of heals, more moves
"""

from getopt import getopt, error
from random import randint, choice
import sys

if sys.version_info[0] < 3:
    input = raw_input

user_health = 100
opponent_health = 100
user_turn = True
opponent_name = "The Opponent"

def start_game():
    global user_health, opponent_health, user_turn, opponent_name
    user_health = 100
    opponent_health = 100
    user_turn = True
    opponent_name = "the Opponent"
    print("Welcome to the Stadium! DUM DUM DUM!\n"
          "You are playing against " + opponent_name + "!")

def play_game():
    global input, user_health, opponent_health, user_turn
    start_game()
    while user_health > 0 and opponent_health > 0:
        try:
            if user_turn:
                print("Your Health: " + str(user_health))
                print(opponent_name + "'s Health: " + str(opponent_health))
                print("[a] Safe & Consistent Damage Move")
                print("[b] Risky but Potentially Highly Damaging Move")
                print("[c] Heal")
                while user_turn:
                    user_input = str(input("Pick a Move.\n"))
                    if verify_user_move(user_input):
                        perform_move(user_input)
                    else:
                        print("That's not an option.")
            else:
                opponent_move = get_opponent_move()
                perform_move(opponent_move)
            if determine_win():
                return 0
        except KeyboardInterrupt:
            print("\n")
            return 1
    return 0

def verify_user_move(move):
    return move in ("a", "b", "c")

def get_damage(move):
    if move == "a":
        return randint(18, 25)
    elif move == "b":
        return randint(8, 35)
    else:
        return randint(30, 60)

def perform_move(move):
    global user_health, opponent_health, user_turn
    damage = get_damage(move)
    if user_turn:
        if move != "c":
            opponent_health -= damage
            print("You did " + str(damage) + " damage to " +
                  opponent_name + "!")
        else:
            user_health += damage
            print("You gained " + str(damage) + " health points!")
    else:
        print(opponent_name + " chose move " + str(move) + "!")
        if move != "c":
            user_health -= damage
            print(opponent_name + " did " + str(damage) + " damage to you!")
        else:
            opponent_health += damage
            print(opponent_name + " gained " + str(damage) + " health points!")
    user_turn = not user_turn

def get_opponent_move():
    return choice(["a", "b", "c"])

def determine_win():
    global user_health, opponent_health
    if user_health <= 0:
        print(opponent_name + " has won!")
    elif opponent_health <= 0:
        print ("Congratulations! You have won!")

def main(*argv):
    """This function starts the program. Provides help messages when the user asks
    for one as well as when user uses program inappropriately.
    """
    try:
        opts, args = getopt(argv[0][1:],"h",["help"])
    except error as msg:
        print(msg)
        print("for help use --help")
        return 2
    if args and not opts:
        print(help_message)
        return 2
    else:
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print(help_message)
                return 2
            else:
                print(help_message)
                return 2
    while True:
        exit_value = play_game()
        if exit_value:
            return exit_value
        user_choosing = True
        while user_choosing:
            response = str(input("Play again? Enter y or n\n"))
            if response in ("y", "n"):
                user_choosing = False
                if response == "n":
                    return exit_value
            else:
                print("That's not a valid option.")

"""Calls the function to start the program on run. Exits the program after
running is complete either due to user exiting or an error.
"""
if __name__ == "__main__":
    sys.exit(main(sys.argv))