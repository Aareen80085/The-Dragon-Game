import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        # Base attack power (small, but will be buffed later)
        self.attack_power = random.randint(5, 10)

    def attack(self, enemy):
        # Damage is between 1 and current attack power
        damage = random.randint(1, self.attack_power)
        enemy.health -= damage
        print(f"{self.name} hits {enemy.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0


class Dragon:
    def __init__(self):
        self.name = "Dragon"
        self.health = 120
        self.attack_power = random.randint(50, 100)

    def attack(self, player):
        damage = random.randint(1, self.attack_power)
        player.health -= damage
        print(f"{self.name} burns {player.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0


# ---------- GAME LOOP ----------
print(" Welcome to Dragon Slayer! ")
player_name = input("Enter your name: ")
player = Player(player_name)
dragon = Dragon()

print("\nThe battle begins!\n")

while player.is_alive() and dragon.is_alive():
    print(f"\nYour Health: {player.health} | Dragon Health: {dragon.health}")
    print("1. Attack")
    print("2. Run Away")

    choice = input("Choose an action: ")

    if choice == "1":
        player.attack(dragon)
        if dragon.is_alive():
            dragon.attack(player)

    elif choice == "2":
        # Village quest instead of game over
        print(" You ran away and reached a nearby village!")
        print("A villager approaches you and offers you a quest!")
        print("If you unlock this chest, you will receive magical powers to defeat the dragon!")

        secret = random.randint(10, 99)
        attempts = 5
        buff_unlocked = False

        while attempts > 0:
            guess = input(f"Enter a 2-digit number (Attempts left: {attempts}): ")

            # Validate input type
            if not guess.isdigit():
                print("Invalid input! Enter numbers only.")
                continue

            # Hints based on number of digits
            elif len(guess) == 1:
                print("Hint: The number has 2 digits. You're missing the tens and hundreds places!")
                continue

            elif len(guess) == 3:
                print("Hint: It's a 2-digit number. You're including the hundreds place!")
                continue

            guess_int = int(guess)

            #Check The guess and provide feedback
        
            if guess_int == secret:
                print("Correct! The villager grants you a legendary buff!")
                buff_unlocked = True
                break
            elif guess_int < secret:
                print("Too low!")
            else:
                print("Too high!")

            attempts -= 1

        if buff_unlocked:
            print(" You gained the 'Dragon Breaker' buff!")
            print("Your attack power is now insanely high!")
            # Huge buff so the dragon dies in ~1–2 hits
            player.attack_power = 1000
        else:
            print("You failed the quest. You return to the dragon unbuffed...")

        print("You return to fight the dragon!\n")
        # Go back to main battle loop
        continue

    else:
        print("Invalid choice!")

# Game ending
if player.is_alive() and not dragon.is_alive():
    print(" You defeated the Dragon! Your legend will be told for generations! ")
elif dragon.is_alive() and not player.is_alive():
    print(" The Dragon defeated you... Try again! ")
