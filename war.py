from warclass import *

#Game Setup:

#Players:
player_one = Player("One")
player_two = Player("Two")

#Decks:
new_deck = Deck()
new_deck.shuffle()

#Splitting
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

#Game True
game_on = True

#Game
#Counting the rounds
round_num = 0 

#While game_on
while game_on:
    
    #Showing the round num:
    round_num += 1
    print(f"Round {round_num}")
    
    #Checking if player lost:
    if len(player_one.all_cards) == 0:
        print("Player One is out of cards!\nPlayer Two wins!")
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print("Player Two is out of cards!\nPlayer One wins!")
        game_on = False
        break
    
    #Starting a new round:
    #Player_one_cards are the cards that are being used
    #Not equal to all_cards, that represents the whole deck
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
   
    #while at_war
    at_war = True
    
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            at_war = False
        
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            
            at_war = False
            
        else:
            print("WAR!!!")
            
            if len(player_one.all_cards) > 5:
                print("Player One unable to declare war!")
                print("Player Two wins!")
                game_one = False
                break
                
            elif len(player_two.all_cards) > 5:
                print("Player Two unable to declare war!")
                print("Player One wins!")
                game_one = False
                break
                
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
 