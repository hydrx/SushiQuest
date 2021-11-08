import random
from sushi_pkg.utilities import Header


class RiceGame:
    def __init__(self):
        self.guess = 0
        self.grains = random.randint(16, 20)

    def run_game(self):
        won_game = False
        Header().print_header("RICE GAME")
        print("RICE FIEND: There are around 16,000 to 20,000 grains of rice "
              "in this sack."
              "\nYou get two tries to guess how many there are! "
              "I'll round to the nearest thousand.")
        # print(self.grains * 1000)
        for i in range(0, 2):
            while True:
                self.guess = input(
                    "\nRICE FIEND: How many grains of rice do you think there "
                    "are? ")
                try:
                    self.guess = int(self.guess)
                    break
                except:
                    print(">> That's not a valid number!")
                    continue
            self.guess = (lambda n: round(n / 1000) * 1000)(self.guess)
            i += 1
            if self.guess == self.grains * 1000:
                print(
                    f"RICE FIEND: You guessed right! There's about"
                    f" {self.guess:,} grains of rice in this sack. Well, "
                    f"this one's all yours.")
                won_game = True
                break
            else:
                print("RICE FIEND: Nope sorry, try again.")
                continue
        return won_game


# RiceGame().run_game()
