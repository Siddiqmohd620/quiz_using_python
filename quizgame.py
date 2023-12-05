print('WELCOME TO MY QUIZ GAME!')

playing = input('DO YOU WANT TO PLAY?')
if playing.lower() != "yes":
    print('Thank You')
    quit()

print('Okay lets play:') 
score=0

answer = input('WHAT DOES CPU STANDS FOR? ')
if answer.lower() == 'central processing unit':
    print('Correct!')
    score+=1
else:
    print('Incorrect!')

answer = input('WHAT DOES RAM STANDS FOR? ')
if answer.lower() == 'random access memory':
    print('Correct!')
    score+=1
else:
    print('Incorrect!')

answer = input('WHAT DOES PSU STANDS FOR? ')
if answer.lower() == 'power supply':
    print('Correct!')
    score+=1
else:
    print('Incorrect!')

answer = input('WHAT DOES GPU STANDS FOR? ')
if answer.lower() == 'graphics processing unit':
    print('Correct!')
    score+=1
else:
    print('Incorrect!')


print('you got ' +str(score)+ ' questions')