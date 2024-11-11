class Rewards:
    def __init__(self):
        self.coins = 0
    
    def add_coins(self, amount):
        self.coins += amount
        # Update level unlocking logic here
