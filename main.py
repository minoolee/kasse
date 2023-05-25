
# Kasse

# Menu items
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Menu
class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_menu(self):
        for index, item in enumerate(self.items, start=1):
            print(f"{index}, {item.name} - {item.price}")

    def remove_item(self, item):
        self.items.remove(item)

# Table
class Table:
    def __init__(self, number):
        self.number = number
        self.order = []

    def add_order(self, item):
       self.order.append(item)

    def display_order(self):
        for index, item in enumerate(self.order, 1):
            print(f"{index}. {item.name} - {item.price}")



praga = MenuItem('Praga', 7)
tee = MenuItem("Tee", 7)
caffee = MenuItem("Caffee", 6)

print(praga.price)

mondayMenu = Menu()
mondayMenu.add_item(praga)
mondayMenu.add_item(tee)
print(mondayMenu.display_menu())
mondayMenu.remove_item(tee)
menu = mondayMenu.display_menu()
print(menu)

order1 = Table(5)
order1.add_order("tee")
show = order1.display_order()
print(show)
