from vending_machine import VendingMachine
from coin import Coin
from item import Item

vm = VendingMachine()
vm.inventory.add_item(Item("Soda", 125), 10)
vm.inventory.add_item(Item("Chips", 75), 5)
vm.inventory.add_item(Item("Candy", 60), 3)

vm.display_items()

vm.insert_coin(Coin.DOLLAR)
vm.insert_coin(Coin.QUARTER)
vm.select_item("Soda")  

vm.insert_coin(Coin.DOLLAR)
vm.select_item("Chips")  

vm.cancel_transaction()  
