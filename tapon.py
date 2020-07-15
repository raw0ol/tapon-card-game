#!/urs/bin/env python3

import pyinputplus as pyip
import random
import pprint
from time import sleep
#from playermenu import set_table # unable due to cross circular import error

class Card:

    def __init__(self, suit, val, name): #TODO add img argument
        self.suit = suit
        self.val = val
        self.name = name

    def show_card(self):
        print(f'{self.name}({self.val}) of {self.suit}')

    def __repr__(self):
        return f'{self.name}({self.val}) of {self.suit}'


class Deck:
    game_cards = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five':5,
                'Six': 6, 'Seven': 7, 'Jack':10, 'Queen': 11, 'King':12}

    suit_type = ['Copas', 'Bastos', 'Oro', 'Espadas']

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in Deck.suit_type:
            for key, value in Deck.game_cards.items():
                self.cards.append(Card(s, value, key))
        random.shuffle(self.cards)

    def show(self):
        for c in self.cards:
            c.show_card()

    def draw_card(self):
        if self.cards == []:
            self.build()
            random.shuffle(self.cards)
        return self.cards.pop()
    
    @staticmethod
    def p_draw(player):
        card_cls_obj = deck.draw_card()
        drawn_cards[f'{player}'] = card_cls_obj
    
    
class Player():
    player_list = []
    
    def __init__(self, user_name, coins, wins, losses, ties): # plan to add avatar and level argument
        self.user_name = user_name
        self.coins = coins
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.make_list()
        #self.avatar = avatar
        #self.level = level

    def make_list(self):
        Player.player_list.append(self)

    @classmethod
    def switch_dealer(clss, p_list):
        p_list.insert(0, p_list.pop())

    def __repr__(self):
        return f"{self.user_name} - Coins:{self.coins} - W:{self.wins} - L:{self.losses} - T:{self.ties}"


class CPU(Player):
    def __init__(self, user_name, coins, wins, losses, ties,  diff):
        super().__init__(user_name, coins, wins, losses, ties)
        self.diff = diff

    def __str__(self):
        return f"{self.user_name} - Coins:{self.coins}- Level:{self.diff}"

class AI(CPU):
    def __init__(self, easy, medium, hard):
        self.easy = easy
        self.medium = medium
        self.hard = hard


def create_players(num_players, num_CPU):
    coins = pyip.inputInt('Coins per game: ', max=6)
    cpu_count = 0
    for p in range(num_players):
        user_name = pyip.inputStr('Enter user name: ')
        # if user_name in player_list[], re do user_name input
        wins = 0
        losses = 0
        ties = 0
        # if user_name in playerStats.txt, update variables
        Player(user_name, coins, wins, losses, ties)

    for c in range(num_CPU):
        difficuly = ['Easy', 'Medium', 'Hard']
        user_name = 'CPU' + str(cpu_count + 1)
        cpu_count += 1
        wins = 0
        losses = 0
        ties = 0
        level = random.choice(difficuly)
        CPU(user_name, coins, wins, losses, ties, level)


def set_table():
    # have button with total table size (2)-(4)-(6)
    table_size = pyip.inputInt('Enter table size ', max=6, min=2)
    print('Select number of non-CPU players')
    # have button (+ 1) for every non CPU player
    p_count = pyip.inputInt(max=table_size, min=1)
    CPUs = table_size - p_count
    create_players(p_count, CPUs)


def dealer_call(player):
    if player.user_name.startswith('CPU'):
        CPU_dealer(player) 
    else:
        player_dealer(player)


