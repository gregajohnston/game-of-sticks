class HumanGameLogic:

    def __init__(self, stick_count=20, max_amount_removable=3):
        self.stick_count = stick_count
        self.max_amount_removable = max_amount_removable

    def multi_player_game(self):
        current_player = 1
        while self.stick_count > 0:
            print("Stick count = {}. Player {}\'s turn to choose.".format(self.stick_count, current_player))
            self.stick_count = remove_sticks(self.stick_count, self.max_amount_removable)
        print("Player {} drew the last stick and lost the game!".format(current_player))
        current_player = [value for value in [1, 2] if value != current_player][0]
        print("Player {} wins!".format(current_player))

    def remove_sticks(number, max_number):
        while True:
            try:
                value = int(input("> "))
            except TypeError:
                print("Invalid selection. Must be an integer.")
                continue
            if value > max_number:
                raise ValueError("Cannot select more than {} sticks.".format(max_number))
                continue
            if value > number:
                raise ValueError("Number must be lower than remaining stick count.")
                continue
        return number - value
