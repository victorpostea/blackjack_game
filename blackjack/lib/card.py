
class Card:
  '''
  Card representation, A suit can be: Hearts, Clubs, Diamonds or Spades
  '''

  def __init__(self, name: str, suit: str) -> None:
      self.name = name
      self.suit = suit

  def __str__(self) -> str:
    return "{0} of {1}".format(self.name, self.suit)

  def get_value(self) -> int:
    '''Retrieves the value of the card

    Args:
      None

    Returns:
      The value of the card in points - int

    '''
    if self.name == "Ace":
      return 11
    elif self.name == "King" or self.name == "Queen" or self.name == "Jack":
      return 10
    else:
      return int(self.name)
