class Student:
    def __init__(self, id, name, attendace_count, grade):
        self.id = id
        self.name = name
        self.attendace_count = attendace_count
        self.grade = grade

    def __str__(self):
        return f"{self.id} {self.name} {self.attendace_count} {self.grade}"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        return self.id == other.id
    def id(self):
        return self.id
    def name(self):
        return self.name
    def attendace_count(self):
        return self.attendace_count
    def group(self):
        return self.group
