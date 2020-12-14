# Jurassic Journey

# A choose your own adventure game that (mostly) follows the plot of the 1st Jurassic Park movie.

from time import sleep
from colorama import Fore, Style

snacks = ("Chips", "Chocolates", "Gummy Worms")
dinos = ("Velociraptor", "T-Rex", "Dilophosaurus")
weapons = ("Shotgun", "Sword", "Taser")
game_items = [] # 0 is snack, 1 is dino, 2 is num
split = "----------------------------------------"

def game_intro():
    """Welcomes the user to the game. Prompts user to pick 3 items. Adds the items to a list."""

    print("Welcome to Jurassic Park!")
    sleep(1)
    print()
    print("The choices you make in this game will lead you down\na variety of paths, encountering dinosaurs and danger.\nGood luck!")
    sleep(3)
    print()
    print("Before we get started, we need you to pick a few items.")
    sleep(2)
    print()
   
    while True:

        print("Pick a snack from the following list:") 
        print()

        for snack in snacks:
            print(snack)
        print()
        game_snack = input("> ").title()

        if game_snack in snacks: 
            game_snack = game_snack.lower()
            game_items.append(game_snack)
            print(f"{Fore.BLUE + game_items[0].title() + Style.RESET_ALL}! What a great choice!")
            print()
            break
                        
        else:
            print("That doesn't look right. Please try again.")
            print()

    while True:

        print("Pick a dinosaur from the following list:")
        print()

        for dino in dinos:
            print(dino)

        print()
        game_dino = input("> ").title()

        if game_dino in dinos:
            game_dino = game_dino.lower()
            game_items.append(game_dino)
            print(f"{Fore.RED + game_items[1].title() + Style.RESET_ALL}! How scary!")
            print()
            break
        
        else:
            print("That doesn't look right. Please try again.")
            print()

    while True: 

        print("Pick a number 2-50.")
        print()
        game_num = int(input("> "))
        print()

        if game_num < 2 or game_num > 50:
            print("Please enter a number that is between 2 and 50.")
            print()

        else:
            game_items.append(game_num)
            print(f"{Fore.GREEN + str(game_items[2]) + Style.RESET_ALL}. Excellent.")
            print("You'll see these 3 items later in your adventure!")
            print()
            break

    print(split)
    sleep(2)

def first_decision_point():
    """Choose whether to stay inside in computer lab or go on the outdoor dino tour."""

    print("Let's get started!")
    print()

    while True:

        print("Indoors or outdoors? Select A or B:")
        print()
        print("(A) Let's stay inside and check out the computer lab\nthat runs the park.")
        print()
        print("(B) Let's explore the great outdoors and\ncheck out this dinosaur tour!")
        first_decision = input("> ").title()

        if first_decision == "A":
            indoor_option()
            break

        elif first_decision == "B":
            outdoor_option()
            break

        else:
            print("That is not a valid option. Please try again.")

def indoor_option():
    """Follows the first decision point. Choose either the Ray Arnold path or Dennis Nedry path from here"""

    print()
    print("It's much safer inside. No dinos here!")
    sleep(1)
    print()

    while True:

        print("Select A or B from the options below:")
        print()
        print("(A) Go out for lunch with your friend Dodgson\nto discuss an exciting financial opportunity.")
        print()
        print("(B) Stay behind and do your job.\nYou have a dino tour program to run!")
        indoor_decision = input("> ").title()

        if indoor_decision == "A":
            dennis_nedry()
            break

        elif indoor_decision == "B":
            ray_arnold()
            break

        else:
            print("That is not a valid option. Please try again.")

def outdoor_option():
    """Follows the first decision point. Choose either the Ellie Sattler or Alan Grant path from here."""

    print()
    print("Let's get started with this dino tour!")  
    sleep(1)    
    print() 

    while True:

        print("Select A or B from the options below:")
        print()
        print("(A) Help a sick triceratops by digging through\ndino droppings. Ride back in a gas jeep later.")
        print()
        print("(B) Get back in the car and head back\nto the guest center before the approaching storm hits.")
        outdoor_decision = input("> ").title()

        if outdoor_decision == "A":
            ellie_sattler()
            break

        elif outdoor_decision == "B":
            alan_grant()
            break

        else:
            print("That is not a valid option. Please try again.")

