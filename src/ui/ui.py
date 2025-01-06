from src.domain.student import Student
from src.services.student_services import Service
import random
class UI:
    def __init__(self):
        self.__service = Service()
    def print_student(self, students):
        new_array = self.__service.sort_student()
        print(new_array)
    def add_student(self, id, name, attendance, grade):
        new_array = self.__service.get_all_data()
        for student in new_array:
            if student.id == id:
                raise ValueError("Student already exists!")
        if grade < 1 or grade > 10:
            raise ValueError("Grade must be between 1 and 10!")
        words = name.split(" ")
        count = 0
        for word in words:
            count = count + 1
        if count < 2:
            raise ValueError("Name must have at least 2 words!")
        self.__service.add_student(Student(id, name, attendance, grade))

    def add_bonus(self, p, b):
        self.__service.add_bonuses(p, b)

    def students_whose_name_include_a_string(self, string):
        new_array = self.__service.students_whose_name_include_a_string(string)
        print(new_array)
    def menu(self):
        print("Hello! This is an application for managing an exam!")
        while True:
            print("1. Add student")
            print("2. Display all students in decreasing order of their grade: ")
            print("3. Add bonuses to students with attendance greater than a given number: ")
            print("4. Display all students whose name includes a given string: ")
            print("5. Exit")
            command = int(input("Enter command: "))
            if command == 1:
                id = int(input("Enter student id: "))
                name = input("Enter student name: ")
                attendance = int(input("Enter student attendance: "))
                grade = int(input("Enter student grade: "))
                try:
                    self.add_student(id, name, attendance, grade)
                except ValueError as ve:
                    print(ve)
            elif command == 2:
                new_array = self.__service.get_all_data()
                self.print_student(new_array)
            elif command == 3:
                p = int(input("Enter the attendance number: "))
                b = int(input("Enter the bonus: "))
                self.add_bonus(p, b)
            elif command == 4:
                string = input("Enter the string: ")
                self.students_whose_name_include_a_string(string)
            elif command == 5:
                break
    