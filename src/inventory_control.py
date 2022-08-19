class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.inventory, self.orders = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }, []

    def add_new_order(self, customer, order, day):
        for ingredients in self.INGREDIENTS[order]:
            if not self.inventory[ingredients]:
                return False
            self.inventory[ingredients] -= 1
        self.orders.append({customer, order, day})

    def get_quantities_to_buy(self):
        return {
            ingredient: (
                self.MINIMUM_INVENTORY[ingredient] - self.inventory[ingredient]
            )
            for ingredient in self.inventory
        }

    def get_available_dishes(self):
        return {
            dish
            for dish in self.INGREDIENTS
            if self.inventory[self.INGREDIENTS[dish][0]] > 1
        }
