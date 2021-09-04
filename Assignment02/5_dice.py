from random import randint
from time import sleep
from termcolor import colored
while True:
    temp=randint(1,6)
    if temp==6:
        print('%i . lets Dice again!' %(temp))
        sleep(2)
    else:
        playagain=input('%i .wanna play again?(y/n) ' %(temp))
        if playagain=='n':
            break
print(colored('You are out of Dice program.', 'red'))
