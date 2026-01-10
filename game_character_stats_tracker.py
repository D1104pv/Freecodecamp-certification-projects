class GameCharacter:
    # Instantiating
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property # getter to check character name
    def name(self):
        return self._name
    
    @property # getter to check current health
    def health(self):
        return self._health
    
    @health.setter # setter to update health with validation
    def health(self, new_health):
        if new_health < 0 or new_health > 100:
            raise ValueError("Health can't be negative or greater than 100")
        self._health = new_health

    @property # getter to check current mama
    def mana(self):
        return self._mana
    
    @mana.setter # setter for mana with validation
    def mana(self, new_mana):
        if new_mana < 0 or new_mana > 50:
            raise ValueError("Mana can't be negative or greater than 10")
        self._mana = new_mana
    
    @property # getter for current level
    def level(self):
        return self._level
    
    def level_up(self): # method to increase character's level by 1
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")
    
    def __str__(self):
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}\n"
    

hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)  # Displays the character's stats

hero.health -= 30  # Decreases health by 30
hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)  # Displays the stats after leveling up