def ray_arnold():
    """Follows the path of Mr. Ray Arnold as he works at the park."""

    print(split)
    print("Mr. Ray Arnold, you are committed to your job as\nChief Engineer. You even stay at your desk to smoke!")
    sleep(3)
    print()
     
    print("The dino tour has started!")
    sleep(2)
    print()
    print("Looks like the T-Rex is a no-show.")
    sleep(2)
    print()

    arnold_feed_trex()

    print()
    print("Programmer Dennis Nedry left a while ago to\nvisit the snack machine. It's odd that many of\nthe security systems are shutting down.")
    sleep(6)
    print()
    #     Notices security systems are shutting down. Tries to get around code and access is denied. 
    print("Let's try to get the system back online.")
    sleep(2)
    print()

    arnold_magic_word()
    
    print()
    #     Have to go through game_num million lines of code. Will take too long to get park operational. 
    print(f"You would have to go through\n{Fore.GREEN + str(game_items[2]) + Style.RESET_ALL} million lines of code to fix this issue.\nShutting down all power and turning back on\nwill be a faster resolution.")
    #     Shut down all power and now systems need to come back online.
    sleep(6)
    print()

    # Choose a cool_catchphrase for this moment ("Hold on to your butts will be an option.")
    arnold_catchphrase()

    # Choose a weapon from a list.
    game_weapon = arnold_weapon()

    # Encounter game_dino
    # Roll an even number on the dice to defeat the dino, turn the power on, and save the day!
    print("You've made it to the maintenance shed!\nTime to get the park back online!")
    sleep(3)
    print()
    print("OH NO!!")
    sleep(2)
    print()
    print(f"You have encountered a vicious {Fore.RED + game_items[1] + Style.RESET_ALL}!\nUse your {game_weapon} to fight it off!")
    sleep(3)
    print()
    print(f"Roll the dice to see if you will defeat the {Fore.RED + game_items[1] + Style.RESET_ALL}.\nRoll an even number to survive!")
    sleep(3)
    print()

    final_roll = roll_dice()

    if final_roll % 2 == 0:
        print(f"Mr. Arnold! You defeated the {Fore.RED + game_items[1] + Style.RESET_ALL} with your {game_weapon}!\nQuite impressive! You turned the power back on and saved the day!")

    else:
        print(f"Sad day, Mr. Arnold. The {Fore.RED + game_items[1] + Style.RESET_ALL} got the best of you.\nToday was not your day.")

    sleep(3)
    print()

    play_again()

def dennis_nedry():
    """Follows the path of Dennis Nedry as he works at the park"""

    print(split)
    print("You've done such a great job as Computer Programmer\nat Jurassic Park, Dennis Nedry!\nYou deserve a nice lunch with your close friend.")
    sleep(5)
    print()
      # Go grab a game_snack from the snack machine. Advise systems will be down for 18-20 minutes. 
    print(f"Now that you are back from lunch,\nyou have to prepare for the job that you are doing for Dodgson.\nGo ahead and tell everyone you are grabbing {Fore.BLUE + game_items[0] + Style.RESET_ALL}\nfrom the snack machine.\nAdvise systems will be down for 18-20 minutes.")
    sleep(7)
    print()
    #     You are actually grabbing game_num of embyros! 
    print(f"Fooled them! You are actually stealing {Fore.GREEN + str(game_items[2]) + Style.RESET_ALL} embryos\nfrom the secure embryo cold storage.\nNab those embryos, grab a gas powered jeep,\nand meet your contact at the boat dock!")
    print(split)
    sleep(7)
    #     Crash car into pole. Decision: Go left or right?
    print("This rain is heavy!")
    print()
    sleep(2)
    print("Your car CRASHES into a direction pole\nat a fork in the road.")
    sleep(4)
    print()

    nedry_direction()

    nedry_throw()

    print()
    print(f"Roll the dice to see if you will distract\nand get away from the {Fore.RED + game_items[1] + Style.RESET_ALL}.\nRoll an even number to survive!")
    sleep(2)
    print()       
   
    final_roll = roll_dice() 
    #     Dino attack! Roll an even number on the dice to defeat the dino, escape with the embryos, and become rich overnight!  

    if final_roll % 2 == 0:
        print(f"Dennis Nedry! Against all odds you defeated the {Fore.RED + game_items[1] + Style.RESET_ALL}!\nQuite impressive!\nEnjoy maniacally laughing while you make your way\ndown to the docks to sell those embryos.\nYou'll be rich overnight.")
        
    else:
        print(f"Sorry, Dennis. The {Fore.RED + game_items[1] + Style.RESET_ALL} was not\ndisracted by your attempt.\nWhat do you think happens to those embryos though?\nSurely this will be the last time someone\nwill have one of these dino parks...")

    sleep(6)
    print()

    play_again()

