from random import *

answers = ['It is certain',	'Reply hazy, try again', 'Don’t count on it', 'It is decidedly so',
           'Ask again later', 'My reply is no', 'Without a doubt', 'Better not tell you now',	'My sources say no',
           'Yes definitely', 'Cannot predict now', 'Outlook not so good', 'You may rely on it',
           'Concentrate and ask again',	'Very doubtful', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes',
           'Signs point to yes']

print('Hello, stranger! I\'m here to answer all of your questions', '\n', 'Tell me, what\'s your name?')
name = input()
print('Nice to meet you,', name)

while True:
    print('What question do you have for me?')
    q = input()
    print(choice(answers))
    print('Do you have any more questions? Y - yes, N - no')
    n = input()
    while n.lower() != 'y' and n.lower() != 'n':
        print('Please, enter the valid letter (Y - yes, N - no)')
        n = input()
    if n.lower() == 'y':
        continue
    elif n.lower() == 'n':
        break

print('Thank you for asking me questions today!\nCome back any time for new answers!')
