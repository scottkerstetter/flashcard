"""
Flash Car
"""

# script and version info
script = "flashcard.py"
version = "1.0.0"
author = "S Kerstetter"
created = "2020-12-13"
last_modified = "2020-12-13"

import random
import csv
from sys import argv, exit

script, file_name = argv


# *** START SCRIPT ***
def data_input(file_name):
    card_list = []
    with open(file_name) as infile:
        reader = csv.reader(infile)
        for row in reader:
            q = row[0]
            a = row[1]
            card_list.append([q, a])
    return card_list


def quiz(card_list):
    header = card_list.pop(0)
    print(f"Starting Quiz on {header[0]} and {header[1]} ")
    master_list = card_list.copy()
    input("\nPress ENTER to continue\n")
    while True:
        card = random.choice(card_list)
        card_list.pop(card_list.index(card))
        print("\nQuestion: ", card[0])
        input(">")
        print("Answer: ", card[1])
        input(">")
        if len(card_list) == 0:
            print("Have another go?")
            choice = input("> ")
            if 'yes' in choice:
                card_list = master_list.copy()
                print("Starting again...")
            else:
                print("Exiting program.")
                exit(0)


def answer_key(card_list):
    print("\nFile Contents / Answer Key:")
    for i in range(len(card_list)):
        print(card_list[i][0], '=', card_list[i][1])


# *** Start Program ***
print(f"""
FLASH CARD

Description:
A simple script for drilling flash cards.  Practice makes less bad!

Credits
Script: {script}
Date Created: {created}
Author: {author}
Version: {version}
Last Modified: {last_modified}
""")

card_list = data_input(file_name)

print("Show file contents?")
print("Enter 'yes' or 'no'")

while True:
    choice = input('> ')

    if 'yes' in choice:
        answer_key(card_list)
        break
    elif 'no' in choice:
        break
    else:
        print("Entry not valid.  Try again.")

input("\nPress ENTER to continue\n")

quiz(card_list)
