class SimpleComputerGameLogic:


    def __init__(self, stick_count=20, max_amount_removable=3):
        self.stick_count = stick_count
        self.max_amount_removable = max_amount_removable

    def easy_computer_game(self):
        current_player = 'USER'
        while self.stick_count > 0:
            current_player = [value for value in ['USER', 'COMPUTER'] if value != current_player][0]
            print("Stick count = {}. {}\'s turn to choose.".format(self.stick_count, current_player))
            if current_player == 'USER':
                self.stick_count = self.remove_sticks_human(self.stick_count, self.max_amount_removable)
            else:
                self.stick_count = self.remove_sticks_computer(self.stick_count, self.max_amount_removable)
        print("{} drew the last stick and lost the game!".format(current_player))
        current_player = [value for value in ['USER', 'COMPUTER'] if value != current_player][0]
        print("{} wins!".format(current_player))

    def remove_sticks_computer(self, number_left, max_remove):
        if number_left == 1:
            print("... removing 1 stick... \n")
            return 0
        elif number_left <= (max_remove + 1):
            print("... removing {} sticks... \n".format(number_left-1))
            return 1
        elif number_left % (max_remove + 1) != 0:
            print("... removing {} sticks... \n".format(number_left % (max_remove + 1)))
            return number_left - number_left % (max_remove + 1)
        else:
            print("... removing 1 stick... \n")
            return number_left - 1

    def remove_sticks_human(self, number_left, max_remove):
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
