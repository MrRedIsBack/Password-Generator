import datetime
import os
import string, random
import re

from art import *
from colorama import Fore

from timeit import default_timer as timer

#opening screen
ascii_art = text2art(text='Password Generator') #declare ascii art
os.system('Password Generator') #title
os.system('cls') #clear the screen
print(f"{Fore.MAGENTA}{ascii_art}{Fore.RESET}") #show ascii art

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

while True:
    try:
        amount = int(input('Amount of passwords to generate: '))
        option = str(input('How complicated would you like the password to be?(1-3): ').lower())
        characters = int(input('Amount of characters: '))
        
        passwords = []
        
        start = timer()
        for i in range(amount):
            try:
            
                if option == '1' or option == 'option 1':
                    result_str = ''.join(random.choice(string.ascii_letters) for i in range(characters))
                    print('Password: ' + result_str)
                    passwords.append(result_str)
                    
                elif option == '2' or option == 'option 2':
                    allchars = string.ascii_letters + string.digits
                    result_str = ''.join(random.choice(allchars) for i in range(characters))
                    print('Password: ' + result_str)
                    passwords.append(result_str)
                    
                elif option == '3' or option == 'option 3':
                    allchars = string.ascii_letters + string.digits + string.punctuation
                    result_str = ''.join(random.choice(allchars) for i in range(characters))
                    print('Password: ' + result_str)
                    passwords.append(result_str)
                    
                else:
                    raise Exception('Invalid response.')
                    pass
                
            except Exception as e:
                print(f"Error: {e}")
                continue
            
        end = timer()
        print(f"Took {end-start} seconds to generate {amount:,} passwords.")
        
    except:
        print('Invalid option, try again.')
        continue
    
    try:
        option = str(input('Would you like to save the passwords?(Y/N): ').lower())
        
        if option == 'y':
            try:
                path = str(input('The path to save the password(s) to: '))
                if amount < 6:
                    
                    for i in range(amount):
                        email = str(input('Email: '))
                        if(re.fullmatch(regex, email)):
                            name = str(input('Name/What is the password for: '))
                            
                            with open(f"{path}\{name}.txt", 'w') as file:
                                file.write(f"Email: {email} \n Password: {passwords[i]}")
                                print(f"Password for {name} saved.")
                                file.close()
                        
                        else:
                            print('Invalid email.')
                
                else:
                    start = timer()
                    
                    with open(f"{path}\passwords.txt", 'w') as file:
                        for element in passwords:
                            file.write(f"{element} \n")
                        file.close()
                        
                    end = timer()
                    print('Passwords saved.')
                    print(f"Took {end-start} seconds to save passwords to {path}\passwords.txt")
            
            except Exception as e:
                print(f'Error: {e}')
                pass
            
        elif option == 'n':
            print('Passwords not saved.')
            continue
        
        else:
            raise Exception('Invalid response.')
            pass
        
    except Exception as e:
        print(f"Error: {e}")
        pass
