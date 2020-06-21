# dictionary.py
#       by: Mesbah Uddin
#           A simple interactive app to get definition of the given word and the app will prompt
#           for the right word if spelling mistake happens.


# Works with the json file that contains word's definitions
import json

# Is responsible for prompting with the correct word if a spelling mistake happens.
from difflib import get_close_matches as sense

# Here the json file is being load.
data = json.load(open("data.json"))


# This function works if nothing worng happens.
def definition(key):
    return data[key]


# This function works to prompt right word if spelling mistake happens.
def guess(key):
    return sense(key, data.keys(), cutoff=0.8)[0]


print("press '/' to quit the program.")

# Algs to run the program and process output.
while True:
    key = input("Enter a word: ").lower()
    if key == "/":
        break

    try:
        try:
            for lines in definition(key):
                print(lines)
        except:
            yn = input(
                f"Did you mean '{guess(key).title()}' instead. Press [Y] if yes or [N] if no: ").upper()
            if yn == "Y":
                for lines in definition(guess(key)):
                    print(lines)
            elif yn == "N":
                print("The word doesn't exists. Please double check it.")
            else:
                print("Wrong Entry.")

    except:
        print("The word doesn't exists. Please double check it.")
