# hb-intro-final-project
Hackbright final project
Read_me.md

my game is a black jack gambling game
Opening cash balance is $100
Each opening bid is $10.

Start with 4 complete decks of cards
Cards are the value of their face value, 
except face-cards are worth 10 and 
aces are worth either 1 or 11 (up to the player)

player 1 places their bid (any multiple of $10, up to the value of the cash balance)

Player 1 and the dealer are each dealt 2 cards.
one of the dealer's cards is face down (or hidden)
the second of the dealer's cards is face up.

Player 1 chooses if he wants to take  a "hit" (another card)
He keeps doing this until either the total of his cards exceeds 21 or he wants to stop accepting cards
if he exceeeds 21, he loses, and his cash balance is reduced by the bid

if he has black jack, he automatically wins

If he has not lost, it's the dealer's turn.
The dealer turns the hidden card up.
If the total is 17 or under the dealer "holds" (doesn't take any more cards)
if the dealer has black jack then the dealer wins

if no one has lost (exceeded 21) or won (with a black jack), then the two hands are compared and the higher hand wins.
if player 1 has won, then his cash balance is increased by the amount of the bid
if player 1 loses, then his cash balance is decreated by the amount of the bid
it player 1 and the dealer tie, then the cash balance does not change, 

if the cards run out, shuffle the remaining cards and continue

repeat the process until the cash_balance reaches zero or until player 1 wants to take his winnings, and quit while he is ahead.
