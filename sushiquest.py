import random

from sushi_pkg.utilities import Header, Player, option_check
from sushi_pkg.rice_game import RiceGame
from sushi_pkg.insult_game import InsultGame


class SushiQuest:
    """Overall class for the game."""

    def __init__(self):
        self.quest_items = ["Nori", "Rice", "Fish"]
        self.inventory = []
        self.games_played = {"Rice Game": 0, "Insult Game": 0}
        # self.menu = ""
        self.player_name = ""

    def run_game(self):
        Header().print_header("S U S H I  Q U E S T")
        # Get player name and welcome player
        player = Player()
        self.player_name = player.get_player()
        print(f"Hello, {self.player_name}!")
        print(f"Welcome to SUSHI QUEST.")
        print(
            f"Type 'q' to quit or type the number of the corresponding "
            f"option.")
        # Show menu - main room A
        gm.main_room()


class Menu:
    def __init__(self):
        self.quest_received = False
        # self.talked_nori_hoarder = False
        # self.talked_sushi_eater = False
        # self.talked_rice_fiend = False
        # self.talked_fish_monger = False
        self.talked_NPC = set()
        self.sushi_lover = False

    def main_room(self):
        """Show menu - main room"""
        Header().print_header("You are in the main room.")
        if not self.quest_received:
            # main room A, before receiving quest
            print("There's an unknown figure behind a long, wooden table.")
            options = {"1": "[1] Talk to the unknown figure."}
            # option = self.option_menu(options)
            option_check(options)
            self.quest_received = NPC().sushi_chef(self.quest_received)
            self.main_room()
        else:
            # main room B, once quest received
            options = {"1": "[1] Speak to the SUSHI CHEF",
                       "2": "[2] Leave the room"}
            option = option_check(options)
            if option == "1":
                NPC().sushi_chef(self.quest_received)
                self.main_room()
            else:
                self.lobby()

    def lobby(self):
        """Show menu - lobby"""
        Header().print_header("You are in the lobby.")
        options = {"1": "[1] Talk to the figure on the left.",
                   "2": "[2] Talk to the figure on the right.",
                   "3": "[3] Go outside.",
                   "4": "[4] Return to the main room."}
        if "nori_hoarder" in self.talked_NPC:
            options["1"] = "[1] Talk to NORI HOARDER."
        if "sushi_eater" in self.talked_NPC:
            options["2"] = "[2] Talk to SUSHI EATER."
        option = option_check(options)
        if option == "1":
            NPC().nori_hoarder()
            self.lobby()
        elif option == "2":
            self.sushi_lover = NPC().sushi_eater(self.sushi_lover)
            self.lobby()
        elif option == "3":
            self.outside()
        else:
            self.main_room()

    def outside(self):
        """Show menu - outside"""
        Header().print_header("You are outside.")
        options = {"1": "[1] Talk to the figure on the left.",
                   "2": "[2] Talk to the figure on the right.",
                   "3": "[3] Return to the lobby."}
        if "rice_fiend" in self.talked_NPC:
            options["1"] = "[1] Talk to RICE FIEND."
        if "fish_monger" in self.talked_NPC:
            options["2"] = "[2] Talk to FISH MONGER."
        option = option_check(options)
        if option == "1":
            rice_fiend = NPC()
            rice_fiend.rice_fiend()
            self.outside()
        elif option == "2":
            NPC().fish_monger()
            self.outside()
        else:
            self.lobby()


