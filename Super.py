# Super
# เมื่อต้องการเรียนใช้งานคุณสมบัติต่าง ๆ ในคลาสแม่
# เช่น constructor, Method, Attribute

# super().__init__(name)



class Employee:
    minSalary = 12000
    maxSalary = 50000
    companyName = 'บริษัท MAHATAI จำกัด'

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.__department = department

    def showData(self):
        print('ชื่อพนักงาน = '+self.__name)
        print('เงินเดือน = ', format(self.__salary)) #  ถ้าไม่อยากใช้ format ใช้ str คำสั่ง +str
        print('แผนก = '+self.__department)


class Accounting(Employee):
    __departmentName = 'แผนกบัญชี'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super().showData()

class Programmer(Employee):
    __departmentName = 'แผนกพัฒนาระบบ'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super().showData()

class Sale(Employee):
    __departmentName = 'แผนกขาย'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super().showData()


account = Accounting('อาทิตย์01', 35000)
programmer = Programmer('อาทิตย์02', 50000)
sale = Sale('อาทิตย์03', 25000)