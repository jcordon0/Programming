# -*- coding: utf-8 -*-
class PlayerCharacter: #creating a class that will hold stats for a character
    
    def __init__(self, health, armor_rating, attack_power): #stats health,armor,attack are created inside the class
        
        self.__health = health #this identifies health
        self.__armor_rating = armor_rating #this identifies armor
        self.__attack_power = attack_power #this identifies attack
             
    def set_health(self, health):
        self.__health = health #this sets health as itself

    def set_armor_rating(self, armor_rating):
        self.__armor_rating = armor_rating #this sets armor as itself

    def set_attack_power(self, attack_power):
        self.__attack_power = attack_power #this sets attack as itself
        
    def get_health(self):
         return self.__health #this allows me to get the values for health once they have been identified and set
     
    def get_armor_rating(self):
         return self.__armor_rating #this allows me to get the values for armor once they have been identified and set
     
    def get_attack_power(self):
         return self.__attack_power #this allows me to get the values for attack once they have been identified and set

def main():
    
    hit_points = int(input("How many health points does your character have?\n")) #input for player health
    
    while (hit_points > 100) or (hit_points < 1): #loop statement to ensure values are 1-100
            print("Enter a value between 1 - 100\n")
            hit_points = int(input("How many health points does your character have?\n"))
            
    armor = int(input("How many armor points does your character have?\n")) #input for player armor
    
    while (armor > 20) or (armor < 1): #loop statement to ensure values are 1-20
            print("Enter a value between 1 - 20\n")
            armor = int(input("How many armor points does your character have?\n"))
            
    attack_points = int(input("How many attack points does your character have?\n")) #input for player attack
    
    while (attack_points > 20) or (attack_points < 1): #loop statement to ensure values are 1-20
            print("Enter a value between 1 - 20\n")
            attack_points = int(input("How many attack points does your character have?\n"))
    
    selection = input("Would you like to be a wizard or a rogue?\n") #class selection for user knowledge
    
    if selection.lower() == 'wizard': #conditional statement looking for string that will identify class
        print(f'\nYou have chosen {selection} class: ')
        wizard = PlayerCharacter(hit_points,armor,attack_points) #will pass inputs, will set and get the values in PlayerCharacter
        print(f'Your {selection} stats are...\nHealth: {wizard.get_health()}\nArmor: {wizard.get_armor_rating()}\nAttack: {wizard.get_attack_power()}')
        print(wizard) #prints the object location for wizard
    elif selection.lower() == 'rogue':
        print(f'\nYou have chosen {selection} class: ')
        rogue = PlayerCharacter(hit_points,armor,attack_points) #then gets values for each attribute from the class
        print(f'Your {selection} stats are...\nHealth: {rogue.get_health()}\nArmor: {rogue.get_armor_rating()}\nAttack: {rogue.get_attack_power()}')
        print(rogue) #prints the object location for rogue, to make sure they are two different objects for PlayerCharacter
    else:
        print('\nThat is not a class selection.')
    
if __name__ == "__main__":
    
    main()