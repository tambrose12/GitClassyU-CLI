from .gradebook import Gradebook


class Course:
    def __init__(self, name, level, credits):
        self.name = name
        self.level = level
        self.credits = credits
