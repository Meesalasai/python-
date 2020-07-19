#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
#adding the logic outside of the initialization. This is one way:
#mycards = [(s,r) for s in SUITE for r in RANKS] #list comprehension

class Card:
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank

    def __str__(self):
        return "suite={} rank={}".format(self.suite, self.rank)

    def __lt__(self, other):
        return (RANKS.index(self.rank) < RANKS.index(other.rank))

    def __eq__(self, other):
        return(self.rank == other.rank)

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    #Initialization creates the deck and it all happens inside the class.
    def __init__(self):
        print("Creating New Orderred Deck!")
        self.allcards = [Card(suite = s, rank = r) for s in SUITE for r in RANKS]

    #to shuffle the deck:
    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.allcards) #shuffle all that list above this method is from random lib

    #to split the cards in half:
    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:]) #tuple unpacking #there's 52 cards


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    #initialize the hand:
    def __init__(self, cards):
        self.cards = cards

    #special method for printing out the hand:
    def __str__(self): #it reports back how many cards I have here in this hand that
        return "Contains {} cards".format(len(self.cards)) # that way I know how many cards in the player's hand

    #I can add cards to the hand which is extension
    def add(self, added_cards):
        self.cards.extend(added_cards) #extend my list with the added cards

    #then remove card which pops up card off
    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    #initialize the player:
    def __init__(self, name, hand): #hand object instance
        self.name = name
        self.hand = hand #one of those hand objects

    #players can play a card:
    def play_card(self):
        drawn_card = self.hand.remove_card() #which means they just remove a card and it tells you what cards they place down
        print("{} has placed {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card # and then it return that drawning card

    def remove_war_cards(self): #which means if I have war present then I will call range 3
        war_cards = []
        if len(self.hand.cards) <3:
            return self.hand.cards
        else:
            #both you and computer player both pass 3 cards and they're the same rank and we have war
            for x in range(3):# for these 3 cards
                #war_cards.append(self.hand.remove_card())
                war_cards.append(self.hand.cards.pop()) #and remove those cards
                #if I match with the computer I need to grab those war cards and I will grab them as a list
            return war_cards # i return them as a list

    def still_has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards) != 0 # which returns true if the player still has cards




######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

#Create a new deck and split it in half:
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half() #tuple unpacking

#create both players
comp = Player("Computer", Hand(half1))

name = input("What's your name?")
user = Player(name, Hand(half2))

#It's a kind of automatically play
# Set Round Count
total_rounds = 0
war_count = 0
# Let's play
#I'm going to be doing is automatically playing this game for both the human player and the computer sice they essentially don't have to make any decisions
while user.still_has_cards() and comp.still_has_cards():
    total_rounds +=1
    print("Time for a new round!")
    print("here are the current standings")
    print(user.name+" has the count: " + str(len(user.hand.cards))) #how many cards are left
    print(comp.name+" has the count: " + str(len(comp.hand.cards)))
    print("play a card!")
    print('\n')

# Cards on Table represented by list
    table_cards = []

# Play cards
    c_card = comp.play_card()
    p_card = user.play_card()

# Add that to the actual table_cards list
    table_cards.append(c_card)
    table_cards.append(p_card)

# Check for War! If there's a war?
    if c_card == p_card:
        # the ranking I want actually to compare, that's why [1], because playing cards are tuples
        war_count += 1
        print("we have a match, time for war!")
        print("Each player removes 3 cars 'face down' and the one card face up")
        table_cards.extend(user.remove_war_cards()) #I just take top three cards available
        table_cards.extend(comp.remove_war_cards())

        # Play cards
        c_card = comp.play_card()
        p_card = user.play_card()

        # Add to table_cards
        table_cards.append(c_card)
        table_cards.append(p_card)

        #check to see who has higher rank
        if c_card < p_card:
            print(user.name + " has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name + " has the higher card, adding to hand.")
            comp.hand.add(table_cards)

    else: #no war just checking:
        #check to see who had higher rank
        if c_card < p_card:
            print(user.name + " has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name + " has the higher card, adding to hand.")
            comp.hand.add(table_cards)

print("Great game! It lasted: " + str(total_rounds) + " rounds")
print("A war happened "+str(war_count)+" times")
print("Does the computer still has cards?:")
print(str(comp.still_has_cards()))
print("Does the human still has cards?:")
print(str(user.still_has_cards()))





# Use the 3 classes along with some logic to play a game of war!
