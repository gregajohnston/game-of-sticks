class HumanGameLogic:

    def __init__(self, stick_count=20, max_amount_removable=3):
        self.stick_count = stick_count
        self.max_amount_removable = max_amount_removable

    def multi_player_game(self):
        current_player = 2
        while self.stick_count > 0:
            current_player = [value for value in [1, 2] if value != current_player][0]
            print("Stick count = {}. Player {}\'s turn to choose.".format(self.stick_count, current_player))
            self.stick_count = self.remove_sticks(self.stick_count, self.max_amount_removable)
        print("Player {} drew the last stick and lost the game!".format(current_player))
        current_player = [value for value in [1, 2] if value != current_player][0]
        print("Player {} wins!".format(current_player))

    def remove_sticks(self, number_left, max_remove):
        grab_value = 0
        while grab_value not in range(1, max_remove + 1):
            try:
                grab_value = int(input("> "))
            except ValueError:
                print("Invalid selection. Must be an integer.")
                continue
            if grab_value <= 0:
                print("You have to take at at least 1 stick!")
            elif grab_value > max_remove:
                print("You can't take that many sticks!")
            elif grab_value > number_left:
                print("There aren't that many sticks left!")
            else:
                return number_left - grab_value