def CPU_dealer(player):
    print(player.user_name, 'is the Dealer. Your current card is...')
    drawn_cards[f'{p[i]}'].show_card()

    if player_choice == 'change':
        if drawn_cards[f'{p[i]}'].val > drawn_cards[f'{p[(i-1)]}'].val:
            print('Dealer stays with', end=' ')

        elif drawn_cards[f'{p[i]}'].val == drawn_cards[f'{p[(i-1)]}'].val:
            if p[i].coins > p[i-1].coins and p[i].coins >= 2: 
                print('Dealer stays with', end=' ')
            else:
                print('Dealer will change to...')
                sleep(2)
                Deck.p_draw(player)
                
        else:
            print('Dealer will change to...')
            sleep(2)
            Deck.p_draw(player)


    else:
        if drawn_cards[f'{p[i]}'].val < 5: # random less than 5-7
            print('Dealer will change to...')
            sleep(2)
            Deck.p_draw(player)
        elif drawn_cards[f'{p[i-1]}'].val == 12 and len(p) == 2: 
            # what happens if all three other players have a king???
            # drawn_cards[f'{p[i-2]}'].val == 12 and len(p) == 3:
            # # drawn_cards[f'{p[i-3]}'].val == 12 and len(p) == 4:
            # make deck = 0 and and a suffle function to incrase change of next card getting a king 
            print('Dealer will change to...')
            sleep(2)
            Deck.p_draw(player)
         

    print(player.user_name, drawn_cards[f'{p[i]}'])


def player_dealer(player):
    print(player.user_name, 'is the Dealer. Your current card is...')
    drawn_cards[f'{p[i]}'].show_card()
    print(f'{p[i].user_name}', end=' ')
    dealer_choice = pyip.inputChoice(['stay','change'])
    print()

    if dealer_choice == 'change':
        print('Dealer will Change to ...')
        sleep(2)
        Deck.p_draw(player) 
        
    else:
        print('Dealer stays with', end=' ')

    print(player.user_name, drawn_cards[f'{p[i]}'])


def cpu_call(player, p_choice):
    if p_choice == 'stay':
        if drawn_cards[f'{p[i]}'].val < 5:
            print(player.user_name, 'has chosen to change card: ' + str(drawn_cards[f'{p[i]}']))
            sleep(2)
            drawn_cards[f'{p[i]}'], drawn_cards[f'{p[i+1]}'] = drawn_cards[f'{p[i+1]}'], drawn_cards[f'{p[i]}']
            print('New card... ', player.user_name, drawn_cards[f'{p[i]}'])
            return 'change'
        else:
            print(player.user_name,'has chosen to stay with: ' + str(drawn_cards[f'{p[i]}']))
            return 'stay'

    else:
        if drawn_cards[f'{p[i]}'].val > drawn_cards[f'{p[i-1]}'].val:
            print('CPU player has chosen to stay...')
            print(player, drawn_cards[f'{p[i]}'])
            return 'stay'
        else:
            if drawn_cards[f'{p[i]}'].val < 5:
                print(player.user_name, 'has chosen to change card: ' +  str(drawn_cards[f'{p[i]}']))
                drawn_cards[f'{p[i]}'], drawn_cards[f'{p[i+1]}'] = drawn_cards[f'{p[i+1]}'], drawn_cards[f'{p[i]}']
                print('New card... ', player.user_name, drawn_cards[f'{p[i]}'])
                return 'change'

def tie_check(p_list, tie_count):
        if tie_count == len(p_list):
            print('Tie Game')
            for i, player in enumerate(p_list):
                player.ties += 1
            return True
            
set_table()
deck = Deck()

# deck.show()
p = Player.player_list
random.shuffle(p)
drawn_cards = {}

print()



