from print_statements import PrintStatements
from human_game_logic import HumanGameLogic
from ai_game_logic import AiGameLogic

starting_sticks = 0
max_take = 3

def create_single_or_multi_player_game():
    player_number = 0
    PrintStatements().print_options()
    while player_number not in range(1, 4):
        try:
            PrintStatements(0).print_choose_number()
            player_number = int(input("> "))
            PrintStatements(player_number).print_choose_number()
        except TypeError:
            print("Invalid selection. Must be an integer.")
    return player_number

def set_starting_sticks(starting_sticks):
    PrintStatements().print_set_sticks()
    while starting_sticks not in range(10, 101):
        try:
            starting_sticks = int(input("> "))
        except TypeError:
            print("Invalid selection. Must be an integer.")
    PrintStatements(starting_sticks).print_set_sticks()
    return starting_sticks

def select_game_mode(number, sticks, max_take):
    if number == 1:
        HumanGameLogic(sticks, max_take).multi_player_game()
    elif number == 2:
        AiGameLogic(sticks, max_take).computer_game('easy')
    elif number == 3:
        ComputerGameLogic(sticks, max_take).computer_game('hard')
    else:
        raise ValueError("Needed an integer from 1 to 3.")


def main():
    PrintStatements(max_take).print_welcome_players()
    sticks = set_starting_sticks(starting_sticks)
    select_game_mode(create_single_or_multi_player_game(), sticks, max_take)


if __name__ == '__main__':
    main()
