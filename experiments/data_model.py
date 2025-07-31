import collections
from random import choice

Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
    suits = 'spades diamond clubs hearts'.split()

    def __init__(self):   
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        # This enabled to use the object as an iterable
        return self._cards[position]

suit_values = dict(spades=3, hearts=2, diamond=1, clubs=0)

def spades_high(card: Card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__=="__main__":
    new_card = Card(rank='2', suit='hearts')
    deck = FrenchDeck()

    print(f"Deck length: {len(deck)}")
    print(f"First card: {deck[0]}")
    print(f"Random card: {choice(deck)}")

    print(f"Top 3 cards: {deck[:3]}")
    print("------")
    for suit in deck.suits:
        print(f"Card Value for {suit}: {spades_high(Card('5', suit))}")

    print("------")

    # Sorting example
    for i, card in enumerate(sorted(deck, key=spades_high)):
        if i < 8 or i >= 44:
            print(f"Card {i}: {card.rank} of {card.suit} - Value: {spades_high(card)}")
