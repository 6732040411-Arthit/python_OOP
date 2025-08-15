# constructor เป็นคำสั่งการสร้าง โดยสั่งฟังค์ชั้น def__init__(self):
# เป็น Method พิเศษที่จะถ฿กใช้งานเมื่อตอนเริ่มสร้างัตถุ (ไม่ระบุก็ได้)
# โครงสร้าง comstructor
# def __init__(self):
#     pass

# destructor เป็นตำสั่งทำลาย โดยสั่งฟังค์ชั้น def __def__(self):
# เป็น method พิเศษที่ตรงข้ามกับ constructor จะถูกใช้งาน
# เมื่อเราสิ้นสุดการทำงานของ class หรือถูกทำก่อนจะสลาย object
# ส่วนใหญ่จะเป็นกลุ่มคำสั่งที่ทำหน้าที่คืนหน่วยความจำให้ระบบ (ไม่ระบุก็ได้)
# โคร้างสร้าง destructor
# def __def__(self):
#     pass

# การสร้าง constructor

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self): # โชว์ข้อมูลจาก
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))

    # มีหรือไม่มีก็ได้ destructor
    def __del__(self):
        print('call destructor')

emp1 = Employee('อาทิตย์', 50000, 'วิชาการ')
emp1.showData()

emp2 = Employee('ติสันเทียะ', 25000, 'กิจการ')
emp2.showData()

emp3 = Employee('อาทิตย์ ติสันเทียะ', 10000, 'อาคาร')
emp3.showData()

emp4 = Employee('sun', 20000, 'HR')
emp4.salary = 21000 # ตัวแปรที่เก็บข้อมูลเกี่ยวกับเงินเดือนของพนักงานหรือค่าตอบแทน (ใช้ในการแก้ไขจากค่าเดิม)
emp4.showData()


