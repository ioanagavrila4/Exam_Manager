from src.domain.student import Student
import os
class Repository():
    def __init__(self):
        self.__all_student = []
        self.get_from_text_file_repo()
    def get_all_student(self):
        return self.__all_student
    def add_student_repo(self, student):
        self.__all_student.append(student)
        file_path = os.path.join(os.path.dirname(__file__), "student.txt")
        with open(file_path, "a") as file:
            file.write(f"{student.id},{student.name},{student.attendace_count},{student.grade}\n")
    def add_student_on_list(self, student):
        self.__all_student.append(student)
    def modify_student_grade(self, student_id, new_grade):
        for student in self.__all_student:
            if student.id == student_id:
                student.grade = new_grade
                break
        file_path = os.path.join(os.path.dirname(__file__), "student.txt")
        with open(file_path, "w") as file:
            for student in self.__all_student:
                file.write(f"{student.id},{student.name},{student.attendace_count},{student.grade}\n")
    def get_from_text_file_repo(self):
        file_path = os.path.join(os.path.dirname(__file__), "student.txt")
        with open(file_path, "r") as file:
            rows = file.readlines()
        for row in rows:
            (id, name, attendace_count, grade) = [item.strip() for item in row.split(",")]
            self.add_student_on_list(Student(int(id), name, int(attendace_count), int(grade)))