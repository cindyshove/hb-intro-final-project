# creates a working deck of cards
# this lives inside the final project file
# but it's not the deck I want so i created a blackjack_deck that works better for my program


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
deck = Deck()
print deck