def ellie_sattler(): 
    """Follows the path of Dr. Ellie Sattler as she makes her way through the park."""

    print(split)
    print(f"You seem tenacious!\nYou must be Paleobotanist, Dr. Ellie Sattler.\nCan't believe you found {Fore.BLUE + game_items[0] + Style.RESET_ALL} in the dino droppings!")
    print()
    sleep(6)

     # After you clean up from dino dropping exploration, grab that gas jeep and go rescue Grant and the kids!
    
    sattler_save_kids()

    print(split)
    print("You reach the t-rex paddock.")
    print()
    sleep(3)
    print("Grant and the kids are nowhere to be found.")
    print()
    sleep(4)
    print("WAIT!")
    print()
    sleep(2)
    print("Jeff Goldblum...errrr...Dr. Ian Malcolm is alive,\ninjured, and moaning in what sounds like a\nslightly sexual nature?")
    sleep(4)
    print()
    print("The ground rumbles.")
    print()
    sleep(2)
    print("!!!!!!!!!!!!!!!!!") 
    print()
    sleep(2)
    print("The t-rex is approaching quickly.")
    print()
    sleep(2)
    print("Dr. Sattler carefully places Malcolm's manly yet\ndelicate body into the jeep.")
    sleep(6)
    print()
        #     Find and rescue Malcolm. T-rex approaches. Car goes game_num MPH. 
    #         If greater than or equal to 32 MPH escape the T-Rex
    #         If less than 32 MPH...get creative to escape that T-Rex
    sattler_drive()

    #     Mr. Arnold is going to turn on the power. Listen to geriatric owner of murder park ramble about a flea circus while his grandkids are missing. Eat some icecream. 
    print()
    print("You've made it back to the visitor center with\nan injured yet glistening Malcolm.")
    print()
    sleep(4)
    print("Mr. Arnold is going to flip the park circuit\nbreakers at the maintenance shed.")
    print()
    sleep(4)
    print("Spend this downtime eating melting ice cream while\nthe park owner rambles about a flea circus.")
    print()
    sleep(4)
    print("Relax. Arnold has this under control.")
    print()
    sleep(5)
        #     You haven't heard from Mr. Arnold. 
    print("It's been a while since you've heard from Arnold.")
    print()
    sleep(3)
    print("Maybe it's best if you head out to\nthe maintenance shed to find him a hand.")
    print()
    sleep(5)
    print("Did we say FIND? We meant GIVE!\nAs in help out.")
    print()
    sleep(5)

    sattler_shed()
    print(split)

     #     Turn power on
    print("You made it to the maintenance shed!")
    print()
    sleep(3)
    print("Be careful, there are velociraptors everywhere.")
    print()
    sleep(3)
    print("Follow the electrical conduit to the circuit breakers.")
    print()
    sleep(3)
    print("Alright! You've reached the circuit breakers!")
    print()
    sleep(3)
    print("Start turning everything back on.")
    print()
    sleep(3)
    print("BUZZ")
    sleep(1)
    print("BUZZ")
    sleep(1)
    print("BUZZ")
    print()
    sleep(1)
    print("BOOM")
    print()
    sleep(2)
    print("Lights turn on.")
    print()
    sleep(2)
    print("Power is up and running!")
    print()
    sleep(3)
    print("Mr. Arnold's hand pats your shoulder.")
    print()
    sleep(3)
    print("So comforting to know he was there the whole time,\nhiding behind a wall of cables.")
    print()
    sleep(4)
    print("THAT IS MR. ARNOLD'S SEVERED ARM AND OMG\nTHERE IS A VELOCIRAPTOR!")
    print()
    sleep(4)
    print("RUUUUUUUUUUUUUUUUUNNNNNNNN!!!!")
    print()
    sleep(3)

    sattler_raptor() 

    print(split)
    print("You made it back to the visitor center and\nfound Dr. Alan Grant on the way!")
    print()
    sleep(4)
    print("Time to get out of there.")
    print()
    sleep(2)
    print("A helicopter is on the way.\nGrab the kids and your two boyfriends and leave.")
    print()
    sleep(4)
    print("On the way out,\nyou encounter those darn velociraptors in the lobby.")
    print()
    sleep(4)
    print("CURSES DOORS!!!")
    sleep(2)
    print()

    sattler_lobby()
    print()

    play_again()

