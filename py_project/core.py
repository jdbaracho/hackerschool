import random

welcomeMsg = "Welcome!\nHow many credits will you deposit?\n"
playMsg = "Do you want to play?(yes/no)\n"
betMsg = 'How much is your bet?\n'
invalidAmountMsg = 'Invalid amount'
notEnoughMsg = 'Not enough chips'
winMsg = 'You won! +'
endMsg = 'Out of chips, sorry!'

elements = ('#', '§', '&', '@', '£', '€', '$')
weigth = (50, 40, 30, 20, 10, 5, 1)

class SlotMachine:
        chips = 0
        slots = ['$', '$', '$']

        def __init__(self):
            self.chips = int(input(welcomeMsg))
            print(self)
            print('Chips: ' + str(self.chips) + '\n')

        def bet(self):
            bet = int(input(betMsg))
            if(bet not in (5, 10, 20, 70, 200, 1000, 100000)):
                print(invalidAmountMsg)
                return -1
            
            if(bet > self.chips):
                print(notEnoughMsg)
                return -1

            return bet

        def win(self, bet):
            print(winMsg + str(bet*2))
            self.chips = self.chips + bet*2

        def play(self):

            bet = self.bet()
            while(bet == -1):
                bet = self.bet()

            self.chips -= bet
            self.slots = random.choices(elements, weigth, k = 3)
            print(self)

            if(self.slots[0] == self.slots[1] == self.slots[2]):
                match self.slots[0]:
                    case '#':
                        if(bet == 5):
                            self.win(bet)

                    case '§':
                        if(bet == 10):
                            self.win(bet)

                    case '&':
                        if(bet == 20):
                            self.win(bet)

                    case '@':
                        if(bet == 70):
                            self.win(bet)

                    case '£':
                        if(bet == 200):
                            self.win(bet)

                    case '€':
                        if(bet == 1000):
                            self.win(bet)

                    case '$':
                        if(bet == 100000):
                            self.win(bet)
            
            print('Chips: ' + str(self.chips) + '\n')
            return self.chips


        def __str__(self):
            return '\n-------\n|' + self.slots[0] + '|' + self.slots[1] \
                + '|' + self.slots[2] + '|\n-------'


sm = SlotMachine()



while(1):

    match input(playMsg):
        case 'no':
            break

        case 'yes':
            if(sm.play() < 5):
                print(endMsg)
                break
            

