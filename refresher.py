"""
Object Oriented Programming
"""
# - เราสร้าง ทุกอย่างให้อยู่ในรูปแบบ Object เพื่อที่จะสามารถ reuse ได้
# - ใน python เราใช้คำสั่ง class ในการสร้าง Object
# - แสดงให้เห็นว่า เรียกใช้ class Student เหมือนกัน แต่เป็นคนละอันกันใน memory(คนละจุด)


# - วิธีการ สร้าง class เพื่อ reuse

# - class สามารถมี function ได้ เราจะเพิ่ม function fullname_with_major

# - class variable
# - class variable 2

class Student:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def greetings(self):
        return f"Hello! I am {self.first_name} {self.last_name}"
    
class UniversityStudent(Student):
    def __init__(self, first_name, last_name, major):
        super().__init__(first_name, last_name)
        self.major = major
        
    def greetings(self):
        # return f"{super().greetings()} , my major is {self.major}"
        return f"Hello! I am {self.first_name} currently study {self.major}"
        
class VocationalStudent(Student):
    def __init__(self, first_name, last_name, future_adult_job):
        super().__init__(first_name, last_name)
        self.future_adult_job = future_adult_job
        
    def graduated(self):
        return f"When I graduated, I want to be a {self.future_adult_job}"
    

university_student = UniversityStudent("tochsaporn", "petchpol", "Computer Engineering")
vocation_student = VocationalStudent("katsamapol", "petchpol", "Programmer")

print(university_student.greetings())
print(vocation_student.graduated())





