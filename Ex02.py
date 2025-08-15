# เขียนโปรแกรมสร้าง class ชื่อ people โดยมี attribute และ Method ดังนี้
# attribute
# name เป็นชื่อของบุคคล
# age เป็นอายุของบุคคล
# method
# Introduce() เมื่อเรียกใช้จะพิมพ์ข้อความ my name is <name>. I'm <age> year old
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("My name is {}. I'm {} years old.".format(self.name, self.age))
person = People("อาทิตย์", 22)
person.introduce()