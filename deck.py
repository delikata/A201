import random
class Deck(object):
        """Represent a deck o f 52 pl aying cards ."""

        def __init__(self, start_shuffled):
            """Initializes a deck with 52 cards."""
            suits=["H","S","D","C"]
            ranks= list ( range(2, 11)) + ["J", "Q", "K", "A"]
            self.cards=[]
            for suit in suits:
                    for rank in ranks:
                            self.cards.append(Card(suit, rank))
            if start_shuffled:
                    random.shuffle(self.cards)
        def __str__(self):
                res = []
                for card in self.cards:
                    res.append(str(card))
                return '\n'.join(res)

        def has_card(self, card):
            return card in self.cards

        def draw_random_card(self):
            card=random.choice(self.cards)
            self.cards.remove(card)
            return card
        def draw_hand(self, num_cards):
            cards=[ ]
            for _ in range(num_cards):
                    cards.append(self.draw_random_card())
                    return cards
class Card(object) :
        def __init__(self, s , r):
            self.__suit=s
            self.rank=r

        def __str__(self):
                rep = str(self.rank) + self.suit
                return rep
        
        def __eq__(self, other_card):
                t1 = str(self.suit), self.rank
                t2 = other_card.suit, other_card.rank
                return t1==t2
        def __repr__(self):
                return self.__str__()
        
def main():
        deck1=Deck(True)
            
        print("All the cards in the deck:")
        print(deck1.cards)
        print("Does the deck have the Queen of Hearts? True or False")
        print(deck1.has_card(Card("H", "Q")))
        card=deck1.draw_random_card()
        print("A random card from the deck:")
        print(card)
        if deck1.has_card(card):
                print("Something bad happened...")
                print(card, "Shouldn't be in the deck anymore.")
        print("A hand of six random cards:")
        print (deck1.draw_hand(6))

            
if __name__=="__main__":
        main()
   
