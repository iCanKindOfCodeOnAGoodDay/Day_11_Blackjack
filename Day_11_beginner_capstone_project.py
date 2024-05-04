"""

    Scott Quashen
    London App Brewery
    100 Days of Python Code: Day 11
    May 03 2024

    ------
    Description:    Black Jack - Beginner Capstone Project
    ------
    
    ------
    Inputs:         Console game - Update to accept 'error' inputs not yet implemented
    ------
    
    ------
    Outputs:        Console game 
    ------
    
    ------
    Dependencies:   Random, os, time
    ------

    ------
    Assumptions:    Developed and tested using Spyder 5.15.7, Python version 3.11.5 on macOS 14.4.1
    ------
    
"""

import random, os, time

# constant declared for global usage in this case
console_art = """

__________.__                 __    
\______   \  | _____    ____ |  | __
 |    |  _/  | \__  \ _/ ___\|  |/ /
 |    |   \  |__/ __ \\  \___|    < 
 |______  /____(____  /\___  >__|_ \
        \/          \/     \/     \/
     ____.              __          
    |    |____    ____ |  | __      
    |    \__  \ _/ ___\|  |/ /      
/\__|    |/ __ \\  \___|    <       
\________(____  /\___  >__|_ \      
              \/     \/     \/      

"""

def main():
         
    """
    
    Description -   Runs our blackjack game, contains a recursive call to main at the end which runs a new game
    ----------
    Input -         CConsole Game
    ----------
    Output -        Console game
    -------

    """ 

    os.system('clear')
    
    time.sleep(.1) # program some lag so that the clear function does not clear the gameplay - it seems to take a split second to complete and happens after other code has ran

    print(console_art)
    
    # when score is calculated,  if bust with an ace, score is decreased by 10 for each in ace in hand, so that the values of the aces are each set to 1
    card_names = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    
    deck = []
    for card in card_names:
        deck.append(card)
        deck.append(card)
        deck.append(card)
        deck.append(card)
        
    player_cards, deck = starting_deal(deck)
    dealer_cards, deck = starting_deal(deck)
    
    player_score = 0
    dealer_score = 0
    
    print('Player Cards:')
    print(player_cards)
    
    player_score = get_score(player_cards, card_names)
    
    print(f'Dealer shows {dealer_cards[1]}')
    dealer_score = get_score(dealer_cards, card_names)
    
    should_ask_if_player_wants_to_hit = True  
    
    while should_ask_if_player_wants_to_hit == True:    
        
        wants_to_hit = input('Do you want to hit? (y or n)')   
        
        if wants_to_hit == 'y':     
            hit_card, deck = hit( deck )
            player_cards.append(hit_card)
            print('Player Cards')
            print(player_cards)     
            player_score = get_score(player_cards, card_names)
            print(player_score)
             
            player_bust = bust_check(player_score)
            
            if player_bust == True:
                print('Player bust, Game Over!')
                should_ask_if_player_wants_to_hit = False

        else:         
            should_ask_if_player_wants_to_hit = False
    
    dealer_needs_to_hit = False
    if dealer_score < 17:
        dealer_needs_to_hit = True
        
    while dealer_needs_to_hit == True:
        
        dealer_hit, deck = hit( deck )
        dealer_cards.append(dealer_hit) 
        dealer_score = get_score(dealer_cards, card_names)   
        dealer_bust = bust_check(dealer_score)
        
        if dealer_bust == True:
            dealer_needs_to_hit = False # exit loop
            print('Dealer Bust, Player wins')
            
        if dealer_score < 17:
            dealer_needs_to_hit = True  
            print('dealer hit')
            
        else:
            dealer_needs_to_hit = False
            print('dealer stays')
            
    print('Dealers Cards: ')
    print(dealer_cards)
    print(dealer_score)
    
    # game over already triggered if somebody busted
    if(player_score < 22):
        if(dealer_score < 22):
            check_who_won(player_score, dealer_score)
    
    play_again = input('play again? (y or n)')
    if play_again == 'y':
        main() # recursive call to re run our blackjack program
            
def get_score( hand, card_names ):  # adjusts score appropriately if user score is over 21 and has an ace  
       
    """
    
    Description -   Loops the hand counting the values for each card name, accounting for the dynamic ace ( 1 or 11 )
    ----------
    Input -         Player hand, or dealer hands, and the cards dictionary for looking up value
    ----------
    Output -        Score
    -------

    """ 

    score = 0 
    for card in hand:
        score += card_names[card]
        
    if score > 21:
        has_ace = False
        for card in hand: 
            if card == 'A':
                score -= 10
    return score

def bust_check( score ): # update this to account for setting the ace to 1, loop through cards, and decrease ace from 11 to 1 if this is the case
    did_bust = False
    if score > 21:
        did_bust = True
    return did_bust

def check_who_won( player_score, dealer_score ):
       
    """
    
    Description -   See who gets the higher score, only called if nobody busts to avoid extra messages
    ----------
    Input -         Both scores
    ----------
    Output -        Output text to console
    -------

    """ 

    if player_score == dealer_score:
        print('tie game')
    elif player_score > dealer_score:
        print('player wins!')
    else:
        print('Dealer wins!')
    
    
def starting_deal( the_deck ): # call this func for the dealer and player
       
    """
    
    Description -   Pulls cards out of the deck and deals 2 random cards to both player and dealer
    ----------
    Input -         Pass in the deck
    ----------
    Output -        Output a starting hand, and the deck *called once for the player and once for the dealer
    -------

    """ 

    cards_got = 0
    starting_hand = []
    while cards_got < 2:   
        random_card_index = random.randint(0, (len(the_deck) - 1)) # choose a random card from the deck
        starting_hand.append(the_deck[random_card_index]) # add a card to either player or dealer's list of card      
        del(the_deck[random_card_index]) # remove the dealt card from the deck
        cards_got +=1 # whoever's hand is being filled will get two cards
        
    return starting_hand, the_deck
        

def hit( the_deck ):
           
    """
    
    Description -   Hit func works for the dealer and the player
    ----------
    Input -         Pass in the deck
    ----------
    Output -        The updated deck, and the hit card
    -------

    """ 

    random_card_index = random.randint(0 , (len(the_deck) - 1))
    hit_card = the_deck[random_card_index]   
    del(the_deck[random_card_index])  
    return hit_card, the_deck

# run
if __name__ == '__main__':
    main()





