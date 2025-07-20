from inventory import Inventory
from payment import PaymentProcessor
from item import Item
from coin import Coin

class VendingMachine:
    def __init__(self):
        self.inventory = Inventory()
        self.payment = PaymentProcessor()

    def display_items(self):
        for name, qty in self.inventory.items.items():
            item = self.inventory.item_map[name]
            print(f"{name} - Price: {item.price}, Qty: {qty}")

    def insert_coin(self, coin: Coin):
        self.payment.insert_coin(coin)
        print(f"Inserted {coin.name}, total: {self.payment.inserted_amount}")

    def select_item(self, item_name: str):
        if not self.inventory.is_available(item_name):
            print("Item out of stock.")
            return

        item = self.inventory.item_map[item_name]
        if self.payment.inserted_amount < item.price:
            print("Insufficient funds.")
            return

        change = self.payment.inserted_amount - item.price
        if not self.payment.can_make_change(change):
            print("Cannot dispense due to lack of change.")
            return

        self.inventory.deduct(item_name)
        change_map = self.payment.deduct_change(change)
        self.payment.inserted_amount = 0
        print(f"Dispensing {item.name}")
        print(f"Returning change: {change_map}")

    def cancel_transaction(self):
        refund = self.payment.refund()
        print(f"Transaction cancelled. Refunded: {refund}")
