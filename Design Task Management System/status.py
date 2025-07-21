from enum import Enum

class Status(Enum):
    TODO = 1
    IN_PROGRESS = 2
    DONE = 3

    def __str__(self):
        return self.value