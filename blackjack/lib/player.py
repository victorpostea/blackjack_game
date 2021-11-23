from lib.card import Card
from lib.deck import Deck


class Player:
  """
  Player
  """

  def __init__(self, name:str=None) -> None:
    self.name = name
    self.cards = []

  def __str__(self) -> str:
    return self.name

  def add_card(self, card: Card) -> None:
    ''' Adds Cards to the deck array

    Args:
      card: The card instance to be added to the player's hand

    Returns:
      None

    '''
    self.cards.append(card)

  def pick_cards(self, deck: Deck, num_cards: int) -> None:
    ''' Picks number of cards from the deck to start the game. It adds the cards to the player's hand

    Args:
      deck: The deck instance
      num_cards: the amount of cards to be picked

    Returns:
      None

    '''
    print("{0} picks {1} card(s) from the deck...".format(self.name, num_cards))

    # retrieve the cards from the deck
    cards = deck.get_cards(num_cards)
    # add the cards to the player's hand
    for card in cards:
      self.cards.append(card)

  def show_cards(self) -> None:
    ''' Shows the cards in the player's hand

    Args:
      None

    Returns:
      None

    '''
    print("{0} cards are:".format(self.name))
    for card in self.cards:
      print("\t" + str(card))

  def get_points(self) -> int:
    ''' Retrieves the player's points

    Args:
      None

    Returns:
      points: Player's points

    '''
    points = 0
    for card in self.cards:
      points += card.get_value()
    return points

  def play(self, deck: Deck) -> None:
    ''' A single loop of the game where player gets to choose a card and checks for blackjack or bust

    Args:
      deck: The deck instance

    Returns:
      None

    '''
    continue_play = True

    while continue_play:
      # check if the player can pick another card
      points = self.get_points()
      if points >= 21:
        print("{0} cannot pick another card as (s)he has {1} points already".format(self.name, points))
        break
      else:
        print("{0}, do you want to pick another card? [y/n]".format(self.name))
        choice = input(" > ")
        if choice == 'y':
          # get another card from the deck
          self.pick_cards(deck, 1)
          self.show_cards()
        elif choice == 'n':
          continue_play = False
        else:
          print("Did not recognize your choice, please try again")


