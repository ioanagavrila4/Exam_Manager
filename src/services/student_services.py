from src.repository.repository import Repository
import random
class Service:
    def __init__(self):
        self.__data = Repository()

    def get_all_data(self):
        return self.__data.get_all_student()

    def add_student(self, student):
        self.__data.add_student_repo(student)

    def sort_student(self):
        student_array = self.__data.get_all_student()
        for pupil in range(0, len(student_array)):
            for pupil2 in range(pupil+1, len(student_array)):
                if student_array[pupil].grade > student_array[pupil2].grade:
                    aux = student_array[pupil]
                    student_array[pupil] = student_array[pupil2]
                    student_array[pupil2] = aux
        return student_array

    def add_bonuses(self, p, b):
        student_array = self.__data.get_all_student()
        for pupil in student_array:
            if pupil.attendace_count >= p:
                new_grade = pupil.grade + b
                self.__data.modify_student_grade(pupil.id, new_grade)

    def students_whose_name_include_a_string(self, string):
        student_array = self.__data.get_all_student()
        new_array = []
        for pupil in student_array:
            if string in pupil.name:
                new_array.append(pupil)
        if new_array is not None:
            for i in range(0, len(new_array)):
                for j in range(i+1, len(new_array)):
                    if new_array[i].name > new_array[j].name:
                        aux = new_array[i]
                        new_array[i] = new_array[j]
                        new_array[j] = aux
        return new_array
