class Employee:
    def __init__(self, name, salary, department):
        # public attribute
        self.name = name
        self.salary = salary
        self.department = department


# public method
    def showData(self): # โชว์ข้อมูลจาก
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))


emp1 = Employee('อาทิตย์', 50000, 'วิชาการ')
emp1.salary = 51000  # เปลี่ยนค่า salary โดยตรง
print(emp1.salary)  # แสดงหลังเปลี่ยนค่า salary 51000