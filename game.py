"""
Your name: Shik Hur
Your student number: A01249842
"""
import math
import random
import itertools


def is_multiple_of_3(number: int) -> bool:
    """
    Determine if a number is a multiple of 3 or not.

    :param number: must be a integer
    :precondition: must be a positive number
    :postcondition: determine whether or not the input number is a multiple of 3
    :return: True or False

    >>> is_multiple_of_3(3)
    True
    >>> is_multiple_of_3(10)
    False
    """
    if number % 3 == 0:
        return True
    return False


def make_asteroid_belt_zone_in_board(board: dict, rows: int, coordinate: tuple) -> None:
    """
    Make asteroid belt zone in the board.

    :param board: must be a dictionary
    :param rows: must be a positive integer
    :param coordinate: must be a tuple
    :precondition: board must follow following format
        {(x-coordinate, y-coordinate): "Short description", ...}
        and the board size must be n * n
        and this function must be called in the make_board() function
    :postcondition: make asteroid belt zone in the board
    :return: None

    >>> test_board = {}
    >>> for x_coordinate in range(0, 25):
    ...     for y_coordinate in range(0, 25):
    ...         test_board[(x_coordinate, y_coordinate)] = "Test Description"
    >>>
    >>> make_asteroid_belt_zone_in_board(test_board, 25, (10, 10))
    >>> test_board[(10, 10)]
    'Asteroid Belt'
    """

    asteroid_belt_x_coordinates = list(range(0, rows))
    selected_x_coordinates = list(filter(is_multiple_of_3, asteroid_belt_x_coordinates))
    asteroid_belt_coordinates = list(enumerate(selected_x_coordinates))
    if coordinate in asteroid_belt_coordinates:
        board[coordinate] = "Asteroid Belt"
    if (coordinate[0] - 15) * (coordinate[0] - 15) + (coordinate[1] - 10) * (coordinate[1] - 10) == 25:
        board[coordinate] = "Asteroid Belt"


