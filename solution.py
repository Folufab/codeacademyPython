# Create a Menu class
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
# This gives the availability of the menu
  def __repr__(self):
    rep_string = 'The {} Menu is avaiable from {} to {}'.format(self.name, self.start_time, self.end_time)
    print(rep_string)
# This calcualates the cost of an order  
  def calculate_bill(self, purchased_items):
    total_price = 0
    for purchase in purchased_items:
      total_price += self.items.get(purchase)
    return total_price

# Creating the menus

# Brunch Menu
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu('Brunch', brunch_items, '11.00', '16.00')

# Early-bird menu
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('Early-bird', early_bird_items, '15.00', '18.00')

# Dinner menu
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu('Dinner', dinner_items, '17.00', '23.00')

# Kids Menu
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu('Kids', kids_items, '11.00', '21.00')

# Tesing the calculates bill method
first_order = ['pancakes', 'home fries', 'coffee']
brunch_menu.calculate_bill(first_order)
print(brunch_menu.calculate_bill(first_order))

second_order = ['salumeria plate', 'mushroom ravioli (vegan)']
early_bird_menu.calculate_bill(second_order)
print(early_bird_menu.calculate_bill(second_order))

# Creating the Franchises class
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    print('This Franchise is at {}.'.format(self.address))

  def available_menus(self, time):
    avail_menus = []
    if time <= '16.00' and time >= '11.00':
      avail_menus.append('Brunch Menu') 
    if time <= '18.00' and time >= '15.00':
      avail_menus.append('Early Bird Menu')
    if time <= '23.00' and time >= '17.00':
      avail_menus.append('Dinner Menu')
    if time <= '21.00' and time >= '11.00':
      avail_menus.append('Kids Menu')
    return avail_menus

#Creating the Franchises

flagship_store = Franchise("1232 West End Road", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])

new_installment = Franchise("12 East Mulberry Street", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])

# Testing the available menus by time method
print(flagship_store.available_menus('17.00'))

# Creating a new menu
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu('Take a’ Arepa', arepas_items, '10.00', '20.00')

# Creating a new franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

#Creating the Business class

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# Creating new Businesses

first_business = Business("Basta Fazoolin' with my Heart", ['flagship_store', 'new_installment'])

second_business = Business("Take a' Arepa", [arepas_place])


