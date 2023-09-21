### Print ASCII Art beginning of program

import random

print("")
intro_ascii_art = \
"""
 __        __   _                            _             
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___       
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \      
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/
"""                                                           
sec_ascii_art = \
"""
   ____                    _____ ___    _      ____                       _ _               
  / ___|___  _ __ ___  _ _|_   _|_ _|  / \    / ___|  ___  ___ _   _ _ __(_) |_ _   _   _   
 | |   / _ \| '_ ` _ \| '_ \| |  | |  / _ \   \___ \ / _ \/ __| | | | '__| | __| | | |_| |_ 
 | |__| (_) | | | | | | |_) | |  | | / ___ \   ___) |  __/ (__| |_| | |  | | |_| |_| |_   _|
  \____\___/|_| |_| |_| .__/|_| |___/_/   \_\ |____/ \___|\___|\__,_|_|  |_|\__|\__, | |_|  
                      |_|                                                       |___/       
"""

print(intro_ascii_art)
print(sec_ascii_art)

#Dictionary for flashcards.

sec_flashcards = {
    "Malware that spread by human action": "Virus",
    "Malware that spread by themselves": "Worm",
    "Disguise themselves as beneficial program": "Trojan",
    "A type of Malware that locates and saves data from users without them knowing about it.": "Spyware",
    "Software that encrypts programs and data until a ransom is paid to remove it.": "Ransomware",
    "A computer program or part of a program that lies dormant until it is triggered by a specific logical event.": "Logic Bomb",
    "Programs that allow hackers to gain access to your computer and take almost complete control of it without your knowledge, escalating user privileges.": "Rootkits",
    "A set of computers that are penetrated by malicious software known as malware that allows an external agent to control their actions.": "Botnet",
    "Type of spam that have purpose of giving up information, usually used in recon phase of a larger attack.": "Phishing",
    "Software vulnerability that has been previously unreported and for which no patch yet exists.": "Zero-Day Vulnerability",  
}

# Adding randomization

flashcard_items = list(sec_flashcards.items())
random.shuffle(flashcard_items)

# Variable to keep track of the number of tries
attempts = 0

# Flashcards asked randomly
for question, response in flashcard_items:
    while True:
        # Display question and have user answer
        user_response = input(f"What is the answer for  {question}? ")
        
       # Number of attempts goes up
        attempts += 1
        
        # Check if the response is correct
        if user_response.lower() == response.lower():
            print("")
            print("Correct!")
            print("")
            break  
        # Move on to the next flashcard
        else:
            print("")
            print("Incorrect. Try again.")
            print("")

# Print the total number of attempts
print(f"You completed all flashcards in {attempts} attempts.")
