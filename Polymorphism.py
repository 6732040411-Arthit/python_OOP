# Polymorphism
# การพร้องรูป
# เกิดจาก poly หลากหลาย morphology รูปแบบ
# ในทางโปรแกรม คือการที่ mrthod ชื่อเดียวกัน 
# สามารถรับอาร์กิวเมนต์ที่แตกต่างกันได้หลายรูปแบบ
# โดย method นี้จะถูกเรียกว่า oveload method

# Overloading
class Employee:
    minSalary = 12000
    maxSalary = 50000
    companyName = "บริษัท XYZ จำกัด"

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.__department = department

    # แสดงรายละเอียด
    def _showData(self):
        print("ชื่อพนักงาน = " + self.__name)
        print("เงินเดือน = " + str(self.__salary))
        print("แผนก = " + self.__department)

    # รายได้ต่อปี
    def _getIncome(self):
        return self.__salary * 12

    def __str__(self):
        return "ชื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {} , รายได้ต่อปี = {}".format(
            self.__name, self.__department, self.__salary, self._getIncome()
        )


class Accounting(Employee):
    __departmentName = "แผนกบัญชี"

    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        self.__age = age

    def _showData(self):
        super()._showData()
        print("อายุ = " + str(self.__age))


class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"

    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__departmentName)
        self.__experience = experience
        self.__skill = skill

    def _showData(self):
        super()._showData()
        print("ประสบการณ์ = " + str(self.__experience) + " ปี")
        print("ทักษะ = " + self.__skill)


class Sale(Employee):
    __departmentName = "แผนกขาย"

    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)
        self.__area = area

    def _showData(self):
        super()._showData()
        print("พื้นที่รับผิดชอบ = " + self.__area)


print("ข้อมูลพนักงานแผนกบัญชี")
account = Accounting("อาทิตย์", 35000, 35)
account._showData()
print("ข้อมูลพนักงานแผนกพัฒนาระบบ")
programmer = Programmer("ซัน", 50000, 2, "พัฒนาเกม")
programmer._showData()
print("ข้อมูลพนักงานแผนกขาย")
sale = Sale("หนึ่ง", 25000, "เชียงคาน")
sale._showData()