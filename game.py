import time
import random
items = []


def print_pause(string, t):
    """Create a time delay between the strings and print the strings"""
    print(string)
    time.sleep(t)


def intro(ghost):
    """print the intro"""
    print_pause("#### THE GHOST OF DELHI ####\n", 2)
    print_pause(
        'Every year the' + " " +
        ghost.upper() +
        " " +
        "returns to the city of delhi.",
        2)
    print_pause("The streets of delhi are empty. It is a dark night", 2)
    print_pause("Everyone is afraid of his return.", 2)
    print_pause("For bussinesss meeting you arrived " +
                "today in the center of the city.", 2)
    print_pause("Can't you find the ghost and break the curse?", 2)


def appearing(ghost):
    """let the ghost appear"""
    print_pause("You walk on.", 2)
    print_pause("The" + " " + ghost + " " + "appears!!!", 2)


def repeat_game():
    """repeat the game"""
    while True:
        playagain = input("Play again (yes/no)?\n")
        if playagain == "yes":
            items.clear()
            play_game()
        elif playagain == "no":
            break
        else:
            repeat_game()


def choice1(choice, ghost):
    """handle the first choice"""
    if choice == "1":
        if "flashlight" not in items:
            print_pause("The Railway station is really foggy", 2)
            print_pause("You can see absolute nothing", 2)
            print_pause("You walk on and find a flashlight", 2)
            light_choice(ghost)
        else:
            print_pause(
                "You already pasted this way\nPlease choose another way!", 2)
            logic(ghost)


def choice2(choice, ghost):
    """handle the second choice"""
    if choice == "2":
        if "mirrors" not in items:
            print_pause("The church street is totally empty and dark", 2)
            print_pause(
                "You only hear the sound of" +
                "the wind that runs through the hall", 2)
            mirror_choice(ghost)
        else:
            print_pause(
                "You allready pasted this way\nPlease choose another way!", 2)
            logic(ghost)


def choice3(choice, ghost):
    """handle the third choice"""
    if choice == "3":
        print_pause("You enter the fort.", 2)
        print_pause("You hear a terrible sound in the great hall", 2)
        print_pause("It is the" +
                    " " +
                    ghost +
                    " " +
                    "that faces you!",
                    2)
        if "flashlight" in items and "mirrors" in items:
            if ghost == "zombie dog":
                print_pause("### SHOWDOWN ####", 2)
                print_pause("The zombie dog begin to run.", 2)
                print_pause("It attacks you.", 2)
                print_pause(
                    "You combine the 2 items to one weapon\n" +
                    "so that the mirror reflect the light everywhere.",
                    2)
                print_pause("The" + ghost + "get burned by the light.", 2)
                print_pause("YOU WON THE GAME!", 2)
                repeat_game()
            else:
                appearing(ghost)
                print_pause("You faint.", 2)
                repeat_game()
        else:
            if ghost == "zombie dog":
                print_pause(
                    "You enter the dark delhi" +
                    "fort and walk to the cold rooms", 2)
                print_pause("Suddenly the" + " " + ghost +
                            " " + "appears and attacks you.", 2)
                print_pause(
                    "You give everything but the" +
                    " " +
                    ghost +
                    " " +
                    "is to strong.\nYou faint.",
                    2)
                print_pause("Something was missing...", 2)
                logic(ghost)
            else:
                print_pause("The" + " " + ghost + " " + "attacks you!", 2)
                print_pause("You faint!", 2)
                repeat_game()


def light_choice(ghost):
    """handle the excplicit decision in choice1"""
    lightchoice = input("Do you wanna take it up (yes/no)?\n").lower()
    if lightchoice == "yes":
        items.append("flashlight")
        appearing(ghost)
        if ghost == "vampire":
            print_pause(
                "You activate your flashlight and the" +
                ghost +
                "disappears.",
                2)
            print_pause("YOU WON THE GAME", 2)
            repeat_game()

        elif ghost == "zombie dog":
            print_pause(
                "You can't fight the" + " " + ghost + " yet", 2)
            print_pause("You need one more item!", 2)
            logic(ghost)
        else:
            print_pause(
                "The flashlight has no" + " " +
                "effect on the scary doll!", 2)
            print_pause("You faint!", 2)
            repeat_game()
    elif lightchoice == "no":
        if ghost == "vampire":
            print_pause("You return to the starting point.", 2)
            logic(ghost)
        else:
            appearing(ghost)
            print_pause("You faint.", 2)
            repeat_game()
    else:
        print_pause("Please type your answer again!", 2)
        light_choice(ghost)


def mirror_choice(ghost):
    """handle the explicit decision in choice 2"""
    print_pause("There are to little mirrors at the altar.", 2)
    mirrorchoice = input("Do you wanna pick them up(yes/no)?\n").lower()
    if mirrorchoice == "yes":
        items.append("mirrors")
        appearing(ghost)
        if ghost == "vampire":
            if "flashlight" in items:
                print_pause("You activate your flashlight!", 2)
                print_pause("You shine on the mirrors.", 2)
                print_pause(
                    "That reflection builds an wall" +
                    "of light so that the vampire disappears.", 2)
                print_pause("YOU WON THE GAME!", 2)
                repeat_game()
            else:
                if ghost == "zombie dog":
                    print_pause(
                        "Something is missing to fight the" +
                        " " +
                        ghost +
                        " ",
                        2)
                    logic(ghost)
                else:
                    print_pause("You faint!", 2)
                    repeat_game()
        else:
            print_pause("You can't fight the" + " " + ghost + "yet", 2)
            print_pause("You need one more item!", 2)
            logic(ghost)

    elif mirrorchoice == "no":
        print_pause("There is also oil lamp.", 2)
        oil_choice(ghost)

    else:
        print_pause("Please type your answer again!", 2)
        mirror_choice(ghost)


def oil_choice(ghost):
    """handle the choice after the mirror choice"""
    oilchoice = input(
        "Do you wanna pick up the oil lamp (yes/no)?\n").lower()
    if oilchoice == "yes":
        if ghost == "scary doll":
            appearing(ghost)
            print_pause("You turn your oil lamp on!", 2)
            print_pause("The" + " " + ghost +
                        " " + "get's burned and dies", 2)
            print_pause("YOU WON THE GAME!", 2)
            repeat_game()
        else:
            appearing(ghost)
            print_pause("You faint!", 2)
            repeat_game()
    elif oilchoice == "no":
        appearing(ghost)
        print_pause("You faint", 2)
        repeat_game()
    else:
        print_pause("Please type your answer again!", 2)
        oil_choice(ghost)


def logic(ghost):
    """handle the whole logic of the game"""
    print_pause("Where do you want to go?\n", 2)
    choice = input(
        "Choose on of the following numbers:\n1." +
        "Railway station\n" +
        "2. church street\n3. fort\n").lower()
    if choice not in "1" and choice not in "2" and choice not in "3":
        print_pause("\nSorry I don't understand!", 0)
        print_pause("Please repeat the input!\n", 0)
        logic(ghost)
    choice1(choice, ghost)
    choice2(choice, ghost)
    choice3(choice, ghost)


def play_game():
    """combine the  functions"""
    ghost = random.choice(["vampire", "zombie dog", "scary doll"])
    intro(ghost)
    logic(ghost)


play_game()
