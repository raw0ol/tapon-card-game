#!/urs/bin/env python3
from players import Player, CPU
from cards import Deck
import pyinputplus as pyip
import random
from time import sleep

'''
Spanish card game
Single player command line game where you can play up to 3 CPUs.
Last player standing, wins!

How to play:
Select table size between 2-4.
Select player coins. Last player standing collects all coins and wins!
Each player draws card from deck and decides wether to stay or change on their turn.
You are unable to change if the player next in line holds a king(12).
You can stay and hold card if you receive a higher card from player in line before you.
Player with lower card in each round loses coin.
Dearler can draw card from deck if they choose to.
'''

def set_table():
    players_table_size = pyip.inputInt('Enter table size ', max=4, min=2)
    total_CPUs = players_table_size - 1
    create_players(total_CPUs)

def create_players(num_CPUs):
    coins = pyip.inputInt('Enter player coins per game: ', max=6)

    user_name = pyip.inputStr('Enter user name: ')
    Player(user_name=user_name, coins=coins, wins=0, losses=0, ties=0)

    cpu_name_count = 0
    for i in range(num_CPUs):
        level = ['Easy', 'Medium', 'Hard']
        user_name = 'CPU' + str(cpu_name_count + 1)
        cpu_name_count += 1
        difficulty = random.choice(level)
        CPU(user_name=user_name, coins=coins, wins=0, losses=0, ties=0, difficulty=difficulty)

def dealer_call(player, i):
    if player.user_name.startswith('CPU'):
        CPU_dealer(player, i) 
    else:
        player_dealer(player)

def CPU_dealer(player, i):
    print(player.user_name, ' *****DEALER*****\n')
    drawn_cards[player].show_card()
    if player_choice == 'change':
        if drawn_cards[player].val > drawn_cards[player_list[-2]].val:
            print('Dealer stays...')

        elif drawn_cards[player].val == drawn_cards[player_list[(i-1)]].val:
            if player.coins > player_list[i-1].coins and player.coins >= 2: 
                print('Dealer stays...')
            else:
                print('Dealer will change card...')
                drawn_cards[player] = deck.draw_card()        
        else:
            print('Dealer will change card...')
            drawn_cards[player] = deck.draw_card()
        sleep(2)
    else:
         # 4-7 3-4(easy), 4-5(medium), 5-6(hard)
        if drawn_cards[player].val < 5:
            print('Dealer will change card...')
            drawn_cards[player] = deck.draw_card()
        elif drawn_cards[player_list[i-1]].val == 12 and len(player_list) == 2: 
            print('Dealer will change card to...')
        else:
            print('Dealer will change card to...')
        sleep(2)
        drawn_cards[player] = deck.draw_card()
    # drawn_cards[player].show_card()

def player_dealer(player):
    print(player.user_name, ' *****DEALER CARD*****\n')
    drawn_cards[player].show_card()
    dealer_choice = pyip.inputChoice(['stay','change'])

    if dealer_choice == 'change':
        print('Dealer will change card...')
        sleep(3)
        drawn_cards[player] = deck.draw_card()
    else:
        print('Dealer stays...')

def cpu_call(player, player_choice, i):
    if player_choice == 'stay':
        if drawn_cards[player].val < 5:
            print(f'{player.user_name} has chosen to change card...')
            sleep(2)
            drawn_cards[player], drawn_cards[player_list[i+1]] = drawn_cards[player_list[i+1]], drawn_cards[player]
            return 'change'
        else:
            print(f'{player.user_name} has chosen to stay...')
            return 'stay'
    else:
        if drawn_cards[player].val > drawn_cards[player_list[i-1]].val:
            print(f'{player.user_name} has chosen to stay...')
            return 'stay'
        elif drawn_cards[player].val < 5:
            print(f'{player.user_name} has chosen to change card...')
            drawn_cards[player], drawn_cards[player_list[i+1]] = drawn_cards[player_list[i+1]], drawn_cards[player]
            return 'change'
        else:
            return 'stay'

def tie_check(player_list, tie_count):
        if tie_count == len(player_list):
            print('Tie Game')
            for i, player in enumerate(player_list):
                player.ties += 1
            return True
        else:
            return False
#|---------------------------------------------------------------------------------|
#|--------------------------------GAME LOOP----------------------------------------|
#|---------------------------------------------------------------------------------|
deck = Deck()
set_table()
player_list = Player.player_list
random.shuffle(player_list)
drawn_cards = {}

while len(player_list) > 1:
    player_choice = 'stay'
    for i, player in enumerate(player_list):
        drawn_cards[player] = deck.draw_card()
        print('\n', player.user_name)

        if player.user_name.startswith('CPU'):
            if drawn_cards[player].val == 12:
                drawn_cards[player].show_card()
            else:
                print(
'''
+--------+
|        |
|        |
|   ??   |
|        |
|        |
+--------+
''')
        else:
            drawn_cards[player].show_card()

    for i, player in enumerate(player_list):
        if drawn_cards[player].val == 12:
            print(player.user_name, '|-^-^-^-| King, you\'re safe this round \n')
            player_choice = 'stay'
            sleep(2)
            continue

        if player != player_list[-1] and drawn_cards[player_list[i+1]].val == 12:
            print(player.user_name, 'Kneel to the King, you\'re unable to trade.\n')
            sleep(2)
            continue

        # DEALER FUNCITON
        if player == player_list[-1]:
            dealer_call(player, i)
            sleep(2)

        # CPU Non-Dealer
        elif player.user_name.startswith('CPU'):
            player_choice = cpu_call(player, player_choice, i)
            sleep(2)
            
        #player Non-Dealer
        else:
            if player_choice == 'change':
                drawn_cards[player].show_card()

            player_choice = pyip.inputChoice(['stay','change'])
            if player_choice == 'change':
                print(f'{player.user_name} has chosen to change card...')
                drawn_cards[player], drawn_cards[player_list[i+1]] = drawn_cards[player_list[i+1]], drawn_cards[player]
                print('Your new card...')
                drawn_cards[player].show_card()
            else:
                print('You have chosen to stay.')
        sleep(2)

    sleep(3)
    print('\n---------------- Player Cards -----------------------')
    for i, player in enumerate(player_list):
        print('\n', player.user_name)
        drawn_cards[player].show_card()
    print('----------------- Player Cards ----------------------\n')

    # make a list to find lowest card of all players
    min_list =[]
    for i in drawn_cards.values():
        min_list.append(i.val)

    x = min(min_list)
    sleep(2)
    tie_count = 0

    # find the lower card of all players
    for i, player in enumerate(player_list):
        if drawn_cards[player].val == x and drawn_cards[player].val != 12:
            player_list[i].coins -= 1
            print(f'{player.user_name} tosses coin to the pile')
            if player.coins == 0:
                tie_count += 1

    tie = tie_check(player_list, tie_count)
    if tie:
        print(player_list, 'This should be end of game')
        break
            
    for i, player in enumerate(player_list):
        if player.coins == 0:
            player.losses += 1
            player_list.remove(player)
            print(f'{player.user_name} has been ELIMINATED!')
        else:
            continue

    if len(player_list) == 1:
        print('End of game!')
        player_list[0].wins += 1
        print(player_list[0].user_name + ' Wins the game!')

    sleep(3)
    print('\n*************** Current Score ***********************')
    for player in player_list:
        print(f'{player.user_name}: Coins:{player.coins}')
    print('***************** Current Score ***********************')

    # swittches dealer
    Player.switch_dealer(player_list)

    # clear list/dict
    min_list.clear()
    drawn_cards.clear()
    sleep(6)