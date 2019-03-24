#  File: RPG.py
#  Description: Simulates a simple RPG by defining character classes
#  Student's Name: Johnathan Tran
#  Student's UT EID: jht697
#  Course Name: CS 313E 
#  Unique Number: 54170
#
#  Date Created: 09/18/2017
#  Date Last Modified: 09/21/2017


# Defining class for Weapon with attributes type and damage
class Weapon():
    
    def __init__(self,type,damage):
        self.type = type
        self.damage = damage
        

# Defining class for Armor with attributes type and armor class
class Armor():

    def __init__(self,type,AC):
        self.type = type
        self.AC = AC
    

# Defining classes for Characters
class RPGCharacter():

    # Initializing values for health and spell points
    def __init__(self,health,spell_points,weapon):
        self.health = health
        self.spell_points = spell_points
        self.weapon = Weapon("bare hands",1)
        self.armor = Armor("no armor worn",10)

    # Method for taking off armor 
    def takeOffArmor(self,armor):
        no_armor = Armor("no armor worn",10)
        return(self.name + " is no longer wearing anything.")
    
    # Method for unwielding a weapon
    def unwield(self,weapon):
        weapon.type = Weapon("bare hands",1)
        
        if self.weapon.type == "bare hands":
            return (self.name + " was not wielding anything.")
        else:
            return (self.name + " is no longer wielding anything.")

    # Method for fighting an opponent, deducts weapon damage from opponent health
    def fight(self,opponent):
    
        print(self.name + " attacks " + opponent.name + " with a(n) " + self.weapon.type)
        opponent.health -= self.weapon.damage
        print(self.name + " does " + str(self.weapon.damage) + " damage to " + opponent.name)
        print(opponent.name + " is now down to " + str(opponent.health) + " health.")
    
        opponent.checkForDefeat()
        return

    # Gives current stats for character
    def __str__(self):
        return("\n" + self.name + "\n" + "   Current Health: " + str(self.health) + "\n"
               + "   Current Spell Points: " + str(self.spell_points) + "\n"
               + "   Wielding: " + self.weapon.type + "\n"
               + "   Wearing: " + self.armor.type + "\n"
               + "   Armor Class: " + str(self.armor.AC) +"\n")

    # Checks if character health is at or below zero
    def checkForDefeat(self):
        if self.health <= 0:
            print(self.name + " has been defeated!")
            


# Creating subclass Fighter          
class Fighter(RPGCharacter):
    
    def __init__(self,name):
        self.name = name
        self.health = 40
        self.spell_points = 0
        self.weapon = Weapon("bare hands",1)
        self.armor = Armor("no armor worn",10)

    # Setting weapons for what this character can wield
    def wield(self,weapon):
        if (weapon.type == "dagger"):
            self.weapon = Weapon("dagger",4)
        if (weapon.type == "axe"):
            self.weapon = Weapon("axe",6)
        if (weapon.type == "staff"):
            self.weapon = Weapon("staff",6)
        if (weapon.type == "sword"):
            self.weapon = Weapon("sword",10)
        
        print(self.name + " is now wielding a(n) " + weapon.type)

    # Setting armor for what this character can wear
    def putOnArmor(self,armor):
        if armor.type == "plate":
            self.armor = Armor("plate",2)
        if armor.type == "chain":
            self.armor = Armor("chain",4)
        if armor.type == "leather":
            self.armor = Armor("leather",10)
            
        print(self.name + " is now wearing " + armor.type)
    
    
   
# Creating subclass Wizard
class Wizard(RPGCharacter): 
    
    def __init__(self,name):
        self.name = name
        self.health = 16
        self.spell_points = 20
        self.weapon = Weapon("bare hands",1)
        self.armor = Armor("none",10)
        
    # Allows wizard to only wield a dagger or staff
    def wield(self,weapon):
        if (weapon.type == "staff") or (weapon.type == "dagger"):
            if weapon.type == "staff":
                self.weapon = Weapon("staff",6)
            if weapon.type == "dagger":
                self.weapon = Weapon("dagger",4)
                
            print(self.name + " is now wielding a(n) " + weapon.type)
        
        else:
            return("Weapon not allowed for this character class.")   

    # Doesn't allow the wizard to wear armor
    def putOnArmor(self,armor):
        if armor.type == "none":
            self.armor == Armor("none",10)
            
        return("Armor not allowed for this character class.")
    
    def castSpell(self,spell_name,target):
        
        # Creating spells
        class Spells():
            def __init__(self,spell_name,cost,effect):
                self.spell_name = spell_name
                self.cost = cost
                self.effect = effect
            
        if spell_name == "Fireball":
            Fireball = Spells("Fireball",3,5)
            spell = Fireball

        if spell_name == "Lightning Bolt":
            Lightning_Bolt = Spells("Lightning Bolt",10,10)
            spell = Lightning_Bolt
            
        if spell_name == "Heal":
            Heal = Spells("Heal",6,-6)
            spell = Heal
            
        print(self.name + " casts " + spell_name +  " at " + target.name)

        # Shows various outcomes after the spell is cast
        if spell_name != "Fireball" and spell_name != "Lightning Bolt" and spell_name != "Heal":
            print("Unknown spell name. Spell failed.")
            
        if (self.spell_points < 6):
            print("Insufficient spell points.")
            return

        # Deducts cost from spell points and spell effect from the target health
        target.health -= spell.effect
        self.spell_points -= spell.cost

        # Displays effects if spell Heal is used
        if spell_name == "Heal":
            print(self.name + " heals " + target.name + " for 6 health points.")
            
        else:
            print(self.name + " does " + str(spell.effect) + " damage to " + target.name)
            print(target.name + " is now down to " + str(target.health) + " health.")
            target.checkForDefeat()
        

def main():
    
    # creating valid weapon types and damage values
    dagger = Weapon("dagger",4)
    axe = Weapon("axe",6)
    staff = Weapon("staff",6)
    sword = Weapon("sword",10)
    bare_hands = Weapon("bare hands", 1)

    # creating valid armor types and armor classes
    plateMail = Armor("plate", 2)
    chainMail = Armor("chain", 5)
    leather = Armor("leather",8)
    no_armor = Armor("none",10)

    # creating names of RPG characters
    gandalf = Wizard("Gandalf the Grey")
    aragorn = Fighter("Aragorn")

    # Testing

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)
    
    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(plateMail)
    aragorn.wield(axe)
    
    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)
    
    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)
    
main()