class NPC:
    def sushi_chef(self, quest):
        """Talk to SUSHI CHEF."""
        if not quest:
            # Quest not yet received
            # Dialogue round 1
            print("\nYou walk up to the unknown figure. "
                  "They stare at you for a moment before finally speaking.")
            print("SUSHI CHEF: I am the Sushi Chef. I'm afraid I don't have "
                  "any sushi to offer you.\n")
            options1 = {"1": f"[1] Ask \"Why not?\""}
            option_check(options1)
            # Dialogue round 2
            print("\nSUSHI CHEF: *Sighs* I'm out of ingredients. "
                  "Will you gather some for me?\n")
            options2 = {"1": "[1] \"Okay.\"", "2": "[2] \"No.\""}
            while True:
                option2 = option_check(options2)
                if option2 == "1":
                    print(
                        "\nSUSHI CHEF: Thank you! I'll make you the best "
                        "sushi you've ever had.\n")
                    quest_received = True
                    # return to menu A2 - main room
                    return quest_received
                else:
                    print("\nSUSHI CHEF: Won't you please help me out?\n")
                    continue
        else:
            # Quest has been received
            quest_received = True
            print("\nSUSHI CHEF: Do you have those ingredients?\n")
            options3 = {"1": "[1] \"Yes.\"", "2": "[2] \"Not yet.\""}
            option3 = option_check(options3)
            if option3 == "2":
                return quest_received
            print("\nSUSHI CHEF: Let's see...")
            # Check if quest fulfilled
            if not game.quest_items:
                # End game sequence
                print("\nSUSHI CHEF: Ah, you've brought me everything I need.")
                print("\nSUSHI CHEF: *mixes sushi rice*")
                print("\nSUSHI CHEF: *chops fish*")
                print("\nSUSHI CHEF: *rolls sushi*")
                print("\nSUSHI CHEF: Ready to eat the best sushi of your "
                      "life?.\n")
                options4 = {"1": "[1] \"Yes! Finally!!\"",
                            "2": "[2] \"Not really, I don't even like "
                                 "sushi...\""}
                option4 = option_check(options4)
                if option4 == "1":
                    pass
                else:
                    print("\nSUSHI CHEF: WHAT DO YOU MEAN YOU DON'T LIKE "
                          "SUSHI???\n")
                    options5 = {"1": "[1] \"Sheesh, fine, I'll try it.\"",
                                "2": "[2] \"...\""}
                    while True:
                        option5 = option_check(options5)
                        if option5 == "1":
                            break
                        else:
                            print("\nSUSHI CHEF: You went through all that "
                                  "just to not eat my sushi? The "
                                  "disrespect!\n")
                            continue
                print("\nThe SUSHI CHEF sets down a plate of sushi in front "
                      "of you.\nIt is, indeed, the best sushi you've ever "
                      "had.")
                Header().print_header("T H E  E N D")
                exit()
            else:
                # Quest has not yet been fulfilled
                print(f"\nSUSHI CHEF: Do you take me for a fool, "
                      f"{game.player_name}? You're still missing "
                      f"something...\n")

    def nori_hoarder(self):
        """Talk to NORI HOARDER."""
        if "Nori" not in game.inventory:
            # Dialogue round 1
            print("\nNORI HOARDER: Hey! Hey, you!\n")
            options1 = {"1": "[1] \"...Me?\"", "2": "[2] Run away"}
            option1 = option_check(options1)
            if option1 == "2":
                return False
            else:
                gm.talked_NPC.add("nori_hoarder")
            # Dialogue round 2
            print(f"\nNORI HOARDER: Yeah, you're {game.player_name}, right? "
                  f"I've got a whole stack of nori. You want some?\n")
            options2 = {"1": "[1] \"Okay!\"",
                        "2": "[2] \"How do you know who I am?\""}
            option2 = option_check(options2)
            if option2 == "1":
                # Add nori to player inventory
                print("\nNORI HOARDER: Here you go!")
                nori_idx = game.quest_items.index("Nori")
                nori = game.quest_items.pop(nori_idx)
                game.inventory.append(nori)
            else:
                # Dialogue round 3
                print("\nNORI HOARDER: Don't worry about it. Do you want "
                      "some nori or not?\n")
                options3 = {"1": "[1] \"I guess so.\"",
                            "2": "[2] \"Stay away from me, you creep!\""}
                option3 = option_check(options3)
                if option3 == "1":
                    # Add nori to player inventory
                    print("\nNORI HOARDER: Here you go!")
                    nori_idx = game.quest_items.index("Nori")
                    nori = game.quest_items.pop(nori_idx)
                    game.inventory.append(nori)
        else:
            # Nori already in player inventory
            print("\nNORI HOARDER: I've already given you some nori.")

    def rice_fiend(self):
        """Talk to RICE FIEND."""
        gm.talked_NPC.add("rice_fiend")
        if game.games_played["Rice Game"] == 0:
            # Introduce if game hasn't been played yet.
            # Dialogue round 1
            print("\nRICE FIEND: You looking for some rice? I've got a whole "
                  "wheelbarrow here.\n")
            options1 = {"1": "[1] \"Yeah, can I have some?\"",
                        "2": "[2] \"No thanks\""}
            option1 = option_check(options1)
            if option1 == "2":
                return False
            # Dialogue round 2
            print("\nRICE FIEND: I'll give you a sack of rice if you play a "
                  "game with me.\n")
            options2 = {"1": "[1] \"A game?\"", "2": "[2] \"I'd rather not.\""}
            option2 = option_check(options2)
            if option2 == "2":
                return False
            # Play Rice Game
            self.play_rice_game()
        else:
            if "Rice" not in game.inventory:
                # Let player know this is a new sack of rice
                print("\nRICE FIEND: I've given away that last sack of rice, "
                      "but here's another if you want to guess again!\n")
                options3 = {"1": "[1] \"I'll play again\"",
                            "2": "[2] \"I don't think so.\""}
                option3 = option_check(options3)
                if option3 == "2":
                    return False
                # Play Rice Game
                self.play_rice_game()
            else:
                # Rice already in player inventory
                print("\nRICE FIEND: Only one sack of rice per person!")

    def play_rice_game(self):
        """Start Rice Game."""
        game.games_played["Rice Game"] += 1
        rice_game = RiceGame()
        won_game = rice_game.run_game()
        if won_game:
            rice_idx = game.quest_items.index("Rice")
            rice = game.quest_items.pop(rice_idx)
            game.inventory.append(rice)

    def fish_monger(self):
        """Talk to FISH MONGER."""
        gm.talked_NPC.add("fish_monger")
        if game.games_played["Insult Game"] == 0:
            # Introduce if game hasn't been played yet.
            # Dialogue round 1
            print("\nFISH MONGER: *Plays clarinet*\n")
            options1 = {"1": "[1] \"Um...\"", "2": "[2] Leave"}
            option1 = option_check(options1)
            if option1 == "2":
                return False
            # Dialogue round 2
            print("\nFISH MONGER: What do you want from me, oil spill?\n")
            options2 = {"1": "[1] \"What did you call me??\"",
                        "2": "[2] Do not engage further."}
            option2 = option_check(options2)
            if option2 == "2":
                return False
            # Dialogue round 3
            print("\nFISH MONGER: Ha, what are you wandering around here for, "
                  "land lubber? Looking for some fish? Well I don't just go "
                  "handing out freebies to random weaklings.\n")
            options3 = {"1": "[1] \"Fight me!!\"",
                        "2": "[2] \"I don't have time for this...\""}
            option3 = option_check(options3)
            if option3 == "1":
                self.play_insult_game()
            # pass
        else:
            if "Fish" not in game.inventory:
                # Ask to play insult game again
                print(f"\nFISH MONGER: {game.player_name} the loser back "
                      f"again for another round?\n")
                options4 = {"1": "[1] \"I'll beat you this time!\"",
                            "2": "[2] Hiss and walk away."}
                option4 = option_check(options4)
                if option4 == "1":
                    self.play_insult_game()
            else:
                # Fish already in player inventory
                print("\nFISH MONGER: Why can't you just leave me and my "
                      "clarinet alone?")

    def play_insult_game(self):
        """Start Insult Game."""
        game.games_played["Insult Game"] += 1
        insult_game = InsultGame()
        won_game = insult_game.run_game()
        if won_game:
            fish_idx = game.quest_items.index("Fish")
            fish = game.quest_items.pop(fish_idx)
            game.inventory.append(fish)

    def sushi_eater(self, sushi_lover):
        """Talk to Sushi Eater."""
        gm.talked_NPC.add("sushi_eater")
        if not sushi_lover:
            print("\nSUSHI EATER: I just love eating sushi! Don't you?\n")
            options = {"1": "[1] \"Yes!!\"", "2": "[2] \"No, sushi is vile.\""}
            option = option_check(options)
            if option == "2":
                print("\nSUSHI EATER: Oh, what a shame..")
            else:
                print("\nSUSHI EATER: Of course! Everyone loves sushi.")
                sushi_lover = True
                return sushi_lover
        else:
            sushi_lover = True
            print("\nSUSHI EATER: Hmm... I see you're gathering sushi "
                  "ingredients?\n")
            options2 = {"1": "[1] \"Yeah, I am.\"",
                        "2": "[2] \"Mind your own business!\""}
            option2 = option_check(options2)
            if option2 == "2":
                return sushi_lover
            else:
                print("\nSUSHI EATER: Let's see what you've got...")
                if not game.inventory:
                    print("SUSHI EATER: Looks like you've got nothing yet.")
                else:
                    for item in game.inventory:
                        print(f"SUSHI EATER: {item}")
                if game.quest_items:
                    print(f"\nSUSHI EATER: You're still missing something. "
                          f"Need a hint?\n")
                    options3 = {"1": "[1] \"Sure!\"",
                                "2": "[2] \"Nah, I can do this on my "
                                     "own.\""}
                    option3 = option_check(options3)
                    if option3 == "2":
                        print("SUSHI EATER: See ya later then!")
                        return sushi_lover
                    else:
                        hint = self.sushi_hints()
                        if hint:
                            print(f"\nSUSHI EATER: {hint}")
                        else:
                            return sushi_lover
                        return sushi_lover
                else:
                    print("\nSUSHI EATER: You've got all the ingredients!")
                    return sushi_lover

    def sushi_hints(self):
        hints = {
            "Nori": "You still need something to wrap the sushi in.",
            "Rice": "You're missing the key ingredient! It's what holds the "
                    "sushi together.",
            "Fish": "You might want to add some filling for your sushi."
        }
        available_hints = [value for key, value in hints.items() if
                           key in game.quest_items]
        return random.choice(available_hints) if available_hints else False


game = SushiQuest()
gm = Menu()
game.run_game()
