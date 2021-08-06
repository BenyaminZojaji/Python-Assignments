import requests
from random import choice
from time import sleep
def findAllSubIndexes(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) 
wordSite = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(wordSite)
WORDS = list(response.content.splitlines())
WORDS = list(map(lambda i: i.decode(), WORDS))
while True: # beacuse the list has many words like 'aba'! which is not feeling good
    pcWord = choice(WORDS).lower()
    if len(pcWord)>3: 
        break 
health = 10 
outputWord=(len(pcWord)*'-')
while '-' in outputWord and health>0:
    print(('\n%s                 HP:%s') %(outputWord,health))
    sleep(0.5)
    userInput=input('Give me single char: ')[0].lower()
    showIndexes=list(findAllSubIndexes(pcWord, userInput))
    if showIndexes:
        for i in showIndexes:
            outputWord=outputWord[:i]+pcWord[i]+outputWord[i+1:]
    else:
        health-=1
        print('nah! there is no %s in my word' %userInput)
    sleep(0.5)
print('\n%s is correct. well done! Dont tell anyone you are an engenius.\n'%pcWord) if not '-' in outputWord else print('\nLOSER!\n')