def alan_grant():
    """Follows the path of Dr. Alan Grant as he makes his way through the park."""

    print(split)
    print("Good call, Paleontologist Dr. Alan Grant.\nYou'll be stuck in the car with\nself-proclaimed Chaotician Dr. Ian Malcomn\nbut at least you won't be in the car with\nthe park owner's grandkids.")
    sleep(6)
    print()

    print(f"You're approaching the t-rex paddock while\nMalcolm is telling you about his {Fore.GREEN + str(game_items[2]) + Style.RESET_ALL} ex-wives.")
    print()
    sleep(5)
        #     On the way back to the visitor center during the storm, talk to Dr. Malcolm about his game_num amount of ex wives while eating your game_snack
    grant_ex_wives()
    print()
    #     Car stops in front of trex paddock. Trex shows up and lawyer leaves the kids alone. 
    print("The car suddenly STOPS right in front of the t-rex paddock.")
    sleep(3)
    print()
    print("It appears the power has gone out.")
    print()
    sleep(2)
    print("The t-rex starts to break the electrical fence.\nThe kids are all alone in the first car.")
    print()
    sleep(3)
    print("OH NO! The t-rex is fast appoaching their vehicle!")
    print()
    sleep(3)
    #      Stay in the car, or help the kids? Flip a coin with Malcolm. Heads you stay, tales you go. 
    #         If heads: Malcolm goes with a flare and gets injured by Trex. The Trex is distracted so you go to rescue the kids. 
    #        If tales: You bring your game_snack to distract the Trex. Malcolm decides that is a lame choice and gets out of the car with a flare. Much better distraction. Trex goes after Malcolm. You rescue the kids.
    grant_coin_flip()
    
    print("You get to the kids and rescue the older one.\nThe younger one is stuck in the car.")
    print()
    sleep(3)
    print("The t-rex SMASHES into the car!\nThis flips the car over the edge of a steep wall.")
    print()
    sleep(4)
    print("The car CRASHES into a tree.")
    print()
    sleep(2)
    print("The younger kid calls out for help.")
    print()
    sleep(2)
    print("Good. He is still alive.")
    print()
    sleep(2)

    #   Climb a tree and rescue one of the grandkids
    grant_climb_tree()

    print("Time to move on from the t-rex enclosure\nand head back to the visitor center on foot.")
    sleep(4)
    print(split)
    print("It's a new day!\nYou and the kids are walking through a field.")
    print()
    sleep(4)
    print("Suddenly, a HERD of Gallimimus start\nflocking towards you.") 
    print()
    sleep(4)
    print("Take cover behind that conveinently\nplaced broken log!")
    print()
    sleep(4)
    #   Run through a field and encounter a herd of Gallimimus. Suddenly a game_dino attacks!
            #Differnt outcome depending on game_dino option 

    grant_field()
    
    print("Grant and the kids ESCAPE the field and continue\non to the visitor center.")
    sleep(5)
    print(split)
    print("They walk through the front door.")
    print()
    sleep(2)
    print("Velociraptors immediately surround them!")
    print()
    sleep(3)
    #   Vistor Center Showdown! T-rex shows up and attacks the raptors. Nice! 
    print("A raptor GLARES right at Grant!") 
    print()
    sleep(3)
    print("The ground starts SHAKING.")
    print()
    sleep(3)
    print("A raptor LUNGES right at Grant!") 
    print()
    sleep(3)
    print("A t-rex GRABS the lunging raptor out of thin air \nand CRUSHES the raptor in its jaws.")
    print()
    sleep(5)
    print("Will Grant and the kids be able to escape this bizarre circus?")
    print()
    sleep(2)
    
    #Roll the dice to see if you escape the T-rex. Even number survives.

    grant_dice_role()

    play_again()

def roll_dice():
    """Roll a dice, print the value, and return the value"""

    import random
    print("Type roll to give it a go!")
    input("> ")
    print()
    sleep(1)
    dice_num = random.randint(1, 6)
    print(f"You rolled a {dice_num}.")
    print()
    sleep(2)
    return dice_num

def flip_coin():
    """Flip a coin!"""

    import random
    print("Type FLIP to give it a go!")
    input("> ")
    print()
    heads_or_tails = random.randint(1, 2)

    if heads_or_tails == 1:
        print("Heads!")
        print()
        sleep(1)
        coin_outcome = "Heads"

    else:
        print("Tails!")
        print()
        sleep(1)
        coin_outcome = "Tails"

    return coin_outcome

def arnold_feed_trex():
    
    while True:
         #     Feeds Trex game_snack
        print("Would you like to feed the T-Rex? Yes or No?")
        arnold_feed = input("> ").title()
        print()

        if arnold_feed.startswith("Y"):
            print(f"Not sure if a T-Rex will like {Fore.BLUE + game_items[0] + Style.RESET_ALL},\nbut go ahead and give it a try.")
            print()
            sleep(4)
            print(f"The t-rex is not impressed with those {Fore.BLUE + game_items[0] + Style.RESET_ALL}.")
            sleep(2)
            break

        elif arnold_feed.startswith("N"):
            print(f"No problem. You've made quite a mess on your desk\nwith your {Fore.BLUE + game_items[0] + Style.RESET_ALL}.\nMight want to clean that up.")
            sleep(3)
            break

        else:
            print("That is not a valid option. Please try again.")

def arnold_magic_word():

    print("Type: access main program")
    input("> ")
    print()
    print("ACCESS DENIED")
    sleep(1)
    print()
    print("That didn't work. Try typing: access main security")
    input("> ")
    print()
    print("ACCESS DENIED")
    sleep(1)
    print()
    print("This isn't good. Alright. Type: access main program grid")
    input("> ")
    print()
    print("ACCESS DENIED and....")
    sleep(1)

    code_line = 0 

    while code_line <= 20: 
        # YOU DIDN'T SAY THE MAGIC WORD displayed on screen multiple times (while loop)
        print("YOU DIDN'T SAY THE MAGIC WORD!")
        code_line += 1
        sleep(0.1)

    sleep(2)

