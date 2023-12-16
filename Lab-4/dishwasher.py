class Dishwasher:
    def __init__(self, water, program_count, model, dishes_count) -> None:
        self.__water = water
        self.__program_count = program_count
        self.model = model
        self.dishes_count = dishes_count

    def get_water(self):
        return self.__water

    def get_program_count(self):
        return self.__program_count

    def get_model(self):
        return self.model

    def get_dishes_count(self):
        return self.dishes_count

    def __str__(self):
        return f"{self.__water}, {self.__program_count}, {self.model}, {self.dishes_count}"

    def __repr__(self):
        return f"{self.__water}, {self.__program_count}, {self.model}, {self.dishes_count}"

    def __del__(self):
        print("destructor is called")

