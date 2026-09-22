
class MLModel:

    def __init__(self, name, algorithm):
        self.name = name
        self.algorithm = algorithm

    def show_info(self):
        print("Model:", self.name)
        print("Algorithm:", self.algorithm)
   