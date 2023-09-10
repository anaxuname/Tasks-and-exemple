"""
Создать класс Task с названием и описанием.
Наследовать от него класс ToDoTask c булевым полем is_completed
"""

class Task:

    def __init__(self, name, description):
        self.name = name
        self.description = description


class ToDoTask(Task):

    def __init__(self, name, description, is_completed: bool = True) -> None:
        super().__init__(name, description)
        self.is_completed = is_completed
