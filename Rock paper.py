import random
##If you want your runs in Thonny to match Moodle, instead of being random & different each time, 
## then you should UNCOMMENT the random.seed(1234) command below.  
## This command is inserted automatically in Moodle, to make the pseudo-random number
## generator always produce the same "random" sequence, so the test cases are always the same for grading.
#random.seed(1234)               

def main():           
    # Don't change the order of this choiceList!
    actionChoices = ['rock', 'paper', 'scissors']
    
    print('==> Rock, Paper, Scissors <==')
    print()
    howManyRounds = int(input('Enter number of rounds: '))
    print()
    
    
    # You'll want to initialize some variables here
    human = 0
    computer = 0
    
    for round in range(1, howManyRounds + 1):
        print(f'Round {round}')
        # Prompt and get the human's choice for the round
        human_choice = input('   Human, choose rock, paper, or scissors: ')
        
        # make computer player's choice for the round using random.choice(...)
        comp_choice = random.choice(['rock', 'paper', 'scissors'])
        
        # then print the computer player's choice
        print(f'   Computer chooses {comp_choice}')
        
        #figure out who won this round, display appropriate mesage, update running score
        if comp_choice == 'rock':
            if human_choice == 'paper':
                print('   Paper covers rock')
                human = human + 1
                print(f'   Current score: human {human}, computer {computer}')
            elif human_choice == 'scissors':
                print('   Rock smashes scissors')
                computer = computer + 1
                print(f'   Current score: human {human}, computer {computer}')
            elif human_choice == 'rock':
                print('   Tie')
                print(f'   Current score: human {human}, computer {computer}')
        if comp_choice == 'paper':
            if human_choice == 'rock':
                print('   Paper covers rock')
                computer = computer + 1
                print(f'   Current score: human {human}, computer {computer}')
            elif human_choice == 'scissors':
                print('   Scissors cuts paper')
                human = human + 1
                print(f'   Current score: human {human}, computer {computer}')
            elif human_choice == 'paper':
                print('   Tie')
                print(f'   Current score: human {human}, computer {computer}')
        if comp_choice == 'scissors':
            if human_choice == 'rock':
                print('   Rock smashes scissors')
                human = human + 1
                print(f'   Current score: human {human}, computer {computer}')
            elif human_choice == 'paper':
                print('   Scissors cuts paper')
                computer = computer + 1
                print(f'   Current score: human {human}, computer {computer}')
            elif human_choice == 'scissors':
                print('   Tie')
                print(f'   Current score: human {human}, computer {computer}')
        print()
    #print the final score and overall win/loss/tie message
    if human > computer:
        print(f'Final score: human {human}, computer {computer}')
        print('Human wins, computer loses.')
    if human < computer:
        print(f'Final score: human {human}, computer {computer}')
        print('Computer wins, human loses.')
    elif human == computer:
        print(f'Final score: human {human}, computer {computer}')
        print('Tie')
main()                  