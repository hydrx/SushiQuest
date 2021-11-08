import random
from sushi_pkg.utilities import Header


def early_exit(choice):
    if choice.lower() == 'q' or choice.lower() == 'quit':
        return True


class InsultGame:
    def run_game(self):
        """Run the Insult Game."""
        Header().print_header("INSULT THUMB WRESTLING")
        # Set variables for Player and FishMonger classes
        player = Player()
        fish_monger = FishMonger()
        # Set rules of game
        print("FISHMONGER: You think you're so special?? With your plain "
              "outfit and empty pockets, you look like a default "
              "character.\nLet's see what you've got!! Bring your best "
              "insults and thumb wrestle me. Let me set down my clarinet..\n"
              "It's three rounds to win. If you can't handle it, type 'q' or "
              "'quit' at any time, weakling.\n")
        # Play 3 rounds of insult game
        for i in range(0, 3):
            choice, choices = player.choose_insult()
            if early_exit(choice):
                break
            insult = player.deal_damage(choice, choices)
            fish_monger.respond(insult)
            i += 1
        # Add early exit without damage calculation
        if early_exit(choice):
            return False
        # Result based on total damage
        # print(fish_monger.fishmonger_hp)
        if fish_monger.fishmonger_hp > 0:
            print(">> Player: Barnacle head!")
            print("\nFISHMONGER: Loser!! Your insults are trash! "
                  "GOMIHITO!!!")
            return False
        else:
            print(">> Player: Shut your mouth, you mediocre clarinet player!")
            print("\nFISHMONGER: Ach! I can't believe this. Take the fish "
                  "and scram!")
            return True


class FishMonger:
    def __init__(self):
        """Hitpoints for Fish Monger."""
        self.fishmonger_hp = 5
        self.insult_responses = {"Great": ["How dare you!?",
                                           "My thumb! You *dolphin noise*!!"],
                                 "Okay": ["You take that back!",
                                          "Keep your grubby thumb off me!"],
                                 "Bad": ["I've heard better comebacks from a "
                                         "tuna sandwich.",
                                         "Ha! When I'm done with you, "
                                         "your thumb will be a boneless "
                                         "filet."]}

    def respond(self, insult):
        """Respond based on Player's insult."""
        if insult == 3:
            self.fishmonger_hp = self.formatted_response(insult, "Great")
        elif insult == 1:
            self.fishmonger_hp = self.formatted_response(insult, "Okay")
        else:
            self.fishmonger_hp = self.formatted_response(insult, "Bad")
        # print(self.fishmonger_hp)
        return self.fishmonger_hp

    def formatted_response(self, insult, damage):
        """Calculate damage based on response."""
        rand_response = self.insult_responses[damage]
        print(f"\nFISHMONGER: {random.choice(rand_response)}\n")
        self.fishmonger_hp -= insult
        return self.fishmonger_hp


class Player:
    def __init__(self):
        """Initialise insults and amount of damage dealt."""
        self.more_damage = 3
        self.less_damage = 1
        self.no_damage = 0
        self.insults = [{"Great": "Do you catch fish for the S.S. Diarrhea?",
                         "Okay": "What's that smell? Oh, it's you...",
                         "Bad": "You smell like rotten fish!"},
                        {"Great": "You bear a great resemblance to your "
                                  "thumb.",
                         "Okay": "If I had a dollar for every brain you don't "
                                 "have, I'd have a dollar.",
                         "Bad": "Your thumb's floppier than a fish!"},
                        {"Great": "If there was a loser contest, you'd still "
                                  "come in second place, you big loser!",
                         "Okay": "Go take a long walk off a short pier!",
                         "Bad": "You're slower than a sea snail."},
                        {"Great": "Hey pal, you just blow in from stupid "
                                  "town?",
                         "Okay": "You're dumber than a beached jellyfish.",
                         "Bad": "You look like you take swimming lessons at "
                                "the YMCA.", },
                        {"Great": "I hope you swallow a fish bone and choke "
                                  "on it!",
                         "Okay": "You one-cent, one-eyed bottom feeder!",
                         "Bad": "I'll fin-ish you off!"}]
        self.used_insults = []

    def choose_insult(self):
        """Choose an insult against the Fish Monger."""
        insult_set = random.choice(self.insults)  # Show random set of insults
        self.used_insults.append(insult_set)  # Track insults shown
        self.insults.remove(insult_set)  # Remove used insults
        # Shuffle insults order
        shuffled = list(insult_set.items())
        random.shuffle(shuffled)
        insult_set = dict(shuffled)
        # Show insults
        n = 0
        choices = {}
        for key, value in insult_set.items():
            print(f"[{n + 1}] {value}")
            choices[n + 1] = {key: value}
            n += 1
        # Check valid input
        while True:
            choice = input("\nInsult: ")
            if early_exit(choice):
                break
            elif choice not in str(choices.keys()):
                print("Please choose a valid option.")
                continue
            else:
                break
        return choice, choices

    def deal_damage(self, choice, choices):
        """Deal appropriate damage"""
        choice = int(choice)
        if "Great" in choices[choice].keys():
            print(">> Great insult, big damage dealt.")
            return self.more_damage
        elif "Okay" in choices[choice].keys():
            print(">> Okay insult, some damage dealt.")
            return self.less_damage
        else:
            print(">> Bad insult, no damage dealt.")
            return self.no_damage


# InsultGame().run_game()
