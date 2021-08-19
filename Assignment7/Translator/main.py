def readFile():
    try:
        myFile = open('translate.txt', 'r')
        wordList = myFile.read().split('\n')
        for i in range(len(wordList)):
            if i%2==0:
                tempDic={}
                tempDic['english']=wordList[i]
            else:
                tempDic['persian']=wordList[i]
                words.append(tempDic)
        myFile.close()
    except:
        print('We can\'t found translate.txt')
def addNewWord():
        myFile = open('translate.txt', 'a')
        eng = input('english: ')
        per = input('persian: ')
        myFile.write('\n%s\n%s' %(eng, per))
        myFile.close()
        words.append({'english':eng, 'persian':per})
def translater(FROM, TO):
    sentenceList = input('Give me sentence: ').split()
    translationList=[]
    for letter in sentenceList:
        dotFlag = False
        if letter.find('.')!=-1 and letter.find('.')==len(letter)-1:
            letter = letter[:letter.find('.')]
            dotFlag = True
        tmp = letter
        for i in range(len(words)):
            if words[i][FROM]==letter:
                tmp = words[i][TO]
                break
        if dotFlag:
            translationList.append(tmp+'.')
        else:
            translationList.append(tmp)
    print('Translate: ' + ' '.join(translationList))
def starterMenu():
    readFile()
    while True:
        userChoice = int(input('\n1- add new word\n2- translation english2persian\n3- translation persian2english\n4- exit\n'))
        if userChoice==1:
            addNewWord()
        elif userChoice==2:
            translater('english', 'persian')
        elif userChoice==3:
            translater('persian', 'english')
        elif userChoice==4:
            exit()
        else:
            print('Are you lost? :)\n')
words = []
starterMenu()
