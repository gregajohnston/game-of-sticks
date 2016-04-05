class PrintStatements:

    def __init__(self, selection=0):
        self.selection = selection
        pass

    def print_options(self):
        print("Options: ")
        print("  1) Play against a friend.")
        print("  2) Play against the computer.")
        print("  3) Play against the trained computer.")

    def print_choose_number(self):
        if self.selection == 0:
            print("Please select a number:")
        elif self.selection == 1:
            print("May the best person win!")
        elif self.selection == 2:
            print("I'll take it easy on you this time.")
        elif self.selection == 3:
            print("Good luck human. You'll need it.")
        else:
            print("Please pick a number from 1 to 3.")

    def print_set_sticks(self):
        if self.selection == 0:
            print("How many sticks are on the table initially? Select from 10 to 100:")
        else:
            print("The game start with {} sticks.".format(self.selection))

    def print_welcome_players(self):
            print("Welcome to the Game of Sticks!")
            print("The object is to make your opponent pick up the last stick.")
            print("You must pick up 1 stick every turn, but may grab up to {} sticks.\n".format(self.selection))
