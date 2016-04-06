import random


class AiGameLogic:

    def __init__(self, stick_count=20, max_amount_removable=3):
        self.stick_count = stick_count
        self.max_amount_removable = max_amount_removable

    def initialize_drawn_list(self, sticks_remaining):
        return [0] * sticks_remaining

    def initialize_choice_list(self, sticks_remaining, max_pick):
        choice_list = [list(range(1, max_pick + 1))] * sticks_remaining
        for index in range(max_pick):
            choice_list[index] = [list(range(1, index+2))]
        return choice_list

    def remove_sticks(self, sticks_remaining, max_pick, drawn_list, choice_list):
        #random.choice(list(range(1, self.max_amount_removable + 1))
        if sticks_remaining == 1:
            remove_value = 1
        elif sticks_remaining <= max_pick:
            remove_value = sticks_remaining - 1
        else:
            remove_value = random.choice(choice_list[sticks_remaining - 1])
        drawn_list[sticks_remaining - 1] = remove_value
        sticks_remaining -= remove_value
        print("... removing {} stick(s)... \n".format(remove_value))
        return sticks_remaining, drawn_list

    def remove_sticks_human(self, sticks_remaining, max_pick):
        grab_value = 0
        while grab_value not in range(1, max_pick + 1):
            try:
                grab_value = int(input("> "))
            except ValueError:
                print("Invalid selection. Must be an integer.")
                continue
            if grab_value <= 0:
                print("You have to take at at least 1 stick!")
            elif grab_value > max_pick:
                print("You can't take that many sticks!")
            elif grab_value > sticks_remaining:
                print("There aren't that many sticks left!")
            else:
                return sticks_remaining - grab_value

    def computer_game(self, computer_version):
        current_player = 'USER'
        sticks_remaining = self.stick_count
        max_pick = self.max_amount_removable
        drawn_list = self.initialize_drawn_list(sticks_remaining)
        choice_list = self.initialize_choice_list(sticks_remaining, max_pick)
        while sticks_remaining > 0:
            current_player = [value for value in ['USER', 'COMPUTER'] if value != current_player][0]
            print("Stick count = {}. {}\'s turn to choose.".format(sticks_remaining, current_player))
            if current_player == 'USER':
                sticks_remaining = self.remove_sticks_human(sticks_remaining, max_pick)
            else:
                if computer_version == 'easy':
                    sticks_remaining, drawn_list = self.remove_sticks(sticks_remaining, max_pick, drawn_list, choice_list)
                else:
                    sticks_remaining, drawn_list = self.remove_sticks(sticks_remaining, max_pick, drawn_list, choice_list)

        print("{} drew the last stick and lost the game!".format(current_player))
        if current_player == 'COMPUTER':
            for index, value in enumerate(drawn_list):
                if value > 0:
                    choice_list[index].remove(value)
        current_player = [value for value in ['USER', 'COMPUTER'] if value != current_player][0]
        print("{} wins!".format(current_player))
        if current_player == 'COMPUTER':
            for index, value in enumerate(drawn_list):
                if value > 0:
                    choice_list[index].append(value)
