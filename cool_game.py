import time
import random


def print_pause(string):
    while True:
        print(string)
        time.sleep(2)
        break


def intro():
    print_pause("You open your eyes and find yourself standing in a grand "
                "hall.")
    print_pause("It's terribly dark... There seems to be no way out...")
    print_pause("Lightning flashes outside and casts light across the dark, "
                "ominous room...")
    print_pause("Wait... Was that grand doorway there just a moment ago? "
                "How lucky!")
    print_pause("Lightning flashes again.")
    print_pause("Aha! A staircase! Maybe there IS a way out of this "
                "creepy place!")


def library(items):
    creatures = random.choice(["manticore", "goblin", "faerie", "phouka",
                               "minotaur"])
    names = random.choice(["Talon", "Scorch", "Grumble", "Thistle",
                           "Meadowsweet"])
    if "grimoire" in items:
        print_pause("You open the door to find a cozy, inviting library.")
        print_pause(f"The {creatures} offers to show you their needlepoint "
                    "progress.")
        print_pause("You politely decline, and leave the library.")
        main(items)
    else:
        print_pause("You open the door to find a cozy, inviting library.")
        print_pause("The warm, amber light is coming from a fire in a giant "
                    "hearth.")
        print_pause(f"Sitting in an armchair by the fire is a {creatures}.")
        print_pause(f"The {creatures} beckons you toward the fire.")
        print_pause(f"You both have a lovely conversation about {creatures} "
                    "rights.")
        print_pause(f"The {creatures}, {names}, gives you a grimoire as a "
                    "token of friendship.")
        print_pause("You leave the library.")
        items.append("grimoire")
        main(items)


def staircase(items):
    oldies = random.choice(["wizard", "witch"])
    print_pause("You climb the stairs and arrive in a cramped, smelly room.")
    print_pause(f"Huddled in the far corner is a clever looking old {oldies}.")
    if "grimoire" in items:
        print_pause(f"The {oldies} notices the grimoire in your hand and "
                    "shares a magick spell.")
        print_pause("You now have a transportation spell! Finally, you can go "
                    "home.")
        play_again()
    else:
        print_pause(f"The {oldies} mumbles something about not having time "
                    "for silly people.")
        print_pause("You head back down the stairs.")
        main(items)


def main(items):
    while True:
        response = input("What would you like to do?\n"
                         "Enter 1 to climb the stairs\n"
                         "Enter 2 to go through the doorway\n>> ")
        if response == '1':
            staircase(items)
        elif response == '2':
            library(items)
        else:
            print_pause("Sorry, I don't understand.")
            main(items)


def play_again():
    while True:
        answer = input("Would you like to play again?\n"
                       "Enter 1 to play again\n"
                       "Enter 2 to exit\n>> ")
        if answer == '1':
            cool_game()
        elif answer == '2':
            print_pause("Farewell!")
            exit(0)
        else:
            print_pause("Sorry, I don't understand.")
            play_again()


def cool_game():
    items = []
    intro()
    main(items)
    play_again()


cool_game()
