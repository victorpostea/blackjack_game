from lib.deck import Deck
from lib.player import Player

class Dealer(Player):
  """
  Dealer player
  """

  def __init__(self) -> None:
    super(Dealer, self).__init__()
    self.name = 'Dealer'

  def show_cards(self, show_first_only:bool=False) -> None:
    ''' Displays dealers cards and masks the second one if show_first_only is True

    Args:
      show_first_only: show only the first card when the flag is set to True

    Returns:
      None

    '''
    print(self.name + ' cards:')
    for index, card in enumerate(self.cards):
      if index == 0 or show_first_only == False:
        print("\t" + str(card))
      else:
        print("\t********************") # mask the other cards in the hand

  def play(self, deck: Deck) -> None:
    '''Dealer's round of play

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
        print("{0} cannot pick another card as he has {1} points already".format(self.name, points))
        break
      elif points < 17:
        # always pick another card if dealer has less than 17 points
        self.pick_cards(deck, 1)
      else:
        continue_play = False

    # show all the cards at the end of the play
    self.show_cards()