def arnold_catchphrase():

    while True: 
        print("Pick a cool catchphrase to say\nas you turn everything back on.")
        sleep(2)
        print()
        print("(A) You know me. It's my duty to please that booty.")
        print()
        print("(B) Hold on to your butts.")
        print()
        print("(C) And you will know my name is the Lord\nwhen I lay my vengeance upon you.")
        print()
        print("(D) I have had it with these motherf*ck!ng snakes\non this motherf*ck!ng plane!")
        arnold_quote = input("> ").title()
        print()

        if arnold_quote == "B":
            print("Powerful! Alright. Give it a go...")
            sleep(1)
            arnold_quote = "Hold on to your butts."
            break
            
        elif arnold_quote == "A":
            print("Seems like the wrong movie, but it's your call.")
            sleep(1)
            print("Ok! Give it a go...")
            sleep(1)
            arnold_quote = "You know me. It's my duty to please that booty."
            break
            
        elif arnold_quote == "C":
            print("Seems like the wrong movie, but it's your call.")
            sleep(1)
            print("Ok! Give it a go...")
            sleep(1)
            arnold_quote = "And you will know my name is the Lord\nwhen I lay my vengeance upon you."
            break
            
        elif arnold_quote == "D":
            print("Seems like the wrong movie, but it's your call.")
            sleep(1)
            print("Ok! Give it a go...")
            sleep(1)
            arnold_quote = "I have had it with these motherf*ck!ng snakes\n on this motherf*ck!ng plane!"
            break

        else:
            print("That is not a valid option. Please try again.")

    power_counter = 3

    while power_counter > 0:
        print(f"{power_counter}...")
        sleep(1)
        power_counter -= 1

    print(arnold_quote.upper())
    print()
    sleep(3)
    # Go to turn on circuit breakers. 
    print("That worked!")
    sleep(2)
    print()
    print("The power turned back on!\nYou'll need to turn on the circuit breakers\nin the maintenance shed on the other\nend of the compound.")
    sleep(5)
    print()

def arnold_weapon():      
    while True:

        print("Pick a weapon to take with you:") 
        sleep(1)
        print()

        for weapon in weapons:
            print(weapon)
        print()
        game_weapon = input("> ").title()

        if game_weapon in weapons:
            print()
            print(f"Sounds good. Take your {game_weapon.lower()}\nand head out to the maintenance shed.")
            print(split)
            game_weapon = game_weapon.lower() 
            sleep(3)
            return game_weapon

        else:
            print("Whoops. That doesn't look right. Please try again.")
            print()

def nedry_direction():

    while True:
        #     Spots a game_dino
        print("Do you go left or right at the fork?")
        direction = input("> ").lower()
        print()

        if direction.startswith("l"):
            print("Ok. Left it is!")
            print()
            sleep(2)
            print("This was the correct direction.\nThe dock is up ahead! Almost home free!")
            print()
            sleep(3)
            print("----------------!!!!!!")
            print()
            sleep(2)
            print(f"A {Fore.RED + game_items[1] + Style.RESET_ALL} comes into view and you swerve to avoid hitting it.")
            sleep(4)
            break

        elif direction.startswith("r"):
            print("Alright. We'll try going right.")
            print()
            sleep(2)
            print("This doesn't look right.\nWe should be at the dock by now.")
            print()
            sleep(3)
            print("You can't see through the fog in your glasses.\nYou CRASH into a bunch of rocks.")
            print()
            sleep(4)
            print(f"You look up and see a {Fore.RED + game_items[1] + Style.RESET_ALL} staring back at you.")
            sleep(4)
            break

        else:
            print("That is not a valid option. Please try again.")

    print()

def nedry_throw():
    while True: 
        nedry_throw_items = ("Stick", Fore.BLUE + game_items[0].title() + Style.RESET_ALL, "Flare")
        print(f"What do you throw at the {Fore.RED + game_items[1] + Style.RESET_ALL} in order to distract it?")
        print()

        for item in nedry_throw_items:
            print(item)
        print()
        nedry_item_choice = input("> ").lower()
        print()

        if nedry_item_choice == "stick" or nedry_item_choice == "flare" and game_items[1] == "t-rex":
            print(f"Worth a try.\nA {nedry_item_choice} might distract a {Fore.RED + game_items[1] + Style.RESET_ALL}.")
            sleep(3)
            break

        elif nedry_item_choice == "stick" or nedry_item_choice == "flare" and game_items[1] == "velociraptor":
            print(f"Be careful.\nThe {Fore.RED + game_items[1] + Style.RESET_ALL} is known to be a pack animal.\nPlaying with a {nedry_item_choice} may be a diversion to allow the others to hunt you.")
            sleep(3)
            break

        elif nedry_item_choice == "stick" or nedry_item_choice == "flare" and game_items[1] == "dilophosaurus":
            print(f"Be wary of the {Fore.RED + game_items[1] + Style.RESET_ALL}.\nThrow that {nedry_item_choice} as far as possible.\nYou don't want to encounter their venom.")
            sleep(3)
            break

        elif nedry_item_choice == game_items[0]:
            print(f"Bold choice.\nIt's doubtful that {Fore.BLUE + game_items[0] + Style.RESET_ALL} would distract a {Fore.RED + game_items[1] + Style.RESET_ALL}.")
            sleep(3)
            break

        else: 
            print("That is not a valid option. Please try again.")

