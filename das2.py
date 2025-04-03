class GroceryStore:
    def __init__(self, name, apple_kg, apple_price, orange_kg, orange_price):
        self.name = name
        self.apple_kg = apple_kg
        self.apple_price = apple_price
        self.orange_kg = orange_kg
        self.orange_price = orange_price

    def calculate_orlogo(self):
        return (self.apple_kg * self.apple_price) + (self.orange_kg * self.orange_price)


bambaruush = GroceryStore("Бамбарууш", 534, 5000, 487, 10000)
jimshen = GroceryStore("Жимсэн", 764, 4800, 423, 9300)
fruits = GroceryStore("Fruits", 136, 5000, 228, 10000)

delguuruud = [bambaruush, jimshen, fruits]

for delguur in delguuruud:
    print(f"{delguur.name} дэлгүүрийн орлого: {delguur.calculate_orlogo()}")

niit_orlogo = sum(delguur.calculate_orlogo() for delguur in delguuruud)
print(f"\nНийт борлуулалтын орлого: {niit_orlogo}")
