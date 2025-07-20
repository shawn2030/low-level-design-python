from enum import Enum

class Coin(Enum):
    """
    Enum representing the two sides of a coin.
    """
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUARTER = 25
    DOLLAR = 100