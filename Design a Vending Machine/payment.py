from coin import Coin
from typing import Dict

class PaymentProcessor:
    def __init__(self):
        self.inserted_amount = 0
        self.coin_inventory = {
            Coin.PENNY : 100,
            Coin.NICKEL : 100,
            Coin.DIME : 100,
            Coin.QUARTER : 100,
            Coin.DOLLAR : 100
        }

    def insert_coint(self, coin: Coin):
        self.inserted_amount += coin.value
        self.coin_inventory[coin] += 1

    def refund(self):
        amount = self.inserted_amount
        self.inserted_amount = 0
        return amount
    
    def can_make_change(self, change: int) -> bool:
        # Simplified greedy logic
        temp = change
        for coin in sorted(Coin, key=lambda x: x.value, reverse=True):
            while temp >= coin.value and self.coin_inventory[coin] > 0:
                temp -= coin.value
        return temp == 0

    def deduct_change(self, change: int) -> Dict[Coin, int]:
        change_map = {}
        for coin in sorted(Coin, key=lambda x: x.value, reverse=True):
            while change >= coin.value and self.coin_inventory[coin] > 0:
                change_map[coin] = change_map.get(coin, 0) + 1
                self.coin_inventory[coin] -= 1
                change -= coin.value
        return change_map if change == 0 else {}