def sattler_save_kids():

    while True: 

        print("Dr. Alan Grant and the park owner's grandkids are in trouble!\nDo you go out and save them? Yes or No?")
        print()
        ellie_save = input("> ").title()
        print()

        if ellie_save.startswith("Y"):
            print("How heroic!")
            sleep(2)
            break

        elif ellie_save.startswith("N"):
            print("We're going to pretend you didn't say that.\nSave those kids! No is not an option!")
            sleep(5)
            break

        else:
            print("That is not a valid option. Please try again.")

def sattler_drive():

    print("The t-rex has been clocked at 32 mph.\nLet's hope this jeep can go faster than that!")
    sleep(6)
    print()

    if game_items[2] >= 32:
        print(f"{Fore.GREEN + str(game_items[2]) + Style.RESET_ALL} mph! Great.\nWe should be able to outrun this t-rex!")
        sleep(4)
        print()
        print("So easy!\nYou escaped that t-rex like it was nothing.")
        sleep(4)

    elif game_items[2] < 10:
        print(f"{Fore.GREEN + str(game_items[2]) + Style.RESET_ALL} mph?\nHow current is your life insurance policy?")
        sleep(3)
        print(split)
        sleep(1)
        print(f"Unreal!\nWho would have thought a t-rex loved {Fore.BLUE + game_items[0] + Style.RESET_ALL}.")
        print()
        sleep(4)
        print("Wait.")
        print()
        sleep(2)
        print(f"Were those the same {Fore.BLUE + game_items[0] + Style.RESET_ALL}\nthat were in the dino droppings?")
        sleep(5)

    else:
        print(f"{Fore.GREEN + str(game_items[2]) + Style.RESET_ALL} mph?\nBreak out the flares. You'll need a big distraction.")
        sleep(3)
        print(split)
        sleep(1)
        print("Amazing!\nLighting all of the flares while still in the car was risky.\nThe t-rex definitely continued to chase it\nwhile you rolled out of the moving vehicle to safety.")
        sleep(7)

def sattler_shed():
 #Get distracted by sexy, open-shirt Dr. Malcolm or turn the power back on to save the day? CHOICE which will ultimately route to turning on the power. 
    while True:
 
        print("Type HELP to go out to the maintenance shed\nand help Mr. Armnold...ANROLD!")
        print()
        sleep(4)
        print("Type STAY to stick around and see where\nthings go with a panting, open-shirted Ian Malcolm.")
        print()
        sattler_shed = input("> ").upper()
        print()

        if sattler_shed.startswith("H"):
            print("Your bravery continues to impress.\nI'm sure Dr. Malcolm will be there when you get back.")
            sleep(4)
            break

        elif sattler_shed.startswith("S"):
            print("You do you.")
            print()
            sleep(2)
            print("He fell asleep....")
            sleep(2)
            print("...didn't he?") 
            sleep(3)
            print("He'll still be there when you get back. \nGo save the day!")
            sleep(4)
            break

        else:
            print("That is not a valid option. Please try again.")
   
def sattler_raptor():
     # escape velociraptor attack using a tactic from a list
    while True: 
        print("You have encountered a raptor wile exiting\nthe maintenance shed.")
        print()
        sleep(4)
        print("Choose your method of combat wisely.\nPick A, B, or C from the list below.")
        print()
        sleep(5)
        print("(A) Open palm slap the velociraptor in the face.\nShe won't see it coming.")
        print()
        print("(B) Use Mr. Arnold's severed arm as a weapon.")
        print()
        print("(C) Run as fast as you can and lock the door.\nRaptors don't know how to open doors.")
        print()
        sattler_combat = input("> ").upper()
        print()

        if sattler_combat == "A":
            print("Sattler SLAPS the raptor across the face.")
            print()
            sleep(3)
            print("The raptor is dumbfounded.")
            print()
            sleep(2)
            print("Sattler escapes the maintenance shed\nand heads back towards the visitor center.")
            sleep(4)
            break 

        elif sattler_combat == "B":
            print("You have the arm. Might as well use it!")
            print()
            sleep(3)
            print("Sattler SMACKS the raptor over the head\nwith the arm and RUNS right out of that shed.\nThe visitor center isn't too far away.")
            print()
            sleep(5)
            print("Run for your life!")
            sleep(3)
            break

        elif sattler_combat == "C":
            print("Ellie takes off running,\ndodges the raptor,\nand locks the door behind her,\ntrapping the raptor.")
            print()
            sleep(6)
            print("Everyone will be perfectly safe because\nthe likelihood that raptors will figure out doors\nin the next 10 minutes of the movie is slim to none.")
            sleep(6)
            break

        else: 
            print("That is not a valid option. Please try again.")

