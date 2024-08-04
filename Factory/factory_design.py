class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)
# create a factory that will design the burger 

class BurgerFactory:

    def createCheeseBurger(self):
        ingredients = ["bun", "cheese", "beef-patty"]
        return Burger(ingredients)
    
    def createSpecialCheeseBurger(self):
        ingredients =  ["bun", "tomatoe", "lettuce", "cheese", "beef-patty"]
        return Burger(ingredients)
    
    def createVeganBurger(self):
        ingredients = ["bun", "special-sauce", "veggie-patty"]
        return Burger(ingredients)
    
# now that we have our menu, we will specify what we want
burgerRestaurant = BurgerFactory()
burgerRestaurant.createCheeseBurger().print()
burgerRestaurant.createSpecialCheeseBurger().print()
burgerRestaurant.createVeganBurger().print()