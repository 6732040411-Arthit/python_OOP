# เขียนโปรแกรมสร้าง class ชื่อ Human โดยมี attribute และ Method ดังนี้
# attribute
# name เป็นชื่อของบุคคล
# age เป็นอายุของบุคคล
# method
#     aging(year) รับ parameter 1 ตัว คือ year
#     แสดงอายุปัจจุบัน

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def aging(self, year):
        print("อายุเดิม: {} ปี".format(self.age))
        self.age += year
        print("หลังจากผ่านไป {} ปี".format(year))
        print("อายุปัจจุบัน: {} ปี".format(self.age))
    def show_info(self):
        print("ชื่อ: {} อายุ: {} ปี".format(self.name, self.age))


person = Human("อาทิตย์ ติสันเทียะ", 21)
person.show_info()
person.aging(1)
person.show_info()