from item import Item

class Inventory:
    def __init__(self):
        self.items = {}         # str : int. name --> quantity
        self.item_map = {}      # str : item

    def add_item(self, item:Item, quantity: int):
        self.items[item.name] = self.items.get(item.name, 0) + quantity
        self.item_map[item.name] = item

    def is_available(self, item_name:str) -> bool:
        return self.items.get(item_name, 0) > 0
    
    def deduct(self, item_name:str):
        if self.is_available(item_name):
            self.items[item_name] -= 1

    