class Employee:
    def __init__(self, name, salary, department):
        # Protected attributes
        self._name = name
        self._salary = salary
        self._department = department

    # Protected method
    def _showData(self):
        print(f'ชื่อพนักงาน = {self._name}')
        print(f'เงินเดือน = {self._salary}')
        print(f'แผนก = {self._department}')

    # Setter method เพื่อแก้ไข salary อย่างปลอดภัย
    def setSalary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("กรุณากรอกเงินเดือนที่ถูกต้อง!")


emp1 = Employee('อาทิตย์', 50000, 'วิชาการ') # สร้างออบเจกต์พนักงาน
emp1.setSalary(51000) # ใช้ Setter Method แทนการแก้ไขโดยตรง
emp1._showData() # เรียกใช้ Protected Method
