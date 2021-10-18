from random import choice

choice_list = ['✋', '🤚']
score = [0, 0, 0] # pc1-pc2-user
for i in range(5):
    pc1 = choice(choice_list)
    pc2 = choice(choice_list)
    user = input('choose between ✋/🤚: ')
    if pc1==pc2==user:
        print(f'pc1{pc1} pc2{pc2} you{user} - draw')
    elif pc1==pc2:
        print(f'pc1{pc1} pc2{pc2} you{user} - user+')
        score[2]+=1
    elif pc1==user:
        print(f'pc1{pc1} pc2{pc2} you{user} - pc2+')
        score[1]+=1
    elif pc2==user:
        print(f'pc1{pc1} pc2{pc2} you{user} - pc1+')
        score[0]+=1
winner = score.index(max(score))
if winner==0:
    print('pc1 win.')
elif winner==1:
    print('pc2 win.')
else:
    print('you win.')