# Main Game Loop
while len(p) > 1:
    for i, player in enumerate(p):
        Deck.p_draw(player)
    #     print(player.user_name, drawn_cards[f'{p[i]}'])
    
    for i, player in enumerate(p):
        if drawn_cards[f'{p[i]}'].val == 12:
            print(player.user_name, end=' ')
            drawn_cards[f'{p[i]}'].show_card()
        else:
            print(player.user_name,'Not a king')

    print()
    # Use show Function to display each Players card per their request
    player_choice = 'stay'

    for i, player in enumerate(p):
        if drawn_cards[f'{p[i]}'].val == 12:
            drawn_cards[f'{p[i]}'].show_card()
            print(player.user_name, 'You have a King!')
            player_choice = 'stay'
            sleep(2)
            print()
            continue


        if p[i] != p[-1] and drawn_cards[f'{p[i+1]}'].val == 12:
            drawn_cards[f'{p[i]}'].show_card()
            print(player.user_name, 'You are stuck with your card, unable to trade')
            sleep(2)
            print()
            continue


        # DEALER FUNCITON
        if p[i] == p[-1]:
            dealer_call(player) # pass on player_choice too???
            sleep(2)
            print()

        # CPU Non-Dealer
        elif player.user_name.startswith('CPU'):
            player_choice = cpu_call(player, player_choice)
            sleep(2)
            # print()
            
        #player Non-Dealer
        else:
            print(f'{p[i].user_name}', drawn_cards[f'{p[i]}'], end=' ')
            player_choice = pyip.inputChoice(['stay','change'])

            if player_choice == 'change':
                print(player.user_name, 'has chosen to change card: ' +  str(drawn_cards[f'{p[i]}']))
                drawn_cards[f'{p[i]}'], drawn_cards[f'{p[i+1]}'] = drawn_cards[f'{p[i+1]}'], drawn_cards[f'{p[i]}']
                print('New card... ', end=' ')
                drawn_cards[f'{p[i]}'].show_card()
            else:
                player_choice = 'stay'
        sleep(3)
        print()


    #TODO make function
    # Displays players name and drawn card at end of round
    for i, player in enumerate(p):
        for k, value in drawn_cards.items():
            print(player.user_name, drawn_cards[f'{p[i]}']) # can use drawn_cards[f'{p[i]}'].name, .val, .suit
            break
    print()

            
    #TODO make function
    # make a list to find lowest card of all players
    print('Finding player(s) with minimum number')
    min_list =[]
    for i in drawn_cards.values():
        min_list.append(i.val)

    sleep(2)
    
    x = min(min_list)
    print(min_list, x, 'This is the minimum number')

    sleep(2)

    tie_count = 0

    #TODO make function 
    # find the lower card of all players
    for i, player in enumerate(p):
        if drawn_cards[f'{p[i]}'].val == x and drawn_cards[f'{p[i]}'].val != 12:
            p[i].coins -= 1
            print(player, 'This Player has the lowest card')
            
            if p[i].coins == 0:
                tie_count += 1

    tie = tie_check(p, tie_count)
    if tie == True:
        print(p, 'This should be end of game')
        break
            
    for i, player in enumerate(p):
        if p[i].coins == 0:
            p[i].losses += 1
            #TODO make function to update playerstats.txt
            p.remove(p[i])
            print(player, 'ELIMINATED!')
        else:
            continue
    
    sleep(2)
    

    print()

   
    if len(p) == 1:
        print('End of game!')
        p[0].wins += 1
        #TODO make function to update playerstats.txt
        print(p[0].user_name + ' Wins the game!')
        print(p[0])
        # break from main game loop and exit...
        
            

    
    print()
    print('*************************************************')
    for player in p:
        print(player)
    print('*************************************************')
    print()

    # swittches dealer
    Player.switch_dealer(p)

    # clear list/dict
    min_list.clear()
    drawn_cards.clear()


    sleep(8)




#BUG if there are two players left, and dealer has lower card then he should trade automatically. 

#BUG found when last two players where 11, one of them was eliminated and the other was made king
 # for c in range(p):
    #     if c.coins == 0



#TODO VISUAL set the deck close to p[-1]
        
#TODO if coins == 0, delete player from list

#TODO Last player standing Wins game

#TODO  def __str__(self):
            #return f"{self.user_name} - Coins:{self.coins} W:{self.wins} - L:{self.losses}" - SHOW ONLY DURING MENU VISUAL SCREEN
            # Rule of thumb:  __repr__ is for developers, __str__ is for customers.


# # IDEAS

# # have level up best being at 1. everytime you lose money, you level up...
# # when you have enough money, you can level down. when a new player enters, coins are redistrubuted in a smart way
# # lets say ther are 40 active players, then if 3 more people join, coins are redistributed???


# # def change_avatar(self, new_avatar):
# #    pass




# # # # # NOTES

# # # # # print(Player.player_list[0].user_name)
# # # # # print(Player.player_list[0].coins)
# # # # # print(Player.player_list[0].wins)
# # # # # print(Player.player_list[0].losses)
# # # # # print(Player.player_list[0].diff)

# # # # # print(deck.cards[0].suit)
# # # # # print(deck.cards[0].val) 
# # # # # print(deck.cards[0].name)

# # # # # pprint.pprint(drawn_cards)
# # # # # print()
# # # # # pprint.pprint(p)
# # # # # print()