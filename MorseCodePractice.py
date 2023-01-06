# THE PURPOSE OF THIS FILE IS TO PRACTICE THE MORSE TABLE THROUGH THE COMMAND LINE
import random

# dictionary mapping the code to each letter
morse_table = {}
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M", "N","O",
            "P","Q","R","S","T","U","V","W","X","Y","Z"]
morse = ["AAAAA","AAAAB","AAABA","AAABB","AABAA","AABAB","AABBA","AABBB","ABAAA","ABAAA","ABAAB",
        "ABABA","ABABB","ABBAA","ABBAB","ABBBA","ABBBB","BAAAA","BAAAB","BAABA","BAABB","BAABB","BABAA",
        "BABAB","BABBA","BABBB"]
#putting the two lists into a dictionary
for i in range(len(letters)):
    morse_table[letters[i]] = morse[i]

def rand_letter(switch=False):
    """Takes a random letter and asks for the morse code equivalent. setting switch to True reverses this and asks for the corresponding letter instead."""
    global running
    if not switch:
        rand = random.choice(letters)
        ind = letters.index(rand)
        answer = input(f"{rand}: ")
        if answer.upper() == morse[ind]:
            print("Correct")
        elif answer.lower() == "exit":
            running = False
            print()
        else:
            print(f"incorrect, {rand} is {morse[ind]}")
        
    else:
        rand = random.choice(letters)
        ind = letters.index(rand)
        key = morse[ind]
        answer = input(f"{key}: ")

        if answer.upper() == "EXIT":
            running = False
            print()
        elif rand == answer:
            print("Correct")
        elif rand != answer:
            print(f"Incorrect. {key} is {rand}")
# MAIN
sw = int(input("Type the number of the desired method:\n[1] Asks for letter \n[2] Asks for the morse\n"))
if sw == 1:
    sw = True
else:
    sw = False
running = True
while(running):
    rand_letter(sw)
    
