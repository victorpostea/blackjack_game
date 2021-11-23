import json
import random
from typing import List
from lib.card import Card

class Deck:
  """
  Deck of cards
  """

  def __init__(self) -> None:
    self.cards = []

    # load the cards from the file
    with open("data/cards.json") as data_file:
      data = json.load(data_file)
      for element in data:
        card = Card(element['name'], element['suit'])
        self.cards.append(card)

  def __str__(self) -> str:
    deck_str = 'Deck is: \n'
    for card in self.cards:
      deck_str += '\t' + str(card) + '\n'
    return deck_str

  def size(self) -> int:
    ''' Retrieves the size of the deck (how many cards are in the deck)

    Args:
      None

    Returns:
      The size of the deck

    '''
    return len(self.cards)

  def shuffle(self) -> None:
    '''Shuffles the cards in the deck

    Args:
      None

    Returns:
      None

    '''
    print("\nShuffling the cards...")
    random.shuffle(self.cards)
    print("Cards shuffled.\n")

  def get_card(self) -> Card:
    '''Gets the top card of the deck

    Args:
      None

    Returns:
      The top card of the deck

    '''
    return self.cards.pop()

  def get_cards(self, num_cards: int) -> List[Card]:
    '''Method that returns multiple cards from the deck

    Args:
      Number of cards to retrieve

    Returns:
      List of cards from the top of the deck

    '''
    round_cards = []
    for i in range(num_cards):
      card = self.get_card()
      round_cards.append(card)
    return round_cards

