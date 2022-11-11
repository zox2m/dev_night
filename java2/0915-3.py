class Person:
    def greeting(self):
        print('안녕하세요?')


class Student(Person):
    def greeting(self):
        super().greeting()
        print('저는 서주민입니다')
