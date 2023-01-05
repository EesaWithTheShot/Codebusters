# THE PURPOSE OF THIS FILE IS TO PRACTICE THE BACONIAN TABLE THROUGH THE COMMAND LINE
import random

# dictionary mapping the code to each letter
baconian_table = {}
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M", "N","O",
            "P","Q","R","S","T","U","V","W","X","Y","Z"]
bacon = ["AAAAA","AAAAB","AAABA","AAABB","AABAA","AABAB","AABBA","AABBB","ABAAA","ABAAA","ABAAB",
        "ABABA","ABABB","ABBAA","ABBAB","ABBBA","ABBBB","BAAAA","BAAAB","BAABA","BAABB","BAABB","BABAA",
        "BABAB","BABBA","BABBB"]
#putting the two lists into a dictionary
for i in range(len(letters)):
    baconian_table[letters[i]] = bacon[i]

def rand_letter(switch=False):
    """Takes a random letter and asks for the Baconian equivalent. setting switch to True reverses this and asks for the corresponding letter instead."""
    global running
    if not switch:
        rand = random.choice(letters)
        ind = letters.index(rand)
        answer = input(f"{rand}: ")
        if answer.upper() == bacon[ind]:
            print("Correct")
        elif answer.lower() == "exit":
            running = False
            print()
        else:
            print(f"incorrect, {rand} is {bacon[ind]}")
        
    else:
        rand = random.choice(letters)
        ind = letters.index(rand)
        key = bacon[ind]
        answer = input(f"{key}: ").upper()
        
        if key == "ABAAA":
            if answer == "I" or answer == "J":
                print("Correct")
            else:
                print(f"Incorrect. {key} is {rand}")
        elif key == "BAABB":
            if answer == "U" or answer == "V":
                print("Correct")
            else:
                print(f"Incorrect. {key} is {rand}")
        elif answer == "EXIT":
            running = False
            print()
        elif rand == answer:
            print("Correct")
        elif rand != answer:
            print(f"Incorrect. {key} is {rand}")
# MAIN
sw = int(input("Type the number of the desired method:\n[1] Asks for letter \n[2] Asks for the cipher\n"))
if sw == 1:
    sw = True
else:
    sw = False
running = True
while(running):
    rand_letter(sw)
    
