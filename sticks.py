from print_statements import PrintStatements



bounds = [1,3]

def create_single_or_multi_player_game():
    PrintStatements.print_options()
    player_number = 0
    while player_number not in range(1, 4):
        try:
            PrintStatements(0).print_choose_number()
            player_number = int(input("> "))
            PrintStatements(player_number).print_choose_number()
        except TypeError:
            print("Invalid selection. Must be an integer.")

def set_starting_sticks():
    PrintStatements.print_set_sticks()
    starting_sticks = 0
    while starting_sticks not in range(10, 101):
        try:
            starting_sticks = int(input("> "))
        except TypeError:
            print("Invalid selection. Must be an integer.")
    PrintStatements(starting_sticks).print_set_sticks()

def welcome_players():
    PrintStatements.print_welcome_players()
    PrintStatements(bounds[1]).print_welcome_players()
    set_starting_sticks()
    create_single_or_multi_player_game()








def main():
    pass




if __name__ == '__main__'
    main()
