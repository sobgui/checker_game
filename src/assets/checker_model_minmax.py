import random


class CheckerModelRandom:
    def __init__(self):
        pass

    def move_piece(self,checker_model):
        selected_piece_position, move_position = self.get_random_move(checker_model)
        checker_model.move_piece(selected_piece_position, move_position)

    def get_random_move(self, checker_model):
        selected_piece_position = random.choice(list(checker_model.dict_of_possible_moves.keys()))
        move = random.choice(checker_model.dict_of_possible_moves[selected_piece_position])
        move_position = move.get_final_position()
        return selected_piece_position, move_position
