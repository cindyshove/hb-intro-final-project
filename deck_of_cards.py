
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        letters = {1:'A', 11:'J', 12:'Q', 13:'K'}
        letter = letters.get(self.rank, str(self.rank))
        return "<Card %s %s>" % (letter, self.suit)

class Deck:
	def __init__ (self):
		self.cards=[]
		for suit in ("spade", "hearts", "diamonds", "clubs"):
			for i in range(1,14):
				self.cards.append(Card(i,suit))

	def __repr__(self):
		for i in self.cards:
			print i

#if I want to print the deck
#deck = Deck()
#print deck


# #create a class called deck_of_cards with values for BLACKJACK
# class Card(object):
# 	def __init__(self, suit, rank, value):
# 		self.rank = rank
# 		self.suit = suit
# 		self.value = value


# #create the first_suit, repeating up to 13
# # manually line by line
# ace_of_hearts = Card("hearts", "ace", 11)
# two_of_hearts = Card("hearts", "two", 2)
# three_of_hearts = Card("hearts", "three", 3)
# four_of_hearts = Card("hearts", "four", 4)
# five_of_hearts = Card("hearts", "five", 5)
# six_of_hearts = Card("hearts", "six", 6)
# seven_of_hearts = Card("hearts", "seven", 7)
# eight_of_hearts = Card("hearts", "eight", 8)
# nine_of_hearts = Card("hearts", "nine", 9)
# ten_of_hearts = Card("hearts", "ten", 10)
# jack_of_hearts = Card("hearts", "jack", 10)
# queen_of_hearts = Card("hearts", "queen", 10)
# king_of_hearts = Card("hearts", "king", 10)


# #REFACTORING - USE CLASSES: 

#     def __repr__(self):
#         letters = {1:'A', 2: 2, 3: 3....11:'J', 12:'Q', 13:'K'}

# hand = [Card(1, 'spade'), Card(10, 'club')]



#REFACTORING: 
# define the ace separately because it has two variables
# but the program totals it as 11 as long as it's not over 21.
# if the total of 