def sattler_lobby():
     #     Visitor Center Showdown! Velociraptor attack in the lobby. game_dino shows up!
    print("The velociraptors are surrounding your group.\nThis doesn't look good.")
    sleep(5)
    print()
    print("Wait....what's that sound?")
    print()
    sleep(3)
    print(f"A {Fore.RED + game_items[1] + Style.RESET_ALL} shows up!")
    print()
    sleep(3)
    print("How unexpected that this dino that you selected at\nthe beginning of the game would show up so late!")
    print()
    sleep(6)

    if game_items[1] == "t-rex":
        print("Good news!")
        print()
        sleep(2)
        print(f"The {Fore.RED + game_items[1] + Style.RESET_ALL} defeated the raptors!")
        print()
        sleep(3)
        print("Bad news...")
        print()
        sleep(2)
        print("...it wants dessert.")
        sleep(3)
        sattler_final_trex()

    elif game_items[1] == "dilophosaurus":
        print(f"Oh. It's just a {Fore.RED + game_items[1] + Style.RESET_ALL} up again a pack of velociraptors.")
        print()
        sleep(4)
        print("Maybe there's a chance...")
        print()
        sleep(3)
        print("Nope. The raptors had no issues there.")
        sleep(3)
        sattler_final_raptor()

    else:
        print("So good news/bad news.")
        print()
        sleep(3)
        print("You are still alive...")
        print()
        sleep(3)
        print(f"...but that fourth {Fore.RED + game_items[1] + Style.RESET_ALL}\njust joined the other raptors.")
        print()
        sleep(5)
        print("It seems they know each other. Probably not good for you.")
        sleep(5)
        sattler_final_raptor()

def sattler_final_trex():
    #     Roll dice to escape from the t-rex. Even number survives.
    print()
    print(f"Roll the dice to see if you will escape the {Fore.RED + game_items[1] + Style.RESET_ALL}.")
    print()
    sleep(2)
    print("Roll an even number to survive!")
    sleep(1)
    print()

    final_roll = roll_dice()
    
    if final_roll % 2 == 0:
        print(f"Dr. Sattler! You escaped the {Fore.RED + game_items[1] + Style.RESET_ALL}!")
        print()
        sleep(3)
        print("You, your lovers, and the kids leave the island via helicopter!")
        sleep(5)

    else:
        print(f"Too bad, Dr. Sattler.") 
        print()
        sleep(2)
        print(f"The {Fore.RED + game_items[1] + Style.RESET_ALL} defeated you.")
        print()
        sleep(2)
        print("Better luck in the 6th movie.\nWe hear you are coming back for that one.")
        sleep(5)

def sattler_final_raptor():
    #     Roll dice to escape from the raptors. Even number survives.
    print()
    print("Roll the dice to see if you will escape the raptors.") 
    print()
    sleep(2)
    print("Roll an even number to survive!")
    print()
    sleep(1)

    final_roll = roll_dice()
    
    if final_roll % 2 == 0:
        print(f"Dr. Sattler! You escaped the raptors!")
        print()
        sleep(2)
        print("You, your lovers, and the kids\nleave the island via helicopter!")
        sleep(2)

    else:
        print(f"Too bad, Dr. Sattler.")
        print()
        sleep(2)
        print("The raptors defeated you.")
        print()
        sleep(2)
        print("Better luck in the 6th movie.\nWe hear you are coming back for that one.")

def grant_ex_wives():

    if game_items[2] < 5:
        print("That seems like an expected amount of ex-wives\nfor a man who clearly loves what he is all about.")
        sleep(5)

    elif game_items[2] <= 30:
        print("We bet he thinks the ex-wives are\nthe problem and not him.") 
        sleep(5)

    else:
        print("Does he get a new wife every 6 months?")
        sleep(4)

def grant_coin_flip():

    print("Flip a coin with Malcolm.")
    sleep(2)
    print("This determines who helps the kids.")
    sleep(2)
    print(f"Heads you stay in the car and eat your {Fore.BLUE + game_items[0] + Style.RESET_ALL}.")
    sleep(3)
    print("Tails you go help the kids.")
    print()

    coin_result = flip_coin()

    if coin_result == "Heads":
        print("Phew! Malcolm will rescue the kids!")
        print()
        sleep(3)
        print("Malcolm grabs the flare.\nHe heads out towards the other car.")
        print()
        sleep(3)
        print("Malcolm lights the flare.\nHopefully he'll throw it soon.")
        print()
        sleep(3)
        print("In a shocking turn of events,\nMalcolm takes off running WITH THE FLARE.\nThe t-rex follows Malcolm,striking him.")
        print()
        sleep(4)
        print("Now you must rescue the kids!")
        print()
        sleep(3)

    else:
        print("The powers that be are not on your side.\nGet ready to rescue those kids.")
        print()
        sleep(4)
        print(f"You decided to distract the t-rex with {Fore.BLUE + game_items[0] + Style.RESET_ALL}.\nNot sure that's going to work, but go ahead.")
        print()
        sleep(6)
        print(f"While waving your {Fore.BLUE + game_items[0] + Style.RESET_ALL} around,\nMalcolm steps out of the car behind you\nand LIGHTS a flare.")
        print()
        sleep(6)
        print("Malcolm distracts the t-rex with the flare,\nleaving you to rescue the kids.\nThe t-rex CHARGES Malcolm and STRIKES him to the ground.")
        print()
        sleep(6)
        print("Hurry! Get to the kids.")
        print()
        sleep(3)

