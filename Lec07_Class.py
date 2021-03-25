##################################################################
# 클래스의 이해 - SchoolMember
##################################################################
class SchoolMember:
    """학교의 멤버를 표현하는 클래스"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_info(self):
        """인적정보를 출력"""
        print('Name: {}, Age: {}'.format(self.name, self.age))

"""
if __name__ == '__main__':
    print(SchoolMember.__doc__)
    I = SchoolMember('김현용', 49)
    print(I)
    print(I.name)
    print(I.age)
    print(SchoolMember.say_info.__doc__)
    I.say_info()
"""
##################################################################
# 클래스의 이해 - 상속
##################################################################


class Teacher(SchoolMember):
    """선생님 클래스"""

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        # SchoolMember.__init__(self, name, age)
        self.salary = salary

    def say_salary(self):
        """급여를 출력"""
        print('Salary: {}'.format(self.salary))

"""
if __name__ == '__main__':
    print(Teacher.__doc__)
    I = Teacher('김현용', 49, 500)
    print(Teacher.__bases__)
    print(I.__class__)

    # 속성
    print(I.name)
    print(I.age)
    print(I.salary)

    # 메서드
    I.say_info()
    I.say_salary()
"""
##################################################################
# 클래스의 이해 - 상속
##################################################################


class Student(SchoolMember):
    """학생 클래스"""

    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def say_marks(self):
        """학점을 출력"""
        print('Marks: {}'.format(self.marks))


if __name__ == '__main__':
    print(Student.__doc__)
    I = Student('김현용', 49, 4.3)
    print(Student.__bases__)
    print(I.__class__)

    # 속성
    print(I.name)
    print(I.age)
    print(I.marks)

    # 메서드
    I.say_info()
    I.say_marks()

