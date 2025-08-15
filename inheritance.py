# สืบทอดคุณสมบัติ (inheritane)
# หลักการ inheritane คือ การทำสร้างสิ่งใหม่ขึ้นด้วยสืบทอดหรือรันเอา (inheritane)
# บางอย่างมาจากสิ่งเดิมที่มีอยู่แล้วโดยการสร้างเพิ่มเติมจากสิ่งที่มีอยู่แล้วได้เลบ

# ข้อดีของการ inheritane คือ จากการที่สามารถนำสิ่งที่เคยสร้างขึ้นแล้วกลับมาใช้ใหม่ (re=use) ได้
# ทำให้ช่วยประหยัดเวลาการทำงานลง เนื่องจากไม่ต้องเสียเวลาพัฒนาใหม่หมด

# Class -> ยกเว้น Private Attribute & Private method

# การสืบทอด
# คลาสแม่
# class Employee:

# คลาสลูก
# class Programmer(Employee):

class Employee:
    minSalary = 12000
    maxSalary = 50000
    companyName = 'บริษัท MAHATAI จำกัด'

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.__department = department


    def _showData(self):
        print('ชื่อพนักงาน = {}'+self.__name)
        print('เงินเดือน = {}'+self.__salary)
        print('แผนก = {}'+self.__department)

class Accounting(Employee):
    __departmantName = 'แผนกบัญชี'
    def __init__(self):
        pass

class Programmer(Employee):
    __departmantName = 'แผนกพัฒนาระบบ'
    def __init__(self):
        pass

class sale(Employee):
    __departmantName = 'แผนกขาย'
    def __init__(self):
        pass


account = Accounting()
print(account.companyName)
programmer = Programmer()
print(programmer.minSalary)
sale = sale()
print(sale.maxSalary)