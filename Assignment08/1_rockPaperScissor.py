from random import choice
def judge(user, computer):
    if user == computer:
        return 'equal'
    elif user == "rock":
        if computer == "scissors":
            return 'user'
        else:
            return 'computer'
    elif user == "paper":
        if computer == "rock":
            return 'user'
        else:
            return 'computer'
    elif user == "scissors":
        if computer == "paper":
            return 'user'
        else:
            return 'computer'
def registrarScores(res):
    if res=='user':
        print('user get +1 point.')
        scores['user']+=1
    elif res=='computer':
        print('computer get +1 point.')
        scores['computer']+=1
    else:
        print('Both of us show %s.'%user_choice)
options = ['rock', 'paper', 'scissors']
scores = {'user':0, 'computer':0}
for i in range(10):
    computer_choice = choice(options)
    user_choice = input('play the game(rock, paper, scissors): ')
    print('computer choice: %s'%computer_choice)
    registrarScores(judge(user_choice, computer_choice))
if scores['computer']>scores['user']:
    print('computer wins.')
elif scores['computer']<scores['user']:
    print('user wins.')
else:
    print('we are both winner 5:5. Hooray!')
