class Burger:
    def __init__(self):
        self.buns = None
        self.patty = None
        self.cheese = None
    
    def setBuns(self, bunStyle):
        self.buns = bunStyle
    
    def setPatty(self, pattyStyle):
        self.patty = pattyStyle

    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle

# the user can decide what kind of bun, cheese or patty they would like to have in their burger

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def addBuns(self, bunStyle):
        self.burger.setBuns(bunStyle)
        return self
    
    def addPatty(self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self
    
    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self
    
    def build(self):
        return self.burger
    
burger = BurgerBuilder()
burger.addBuns("sesame")
burger.addCheese("cheddar")
burger.addPatty("bikini bottom")
burger.build()