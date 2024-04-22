import checker_model_random, checker_model_minmax, checker_model_mtc


class CheckerModelAI:
    def __init__(self):
        pass

    def move_piece(self, checker_model, ai="random", **params):
        if params is None:
            params = {}
        ai_model = None
        if ai == "random":
            ai_model = checker_model_random.CheckerModelRandom()
        if ai == "minmax":
            ai_model = checker_model_minmax.CheckerModelMinMax()
        if ai == "mtc":
            ai_model = checker_model_mtc.CheckerModelMTC()

        ai_model.move_piece(checker_model, **params)
