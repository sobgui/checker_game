import tqdm

import checker_model
import checker_model_ai


class BenchmarkAI:
    def __init__(self, players=None, number_of_test=50, checker_grid=None):
        if players is None:
            players = [
                ["random", {}],
                ["minmax", {"depth": 3, "to_maximize": False}]
            ]

        self.players = players
        self.number_of_test = number_of_test

    def play_game(self):
        wins_player_1 = 0
        wins_player_2 = 0
        players = self.players
        if len(players) == 2:
            for _ in tqdm.tqdm(range(self.number_of_test)):
                piece_model = checker_model.CheckerModel()
                ai_model = checker_model_ai.CheckerModelAI()

                while True:
                    ai_model.move_piece(piece_model, players[0][0], **players[0][1])
                    game_state = piece_model.check_game_state()
                    if game_state == "draw_game":
                        break

                    elif game_state == 1:
                        wins_player_1 += 1
                        break

                    ai_model.move_piece(piece_model, players[1][0], **players[1][1])
                    game_state = piece_model.check_game_state()
                    if game_state == "draw_game":
                        break

                    elif game_state == -1:
                        wins_player_2 += 1
                        break

            print(f"Player 1:{players[0][0]}  wins {wins_player_1}")
            print(f"Player 2:{players[1][0]}  wins {wins_player_2}")
            print(f"Draws: {self.number_of_test - wins_player_1 - wins_player_2}")
        else:
            print(f" We should only have 2 Players!")


benchmark_ai = BenchmarkAI(
    [
        ["mtc", {"depth": 3, "to_maximize": True, "nb_of_iterations": 5}],
        ["mtc", {"depth": 3, "to_maximize": False, "nb_of_iterations": 5}],


    ],
    number_of_test=100)
benchmark_ai.play_game()

# ["mtc", {"depth": 3, "to_maximize": True, "nb_of_iterations": 10}],
