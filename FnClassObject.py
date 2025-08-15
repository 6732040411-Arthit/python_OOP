# FnClassObject ฟังก์ชันออบเจกต์ (Function Object)
# ฟังก์ชั่นที่ทำงานร่วมกับ class และ object

# ininstance และ dir คือฟังก์ชั่นที่ทำงานร่วมกับ class และ object
# โดยมีรายละเอียด ดังนี้
# isinstance => เช็คว่า object นี้ถูกสร้าง class ที่เรานิยามหรือไม่
# dir => แสดง attribte และ methof
# __class__ => แสดงชื่อ class และ object

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self): # โชว์ข้อมูลจาก
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))


emp1 = Employee('อาทิตย์', 50000, 'วิชาการ')
emp2 = Employee('ติสันเทียะ', 25000, 'กิจการ')
emp3 = Employee('อาทิตย์ ติสันเทียะ', 10000, 'อาคาร')
emp4 = Employee('sun', 20000, 'HR')

print(isinstance(emp1, Employee)) # ตรวจสอบ ออบเจกต์ emp1 ถูกสร้างจาก class  ที่ตรวจสอบหรือไม่
print(dir(emp1)) # dir แสดง attribte(ตัวแปรที่เก็บข้อมูลของออบเจกต์) และ methof(ฟังก์ชันที่ใช้จัดการหรือดำเนินการกับข้อมูลในออบเจกต์)
print(dir(emp1.showData())) # เรียกแสดงเฉพาะ emp1 โดยเพิ่มคำสั่ง showdata
print(emp1.__class__) # เช็คออบเจกต์อยู่ในคลาสอะไร