def grant_climb_tree():

    while True: 

        print(f"Do you climb the tree to rescue the kid\nor eat what's left of your {Fore.BLUE + game_items[0] + Style.RESET_ALL}?")
        print()
        print("Type RESCUE or EAT")
        tree_decision = input("> ").upper()
        print()

        if tree_decision == "RESCUE":
            print("You are so heroic!\nClimb that tree and rescue that kid.\nThe car seems super stable in that tree and probably won't move.")
            print()
            sleep(7)
            print("You get Timmy (did we mention his name was Timmy?)\nout of the car.")
            print()
            sleep(5)
            print("You hit the steering wheel\nand the car's tires move.")
            print()
            sleep(3)
            print("You and Timmy RACE down the tree as quickly\nas possible while the car follows you close behind.")
            print()
            sleep(4)
            print("You reach the ground right as the tree\nCRASHES into the dirt. You made it!\nCelebrate good times, COME ON!")
            print()
            sleep(6)
            break

        elif tree_decision == "EAT":
            print("Timmy (did we mention his name was Timmy?)\nneeds to be taught a lesson. Let that terrified\nchild figure out how to climb a tree.\nWhat a time to teach a lesson.")
            print()
            sleep(6)
            print(f"While you enjoy your {Fore.BLUE + game_items[0] + Style.RESET_ALL},\nTimmy emerges from the car!\nSee, you are such a good teacher.")
            print()
            sleep(5)
            print("For whatever reason (probably because he is\na traumatized 10 year old)....")
            print()
            sleep(4)
            print("Timmy LEAPS out of the tree.\nHe's heading right for you!")
            print()
            sleep(4)
            print("Looks like Timmy thought this was a trust fall exercise.")
            print()
            sleep(4)
            print(f"You throw your {Fore.BLUE + game_items[0] + Style.RESET_ALL} to the side\nand catch Timmy right before he hits the ground.\nThat was a close one!")
            print()
            sleep(5)
            break

        else: 
            print("That is not a valid option. Try again.")

def grant_field():

    print("What a beautiful sight to see!")
    print()
    sleep(3)
    print("Nothing could ruin this moment....")
    sleep(1)
    print("...")
    sleep(1)
    print("...")
    sleep(1)
    print("WHAT IS THAT?!?!")
    print()
    sleep(2)
    print(f"A {Fore.RED + game_items[1] + Style.RESET_ALL} emerges to probably wreak some havoc.")
    print()
    sleep(3)
    
    if game_items[1] == "velociraptor":
        print("The velociraptor viciously ATTACKS one of the herd.")
        print()
        sleep(3)
        print("The other raptors work to pick off the stragglers.") 
        print()
        sleep(3)
        print("Get out of there before they see you!")
        print()
        sleep(3)

    elif game_items[1] == "t-rex":
        print("It's shocking how that t-rex snuck up on y'all.")
        print()
        sleep(4)
        print("Surprised you didn't hear it coming.")
        print()
        sleep(3) 
        print("Get outta there!")
        print()
        sleep(2)

    elif game_items[1] == "dilophosaurus":
        print("The dilophosaurs sounds like a rattle snake,\nwhich is conveinent because it shoots venom at its enemies.")
        print()
        sleep(5)
        print("It's small, but deadly.")
        print()
        sleep(2)
        print("Don't wait around to see what happens! Leave!")
        print()
        sleep(2)

def grant_dice_role():

    print("Roll the dice to see if you will escape!")
    print()
    sleep(2)
    print("Roll an even number to survive!")
    print()

    final_roll = roll_dice()

    if final_roll % 2 == 0:
        print(f"Dr. Grant!\nYou and the kids escaped mostly unscathed!\nYou have reunited with Dr. Sattler and are leaving the island!")
        print()
        sleep(5)

    else:
        print(f"Too bad, Dr. Grant.\nThe dinos defeated you.\nAt least you got over your fear of children, right?")
        print()
        sleep(5)

def play_again():
    """Empties the game items list and asks whether or not the user wants to play again"""

    while len(game_items) > 0:
        game_items.pop()

    while True:
    
        print("Would you like to play again? Yes or No?")
        play_again_answer = input("> ").title()
        print(split)

        if play_again_answer.startswith("Y"):
            print()
            play_game()
            break

        elif play_again_answer.startswith("N"):
            print("Hope you enjoyed your time at the park! Goodbye!")
            break

        else: 
            print("That is not a valid option. Please try again.")

def play_game():
    """Get's the game started with an intro and first decision point"""
    
    game_intro()
    first_decision_point()     

play_game()