def make_board(rows: int, columns: int) -> dict[tuple, str]:
    """
    Setup a board to play game.

    :param rows: must be an integer
    :param columns: must be an integer
    :precondition: two inputs must be non-zero integers and be equal to or greater than 2
        Also, rows must be equal to columns
    :postcondition: make a dictionary that contains (rows * columns) keys
    :return: a dictionary that contains (rows * columns) keys. each key is a tuple that contains
        a set of coordinates, and each value is a short string description

    >>> game_board = make_board(3, 3)
    >>> coordinates = [coordinates for coordinates in game_board.keys()]
    >>> coordinates
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    """
    board = {}
    solar_system_boundary_coordinate = rows // 4
    worm_hole_boundary_coordinate = solar_system_boundary_coordinate + ((rows - solar_system_boundary_coordinate) // 8)
    vormir_boundary_coordinate = worm_hole_boundary_coordinate + ((rows - worm_hole_boundary_coordinate) // 2)
    nowhere_boundary_coordinate = vormir_boundary_coordinate + ((rows - vormir_boundary_coordinate) // 2)

    for x_coordinate in range(0, rows):
        for y_coordinate in range(0, columns):
            coordinate = (x_coordinate, y_coordinate)
            if x_coordinate < solar_system_boundary_coordinate and y_coordinate < solar_system_boundary_coordinate:
                board[coordinate] = "Solar System"
            elif x_coordinate < worm_hole_boundary_coordinate and y_coordinate < worm_hole_boundary_coordinate:
                board[coordinate] = "Worm Hole"
            elif x_coordinate < vormir_boundary_coordinate and y_coordinate < vormir_boundary_coordinate:
                board[coordinate] = "Vormir"
            elif x_coordinate < nowhere_boundary_coordinate and y_coordinate < nowhere_boundary_coordinate:
                board[coordinate] = "Nowhere"
            else:
                board[coordinate] = "Titan"

            make_asteroid_belt_zone_in_board(board, rows, coordinate)

    board[(rows - 1, columns - 1)] = "Boss"
    return board


def draw_map(board: dict, spaceship: dict) -> None:
    """
    Draw map.

    The user's location is marked with an X.

    :param board: must be a dictionary
    :param spaceship: must be a dictionary
    :precondition: board must follow following format
        {(x-coordinate, y-coordinate): "Short description", ...}
        and the board size must be n * n
        spaceship must contains the following keys:
        "name", "level", "x-coordinate", "y-coordinate", "class", "maxHP", "attack", "skill", "currentHP", "exp"
        and the spaceship must be in the board
    :postcondition: print the map based on the location of the spaceship
    :return: None

    """

    board_size = len(board)
    width_of_board = int(math.sqrt(board_size))
    print("-" * int(width_of_board))
    for y_coordinate in range(0, width_of_board):
        for x_coordinate in range(0, width_of_board):
            description = board[(y_coordinate, x_coordinate)]
            if (y_coordinate, x_coordinate) == (spaceship["x-coordinate"], spaceship["y-coordinate"]):
                print(f"\033[94m" + "X" + "\033[0m", end="")
            else:
                if description == "Solar System":
                    print(" ", end="")
                elif description == "Worm Hole":
                    print(f"\033[91m" + "@" + "\033[0m", end="")
                elif description == "Vormir":
                    print(f"\033[93m" + "-" + "\033[0m", end="")
                elif description == "Nowhere":
                    print(f"\033[94m" + "?" + "\033[0m", end="")
                elif description == "Boss":
                    print(f"\033[31m" + '"' + "\033[0m", end="")
                elif description == "Asteroid Belt":
                    print("⣿", end="")
                else:
                    print(f"\033[95m" + '"' + "\033[0m", end="")
        print()

    print("-" * int(width_of_board), "(⣿ : Asteroid Belt, You can NOT move to the area)")


def display_intro() -> None:
    """
     The start of the game.

    :precondition: none
    :postcondition: print opening lines on screen
    :return: none

    """

    intro_text_art = f"""       
           !
           !
           ^
          / \\
         /___\\
        |=   =|
        |     |
        |     |  
        |     |
        |     |
       /|##!##|\\
      / |##!##| \\
     /  |##!##|  \\
    |  / ^ | ^ \\  |
    | /  ( | )  \\ |
    |/   ( | )   \\|  
        ((   ))
       ((  :  ))      Hello Avengers! 23 days ago Sanctuary II which is a giant space mother ship attacked Earth.
       ((  :  ))      Unfortunately, It took the core of Earth! The core is essential to all life in Earth!
        ((   ))       But few days ago, it is said that the Sanctuary II was detected in the Titan area.
         (( ))        Avengers!! It's time to assemble! The rest of the Avengers have already left to destroy it!
          ( )         Unfortunately again, they sent a rescue signal!
           .          Pack your suit and weapons! Check your battle spaceship! Embark on this journey! Hurry up!
           .
           .
    """
    print(intro_text_art)
    print()


def display_classes() -> None:
    """
    Display classes of space ships.

    :precondition: None
    :postcondition: Display classes of space ship.
    :return: None

    >>> display_classes()
    1. Queen Jet: uses razor beam, was made of Adamantium
    2. Battle Cruiser: uses vulcan cannon, was made of Graphene
    3. Endurance: equip with guided missiles, was made of reinforced Aluminum
    4. USCSS Prometheus: uses shotgun and flamethrower, was made of Vibranium

    """
    print("1. Queen Jet: uses razor beam, was made of Adamantium")
    print("2. Battle Cruiser: uses vulcan cannon, was made of Graphene")
    print("3. Endurance: equip with guided missiles, was made of reinforced Aluminum")
    print("4. USCSS Prometheus: uses shotgun and flamethrower, was made of Vibranium")


def make_spaceship() -> dict:
    """
    Make a spaceship with 100 hp and specific specs where x = 0 and y = 0.

    This function gets user input and creates the space ship the user wants.

    :precondition: none
    :postcondition: create a dictionary contains the following keys:
        "name", "level", "x-coordinate", "y-coordinate", "class", "maxHP", "attack", "skill", "currentHP", "exp"
    :return: a dictionary contains basic information of the space ship

    """

    spaceship = {}
    name = input(f"\nSet your space ship name: ")
    while len(name) > 20:
        print(f"\nThat's too long! please input again")
        name = input(f"\nSet your space ship name: ")

    spaceship.update({"name": name, "level": 1, "x-coordinate": 0, "y-coordinate": 0})

    print(f"\nSelect the class of your space ship")
    display_classes()
    class_of_spaceship = input(f"\nSelect: ")
    numbers = ["1", "2", "3", "4"]
    while class_of_spaceship not in numbers:
        print(f"\nWrong selection! Please input again!")
        display_classes()
        class_of_spaceship = input(f"\nSelect: ")

    class_of_spaceship = int(class_of_spaceship)
    if class_of_spaceship == 1:
        spaceship.update({"class": "QueenZet", "maxHP": 100, "attack": 50, "defence": 3,
                          "skill": "Hyper Centered Laser Beam"})
    elif class_of_spaceship == 2:
        spaceship.update({"class": "BattleCruiser", "maxHP": 95, "attack": 60, "defence": 2,
                          "skill": "Bombard Vulcan Cannon"})
    elif class_of_spaceship == 3:
        spaceship.update({"class": "Endurance", "maxHP": 140, "attack": 35, "defence": 1, "skill": "Guided Missiles"})
    else:
        spaceship.update({"class": "USCSS", "maxHP": 80, "attack": 75, "defence": 5, "skill": "Shot gun with Flame"})

    spaceship.update({"currentHP": spaceship["maxHP"], "exp": 0})

    return spaceship


def ask_user_to_start_game() -> bool:
    """
    Ask the user if they want to start the game.

    :precondition: none
    :postcondition: prompt a message on screen and get user input and return True or False
    :return: True or False

    """
    answers = ["Y", "YES", "YE"]
    is_start_the_game = input(f"Do you want to start this journey? [Y/N] : ")
    if is_start_the_game.upper().strip() in answers:
        return True
    return False


def show_space_ship_information(spaceship: dict) -> None:
    """
    Show the information of user's spaceship.

    :param spaceship: must be a dictionary
    :precondition: input dictionary must contains the following keys:
        "name", "level", "x-coordinate", "y-coordinate", "class", "maxHP", "attack", "skill", "currentHP", "exp"
    :postcondition: display the information Of user's spaceship
    :return: None

    >>> ship = {"name": "Test ship", "level": 1, "x-coordinate": 0, "y-coordinate": 0, "class": "QueenZet", \
    "maxHP": 100, "attack": 50, "defence": 1, "skill": "Hyper Centered Laser Beam", "currentHP": 100,\
    "exp": 1100}
    >>> show_space_ship_information(ship)
    <BLANKLINE>
    Your Space ship \033[94mTest ship \033[0minfo :
    ----------------------------------------------------------------------
    |             Name :                                Test ship        |
    |            Level :                                        1        |
    |         Location :                                   (0, 0)        |
    |            Class :                                 QueenZet        |
    |           Max HP :                                      100        |
    |       Current HP :                                      100        |
    |           Attack :                                       50        |
    |          Defence :                                        1        |
    |            Skill :                Hyper Centered Laser Beam        |
    |              Exp :                              1100 / 1000        |
    ----------------------------------------------------------------------
    """
    output_format = "|    %15s %40s"
    end_string = "%10s" % "|\n"
    line_length = 70
    print(f"\nYour Space ship " + "\033[94m" + f"{spaceship['name']} \033[0m" + "info :")
    print("-" * line_length)
    print(output_format % ("Name :", spaceship['name']), end=end_string)
    print(output_format % ("Level :", spaceship['level']), end=end_string)
    print(output_format % ("Location :", (spaceship['x-coordinate'], spaceship['y-coordinate'])), end=end_string)
    print(output_format % ("Class :", spaceship['class']), end=end_string)
    print(output_format % ("Max HP :", spaceship['maxHP']), end=end_string)
    print(output_format % ("Current HP :", spaceship['currentHP']), end=end_string)
    print(output_format % ("Attack :", spaceship['attack']), end=end_string)
    print(output_format % ("Defence :", spaceship['defence']), end=end_string)
    print(output_format % ("Skill :", spaceship['skill']), end=end_string)
    print(output_format % ("Exp :", f"{spaceship['exp']} / {spaceship['level'] * 1000}"), end=end_string)
    print("-" * line_length)


def is_alive(spaceship: dict) -> bool:
    """
    Check if the user's spaceship is destroyed.

    :param spaceship: must be a dictionary
    :precondition: input dictionary must contains the following keys:
        "name", "level", "x-coordinate", "y-coordinate", "class", "maxHP", "attack", "skill", "currentHP", "exp"
    :postcondition: determine the spaceship's current hp is 0 or not and return boolean value
    :return: True or False

    >>> ship = {"name": "Test", "level": 1, "x-coordinate": 0, "y-coordinate": 0, "class": "QueenZet", "maxHP": 100,\
    "attack": 50, "defence": 3, "skill": "Hyper Centered Laser Beam", "currentHP": 100, "exp": 0}
    >>> is_alive(ship)
    True

    >>> ship["currentHP"] = 0
    >>> is_alive(ship)
    False

    """
    return spaceship["currentHP"] > 0


def print_numbered_list_of_direction() -> None:
    """
    Print the numbered list of direction.
    
    :precondition: must be called in the get_user_choice() function
    :postcondition: print numbered list of direction to users
    :return: None
    
    >>> print_numbered_list_of_direction()
    <BLANKLINE>
    Where are you heading ?
    1. North
    2. South
    3. West
    4. East
    Or if you want to quit, enter 'Q'
    """
    print("\nWhere are you heading ?")
    print("1. North")
    print("2. South")
    print("3. West")
    print("4. East")
    print("Or if you want to quit, enter 'Q'")


def get_user_choice() -> str:
    """
    Get the direction users want to go.

    :precondition: none
    :postcondition: return one of 'N', 'S', 'W', 'E', and 'Q' strings
    :return: one of 'N', 'S', 'W', 'E', and 'Q' strings

    """
    list_of_directions = ["1", "2", "3", "4", "N", "S", "W", "E", "NORTH", "SOUTH", "WEST", "EAST", "Q", "QUIT"]
    print_numbered_list_of_direction()
    user_input = input("\n\tSelect : ")
    user_input_upper = user_input.upper()
    while user_input_upper not in list_of_directions:
        print(f"{user_input} is wrong input! please try again!")
        print_numbered_list_of_direction()
        user_input = input("\tSelect : ")
        user_input_upper = user_input.upper()

    if user_input_upper[0] == "Q":
        return_value = "Q"
    else:
        return_value = user_input_upper[0]
        if user_input_upper.isdigit():
            return_value_index = list_of_directions.index(user_input_upper[0]) + 4
            return_value = list_of_directions[return_value_index]

    return return_value


def find_maximum_coordinate_of_board(board: dict) -> tuple:
    """
    Find the destination of the game.

    :param board: must be a dictionary
    :precondition: board must follow following format
        {(x-coordinate, y-coordinate): "Short description", ...}
    :postcondition: get the destination coordinates as a tuple
    :return: a tuple contains the x and y coordinates

    >>> game_board = make_board(2, 2)
    >>> find_maximum_coordinate_of_board(game_board)
    (1, 1)
    >>> game_board2 = make_board(4, 4)
    >>> find_maximum_coordinate_of_board(game_board2)
    (3, 3)
    """
    max_coordinate = (0, 0)
    for coordination in board.keys():
        if coordination > max_coordinate:
            max_coordinate = coordination

    return max_coordinate


def validate_move(board: dict, spaceship: dict, direction: str) -> bool:
    """
    Determine if a spaceship is on the board or not after moving.

    :param board: must be a dictionary
    :param spaceship: must be a dictionary
    :param direction: must be a string
    :precondition: board must follow following format
        {(x-coordinate, y-coordinate): "Short description", ...}
        spaceship must contains the following keys:
        "name", "level", "x-coordinate", "y-coordinate", "class", "maxHP", "attack", "skill", "currentHP", "exp"
        and direction must be one of "N", "S", "W", "E" strings
    :postcondition: determine if a spaceship is on the board or not after moving
    :return: True or False

    >>> game_board = make_board(2, 2)
    >>> ship = {"name": "Test", "level": 1, "x-coordinate": 0, "y-coordinate": 0, "class": "QueenZet", "maxHP": 100,\
    "attack": 50, "defence": 3, "skill": "Hyper Centered Laser Beam", "currentHP": 100, "exp": 0}
    >>> validate_move(game_board, ship, "N")
    False

    >>> validate_move(game_board, ship, "S")
    True
    """
    max_coordinate = find_maximum_coordinate_of_board(board)
    current_spaceship_x_coordinate = spaceship["x-coordinate"]
    current_spaceship_y_coordinate = spaceship["y-coordinate"]
    if direction == "N":
        current_spaceship_x_coordinate -= 1
    elif direction == "S":
        current_spaceship_x_coordinate += 1
    elif direction == "W":
        current_spaceship_y_coordinate -= 1
    else:
        current_spaceship_y_coordinate += 1

    if current_spaceship_x_coordinate < 0 or current_spaceship_y_coordinate < 0:
        return False
    elif current_spaceship_x_coordinate > max_coordinate[0] or \
            current_spaceship_y_coordinate > max_coordinate[1]:
        return False
    elif board[(current_spaceship_x_coordinate, current_spaceship_y_coordinate)] == "Asteroid Belt":
        return False

    return True


def move_spaceship(user_choice: str, spaceship: dict) -> None:
    """
    Move spaceship based on what users input.

    :param user_choice: must be a string
    :param spaceship: must be a dictionary
    :precondition: user_choice must be one of "N", "S", "W", and "E"
        spaceship must contains the following keys:
        "name", "level", "x-coordinate", "y-coordinate", "class", "maxHP", "attack", "skill", "currentHP", "exp"
        And, validate_move() function must be executed before calling this function
    :postcondition: the spaceship's position updates
    :return: None

    >>> ship = {"name": "Test", "level": 1, "x-coordinate": 0, "y-coordinate": 0, "class": "QueenZet", "maxHP": 100,\
    "attack": 50, "defence": 3, "skill": "Hyper Centered Laser Beam", "currentHP": 100, "exp": 0}
    >>> move_spaceship("S", ship)
    >>> (ship["x-coordinate"], ship["y-coordinate"])
    (1, 0)

    >>> move_spaceship("E", ship)
    >>> (ship["x-coordinate"], ship["y-coordinate"])
    (1, 1)
    """
    if user_choice == "N":
        spaceship["x-coordinate"] -= 1
    elif user_choice == "S":
        spaceship["x-coordinate"] += 1
    elif user_choice == "E":
        spaceship["y-coordinate"] += 1
    else:
        spaceship["y-coordinate"] -= 1


def calculate_20_percent_chance() -> bool:
    """
    Calculate 20% chance.

    This function is called in the following situations:
    There is a 20% chance of encountering a foe.
    There is a 20% chance of getting damage from a foe when users choose running away.
    Foes have a 20% chance to run away.

    :precondition: none
    :postcondition: determine if users have a 20% chance
    :return: True or False
    """
    random_number = random.randint(1, 6)
    if random_number == 1:
        return True
    return False


def make_foes(map_description: str) -> dict:
    """
    Make a foe has certain HP, attack, defence.

    A strong foe is created according to the map description.
    The level of the foe increases in the order of the following areas.
    Solar System < Worm Hole < Vormir < Nowhere < Titan.
    The name of the foe is randomly generated according to the map.

    :param map_description: must be a string
    :precondition: the input string must be one of these strings: Solar System, Worm Hole, Vormir, Nowhere, Titan
    :postcondition: make a foe as a dictionary contains several keys and values
        {"name": , "HP": , "attack": , "defence": , "exp": }
    :return: a dictionary

    """
    solar_system_foes = ["Ultron", "Ulysses", "Ivan Vanko"]
    worm_hole_foes = ["Loki", "Chitauri", "Alien"]
    nowhere_foes = ["Ronan", "Hela", "Predator"]
    titan_foes = ["Ego", "Doom", "Jerico"]
    vormir_foes = ["Red Skull", "Kang", "Doctor Light"]

    foe = {"name": "".join(random.sample(solar_system_foes, 1)), "HP": 100, "attack": 5, "defence": 2, "exp": 400}
    if map_description == "Worm Hole":
        foe = {"name": "".join(random.sample(worm_hole_foes, 1)), "HP": 110, "attack": 10, "defence": 3, "exp": 700}
    elif map_description == "Nowhere":
        foe = {"name": "".join(random.sample(nowhere_foes, 1)), "HP": 120, "attack": 15, "defence": 4, "exp": 1000}
    elif map_description == "Vormir":
        foe = {"name": "".join(random.sample(vormir_foes, 1)), "HP": 130, "attack": 18, "defence": 5, "exp": 1300}
    elif map_description == "Titan":
        foe = {"name": "".join(random.sample(titan_foes, 1)), "HP": 140, "attack": 20, "defence": 5, "exp": 1500}
    elif map_description == "Boss":
        foe = {"name": "Sanctuary II", "HP": 400, "attack": 25, "defence": 7, "exp": 3000}

    return foe


def check_if_goal_attained(boss: dict) -> bool:
    """
    Check if the user has defeated the boss.

    :param boss: must be a dictionary
    :precondition: input dictionary must contains following keys
        {"name": , "HP": , "attack": , "defence": , "exp": }
        and the boss had to be created when the game started
    :postcondition: determine the boss of the game is dead
    :return: True or False

    >>> game_boss = {"name": "Test boss" , "HP": 100, "attack": 0, "defence": 0}
    >>> check_if_goal_attained(game_boss)
    False

    >>> game_boss = {"name": "Test boss" , "HP": 0, "attack": 0, "defence": 0}
    >>> check_if_goal_attained(game_boss)
    True
    """
    return boss["HP"] <= 0


def print_battle_graphic() -> None:
    """
    Display ASCII art to signal the start of a battle.

    :precondition: this function must be called when a battle starts
    :postcondition: print ASCII art
    :return: None

    """
    print("""
                 .  . '    .
              '   .            . '            .                +
                      `                          '    . '
                .                         ,'`.                         .
           .                  .."    _.-;'    `.              .
                      _.-"`.##%"_.--" ,'        `.           "#"     ___,,od000
                   ,'"-_ _.-.--"\\   ,'            `-_       '%#%',,/////00000HH
                 ,'     |_.'     )`/-     __..--""`-_`-._    J L/////00000HHHHM
         . +   ,'   _.-"        / /   _-""           `-._`-_/___\\///0000HHHHMMM
             .'_.-""      '    :_/_.-'                 _,`-/__V__\0000HHHHHMMMM
         . _-""                         .        '   _,////\\  |  /000HHHHHMMMMM
        _-"   .       '  +  .              .        ,//////0\\ | /00HHHHHHHMMMMM
               `                                   ,//////000\\|/00HHHHHHHMMMMMM
        .             '       .  ' .   .       '  ,//////00000|00HHHHHHHHMMMMMM
             .             .    .    '           ,//////000000|00HHHHHHHMMMMMMM
                          .  '      .       .   ,///////000000|0HHHHHHHHMMMMMMM
          '             '        .    '         ///////000000000HHHHHHHHMMMMMMM
                            +  .  . '    .     ,///////000000000HHHHHHHMMMMMMMM
             '      .              '   .       ///////000000000HHHHHHHHMMMMMMMM
           '                  . '              ///////000000000HHHHHHHHMMMMMMMM
                                   .   '      ,///////000000000HHHHHHHHMMMMMMMM
               +         .        '   .    .  ////////000000000HHHHHHHHMMMMMMhs""")


def is_user_choice_run_away(foe: dict) -> bool:
    """
    Ask users whether to fight or not with a foe.

    :param foe: must be a dictionary
    :precondition: foe must contains the following keys:
        "name", "HP", "attack", "defence", "exp"
    :postcondition: return boolean value depends on user choice
    :return: True or False

    """
    input_list = ["Y", "y", "N", 'n']
    print(f"You encountered {foe['name']}! Do you want to fight? [Y / N] : ", end="")
    user_choice = input()
    while user_choice not in input_list:
        print(f"Your input {user_choice} is wrong! Please try again")
        print(f"Do you want to fight with {foe['name']}? [Y / N] : ", end="")
        user_choice = input()

    user_choice = user_choice.upper()
    if user_choice == "N":
        return True
    return False


def try_to_flee_from_foe(spaceship: dict, foe: dict) -> None:
    """
    Go through the process when users select flight.

    There is 20% chance of getting damage when users try to flee from a foe.

    :param spaceship: must be a dictionary
    :param foe: must be a dictionary
    :precondition: spaceship must contains the following keys:
        "name", "level", "x-coordinate", "y-coordinate", "class", "maxHP", "attack", "skill", "currentHP", "exp"
        foe must contains the following keys:
        "name", "HP", "attack", "defence", "exp"
    :postcondition: users will take damage, but the probability is 20%
    :return: None

    """

    line = ""
    for dash in itertools.repeat("-", 70):
        line += dash
    print(f"\nTry to flee! There is 20% to get damage from the {foe['name']}")
    if calculate_20_percent_chance():
        damage = foe["attack"] - spaceship["defence"]
        spaceship["currentHP"] -= damage
        print(f"\nUnlucky! Your spaceship got damage from the {foe['name']}")
        print("\n" + line)
        print(f"|Your current hp : {spaceship['currentHP']}|")
        print(line)
    else:
        print("\nYou succeeded in escaping safely!\n")


def user_choice_in_battle(spaceship_skill: str, foe_name: str) -> bool:
    """
    Get user choice between fight or flee.

    :param spaceship_skill: must be a string
    :param foe_name: must be a string
    :precondition: this function must be called in the battle_with_foe() function
    :postcondition: return user choice
    :return: True for fighting, False for trying to flee

    """
    valid_input = [str(number) for number in range(1, 3)]
    print(f"\n{foe_name} is ready for battle in front of you! and your {spaceship_skill} is ready!")
    print(f"1. Attack with {spaceship_skill}\n2. Try to flee")
    user_choice = input("\tSelect: ")
    while user_choice not in valid_input:
        print("\nCommander, that can't be done. Please give the appropriate orders!")
        print(f"1. Attack with {spaceship_skill}\n2. Try to flee")
        user_choice = input("\tSelect: ")

    if user_choice == "1":
        return True
    return False


def user_attack_foe(spaceship: dict, foe: dict) -> None:
    """
    Attack a foe.

    :param spaceship: must be a dictionary
    :param foe: must be a dictionary
    :precondition: spaceship must contains the following keys:
        "name", "level", "x-coordinate", "y-coordinate", "class", "maxHP", "attack", "skill", "currentHP", "exp"
        foe must contains the following keys:
        "name", "HP", "attack", "defence", "exp"
    :postcondition: the hp of foe is reduced by the amount of the point of spaceship's attack
    :return: None

    >>> ship = {"name": "Test ship", "level": 1, "x-coordinate": 0, "y-coordinate": 0, "class": "QueenZet", \
    "maxHP": 100, "attack": 50, "defence": 3, "skill": "Hyper Centered Laser Beam", "currentHP": 100, "exp": 0}
    >>> test_foe = {"name": "Test foe" , "HP": 60, "attack": 2, "defence": 10}
    >>> user_attack_foe(ship, test_foe)
    <BLANKLINE>
    Hyper Centered Laser Beam!!!!!
    >>> test_foe
    {'name': 'Test foe', 'HP': 20, 'attack': 2, 'defence': 10}

    """
    print(f"\n{spaceship['skill']}!!!!!")
    foe["HP"] = foe["HP"] - abs(spaceship["attack"] - foe["defence"])


def foe_attack_user(foe: dict, spaceship: dict) -> None:
    """
    Users get attacked by a foe.

    :param foe: must be a dictionary
    :param spaceship: must be a dictionary
    :precondition: foe must contains the following keys:
        "name", "HP", "attack", "defence", "exp"
        spaceship must contains the following keys:
        "name", "level", "x-coordinate", "y-coordinate", "class", "maxHP", "attack", "skill", "currentHP", "exp"
    :postcondition: the hp of user's spaceship is reduced by the amount of the point of foe's attack
    :return: None

    >>> ship = {"name": "Test ship", "level": 1, "x-coordinate": 0, "y-coordinate": 0, "class": "QueenZet", \
    "maxHP": 100, "attack": 50, "defence": 1, "skill": "Hyper Centered Laser Beam", "currentHP": 100, "exp": 0}
    >>> test_foe = {"name": "Test foe" , "HP": 60, "attack": 5, "defence": 10}
    >>> foe_attack_user(test_foe, ship)
    Test foe is attacking!!
    >>> expected_ship = {'name': 'Test ship', 'level': 1, 'x-coordinate': 0, 'y-coordinate': 0, 'class': 'QueenZet', \
    'maxHP': 100, 'attack': 50, 'defence': 1, 'skill': 'Hyper Centered Laser Beam', 'currentHP': 96, 'exp': 0}
    >>> ship == expected_ship
    True
    """
    print(f"{foe['name']} is attacking!!")
    spaceship["currentHP"] = spaceship["currentHP"] - (abs(foe["attack"] - spaceship["defence"]))


def take_turn_of_battle(spaceship: dict, foe: dict) -> None:
    """
    Proceed one turn of a battle.

    :param spaceship: must be a dictionary
    :param foe: must be a dictionary
    :precondition: spaceship must contains the following keys:
        "name", "level", "x-coordinate", "y-coordinate", "class", "maxHP", "attack", "skill", "currentHP", "exp"
        foe must contains the following keys:
        "name", "HP", "attack", "defence", "exp"
    :postcondition: one battle turn is played in which the user attacks first and return
    :return: None

     >>> ship = {"name": "Test ship", "level": 1, "x-coordinate": 0, "y-coordinate": 0, "class": "QueenZet", \
    "maxHP": 100, "attack": 50, "defence": 1, "skill": "Hyper Centered Laser Beam", "currentHP": 100, "exp": 0}
    >>> test_foe = {"name": "Test foe" , "HP": 60, "attack": 10, "defence": 5}
    >>> take_turn_of_battle(ship, test_foe)
    <BLANKLINE>
    Hyper Centered Laser Beam!!!!!
    Test foe's current HP : 15
    Test foe is attacking!!

    >>> expected_ship = {"name": "Test ship", "level": 1, "x-coordinate": 0, "y-coordinate": 0, "class": "QueenZet", \
    "maxHP": 100, "attack": 50, "defence": 1, "skill": "Hyper Centered Laser Beam", "currentHP": 91, "exp": 0}
    >>> ship == expected_ship
    True
    >>> test_foe
    {'name': 'Test foe', 'HP': 15, 'attack': 10, 'defence': 5}

    """
    user_attack_foe(spaceship, foe)
    if foe["HP"] <= 0:
        print(f"\n{foe['name']} is destroyed! You won!")
        return

    print(f"{foe['name']}'s current HP : {foe['HP']}")
    foe_attack_user(foe, spaceship)
    if spaceship["currentHP"] <= 0:
        print(f"\n{spaceship['name']} is in danger! Mayday! Try to flee!")
        return


def display_level_up_message(level: int) -> None:
    """
    Display level-up message on screen.

    :param level: must be a positive integer
    :precondition: this function must be called in the check_and_process_level_up() function
    :postcondition: print messages on screen
    :return: None

    >>> display_level_up_message(2)
    <BLANKLINE>
    **********************************************************************
    Congratulation! Level-up! Your level now : 2!
    Your spaceship's attack, defense, and max hp point was increased!
    **********************************************************************
    """
    print("\n" + "*" * 70)
    print(f"Congratulation! Level-up! Your level now : {level}!")
    print(f"Your spaceship's attack, defense, and max hp point was increased!")
    print("*" * 70)


def level_up_skill(spaceship: dict) -> None:
    """
    Change skill name based on level of user's spaceship.

    :param spaceship: must be a dictionary
    :precondition: spaceship must contains the following keys:
        "name", "level", "x-coordinate", "y-coordinate", "class", "maxHP", "attack", "skill", "currentHP", "exp"
        and this function must be called when the user has leveled up
    :postcondition: change the name of skill of the spaceship
    :return: None

    >>> ship = {"name": "Test ship", "level": 2, "x-coordinate": 0, "y-coordinate": 0, "class": "QueenZet", \
    "maxHP": 100, "attack": 50, "defence": 1, "skill": "Hyper Centered Laser Beam", "currentHP": 100,\
    "exp": 0}
    >>> level_up_skill(ship)
    >>> ship["skill"]
    'Enhanced Laser Shot'

    >>> ship["level"] = 4
    >>> level_up_skill(ship)
    >>> ship["skill"]
    'Triple Mastered Laser Beam'

    """
    queen_zet_skill_list = ["Enhanced Laser Shot", "Double Enhanced Laser Shot", "Triple Mastered Laser Beam"]
    battle_cruiser_skill_list = ["Yamato Cannon", "Double Yamato Cannon", "Mastered Yamato Cannon"]
    endurance_skill_list = ["Double Guided Missiles", "Triple Guided Missiles", "Triple Hellfire Missiles"]
    uscss_skill_list = ["Blue Fire Shot Gun", "U-232 Shot Gun", "Triple U-232 Blue Fire Shot Gun"]
    if spaceship["level"] >= 4:
        skill_index = 2
    else:
        skill_index = spaceship["level"] - 2
    if skill_index < 0:
        skill_index = 0

    class_of_spaceship = spaceship["class"]
    if class_of_spaceship == "QueenZet":
        spaceship["skill"] = queen_zet_skill_list[skill_index]
    elif class_of_spaceship == "BattleCruiser":
        spaceship["skill"] = battle_cruiser_skill_list[skill_index]
    elif class_of_spaceship == "Endurance":
        spaceship["skill"] = endurance_skill_list[skill_index]
    elif class_of_spaceship == "USCSS":
        spaceship["skill"] = uscss_skill_list[skill_index]


def check_and_process_level_up(spaceship: dict) -> None:
    """
    Check if the user can level up and proceed with leveling up.

    :param spaceship: must be a dictionary
    :precondition: spaceship must contains the following keys:
        "name", "level", "x-coordinate", "y-coordinate", "class", "maxHP", "attack", "skill", "currentHP", "exp"
    :postcondition: Check if the user can level up and proceed with leveling up.
    :return: None

    >>> ship = {"name": "Test ship", "level": 1, "x-coordinate": 0, "y-coordinate": 0, "class": "QueenZet", \
    "maxHP": 100, "attack": 50, "defence": 1, "skill": "Hyper Centered Laser Beam", "currentHP": 100,\
    "exp": 1100}
    >>> check_and_process_level_up(ship)
    <BLANKLINE>
    **********************************************************************
    Congratulation! Level-up! Your level now : 2!
    Your spaceship's attack, defense, and max hp point was increased!
    **********************************************************************
    <BLANKLINE>
    Your Space ship \033[94mTest ship \033[0minfo :
    ----------------------------------------------------------------------
    |	          Name :                                Test ship        |
    |	         Level :                                        2        |
    |	      Location :                                   (0, 0)        |
    |	         Class :                                 QueenZet        |
    |	        Max HP :                                      200        |
    |	    Current HP :                                      200        |
    |	        Attack :                                       60        |
    |	       Defence :                                        3        |
    |	         Skill :                      Enhanced Laser Shot        |
    |	           Exp :                               100 / 2000        |
    ----------------------------------------------------------------------
    >>> expected_ship = {"name": "Test ship", "level": 2, "x-coordinate": 0, "y-coordinate": 0, "class": "QueenZet", \
    "maxHP": 200, "attack": 60, "defence": 3, "skill": "Enhanced Laser Shot", "currentHP": 200,\
    "exp": 100}
    >>> ship == expected_ship
    True

    """
    if spaceship["exp"] >= spaceship["level"] * 1000:
        spaceship["maxHP"] += spaceship["level"] * 100
        spaceship["currentHP"] = spaceship["maxHP"]
        spaceship["attack"] += spaceship["level"] * 10
        spaceship["defence"] += spaceship["level"] * 2
        while spaceship["exp"] >= spaceship["level"] * 1000:
            spaceship["exp"] -= spaceship["level"] * 1000
            spaceship["level"] += 1
        display_level_up_message(spaceship["level"])
        level_up_skill(spaceship)
        show_space_ship_information(spaceship)


def battle_with_foe(spaceship: dict, foe: dict) -> None:
    """
    Start a battle with a foe.

    :param spaceship: must be a dictionary
    :param foe: must be a dictionary
    :precondition: spaceship must contains the following keys:
        "name", "level", "x-coordinate", "y-coordinate", "class", "maxHP", "attack", "skill", "currentHP", "exp"
        foe must contains the following keys:
        "name", "HP", "attack", "defence", "exp"
    :postcondition: proceed the battle
    :return: None

    """

    is_user_won = False
    print(f"\nStart Battle with {foe['name']}! Good luck!")
    while is_user_won is False:
        is_user_choice_fight = user_choice_in_battle(spaceship['skill'], foe['name'])

        if is_user_choice_fight is True:
            take_turn_of_battle(spaceship, foe)
        else:
            if foe["name"] == "Sanctuary II":
                print("\n You can NOT run away from the Sanctuary II")
                continue
            try_to_flee_from_foe(spaceship, foe)
            break
        if foe["HP"] <= 0:
            is_user_won = True
        elif spaceship["currentHP"] <= 0:
            break

    if is_user_won is True:
        spaceship["exp"] += foe["exp"]
        print(f"\nYou got {foe['exp']} exp points! Your exp: {spaceship['exp']} / {spaceship['level'] * 1000}\n")
        check_and_process_level_up(spaceship)


def display_boss() -> None:
    """
    Print ASCII art for the battle with the boss, Sanctuary II.

    :precondition: this function must be called when users meet the boss
    :postcondition: print ASCII art
    :return: None
    """
    print("""
      .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
    """)
    print("\n\t\033[94mSanctuary II appears!\033[0m\n")


def display_ending() -> None:
    """
    Display ending credit.

    :precondition: user must defeat Sanctuary II
    :postcondition: print ending credit
    :return: None

    >>> display_ending()
    <BLANKLINE>
    \033[95mYou defeated Sanctuary II and the universe is at peace.
    Lost lives have returned. Well done. Everyone thank you for your hard work!
    <BLANKLINE>
    <BLANKLINE>
    made by Shik Hur, COMP1510 Assignment3
    """
    print("\n\033[95mYou defeated Sanctuary II and the universe is at peace.")
    print("Lost lives have returned. Well done. Everyone thank you for your hard work!")
    print("\n\nmade by Shik Hur, COMP1510 Assignment3")


def game() -> int:  # called from main
    """
    Drive the main game loop.
    """
    display_intro()
    if ask_user_to_start_game() is False:
        print(f"\nOh, Ok... See you again. Let's quit the game.")
        return 0

    spaceship = make_spaceship()
    show_space_ship_information(spaceship)

    achieved_goal = False
    rows = 25
    columns = 25
    board = make_board(rows, columns)
    boss = make_foes("Boss")
    print(f"\n\t{rows} * {columns} map and your {spaceship['class']} have been setup!")
    print("\tYour mission : Find Sanctuary II and defeat them!")
    print("\t\tThere are reports that the Sanctuary II is to the southeast of the Titan area")
    print("\n\tOK! Let's move!")

    while is_alive(spaceship) and not achieved_goal:
        draw_map(board, spaceship)
        direction = get_user_choice()
        if direction == "Q":
            print("Quit the game. Bye.")
            return 0
        valid_move = validate_move(board, spaceship, direction)
        if valid_move:
            move_spaceship(direction, spaceship)
            if (spaceship["x-coordinate"], spaceship["y-coordinate"]) == (rows - 1, columns - 1):
                display_boss()
                battle_with_foe(spaceship, boss)
                achieved_goal = check_if_goal_attained(boss)
                continue

            there_is_a_challenger = calculate_20_percent_chance()
            if there_is_a_challenger:
                description_of_user_location = board[(spaceship["x-coordinate"], spaceship["y-coordinate"])]
                foe = make_foes(description_of_user_location)
                print_battle_graphic()
                print(f"\n\t{foe['name']} has appeared from {description_of_user_location}")
                user_choice_flee = is_user_choice_run_away(foe)
                if user_choice_flee:
                    try_to_flee_from_foe(spaceship, foe)
                else:
                    battle_with_foe(spaceship, foe)

            else:
                print("\tThat's a good move! No enemies found.")
        else:
            print("\n\tCaution! you can't move there! There is Asteroid Belt! Please move again!")

    if achieved_goal:
        print("\033[94m" + "Congratulation! You defeated Sanctuary II")
        display_ending()
    else:
        print("Sorry! you lost the game. Your character is DEAD!")

    return 0


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
