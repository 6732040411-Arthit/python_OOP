# AccessModifier
# คือระดับในการเข้าถึง class attribute method และอื่นๆ ในภาษาเชิงวัตถุ
# โดยมีประโยชน์อย่างมากในเรื่องของการกำหนดระดับการเข้าถึง
# สิทธิในการเข้าใช้งาน การซ้อนข้อมูล และอื่นๆ

# public คือ การประกาศเข้าถึงที่เข้มงวดน้อยที่สุด หรือกล่าวได้ว่าใคร ๆ
# ก็สามารถเข้าถึงและเรียกใช้งานได้ ไม่มี _ เป็น public

# protected(_) เป็นการประกาศระดับการเข้าถึงเฉพาะคลาสของตัวมันเองและคลาสลูก
# ที่สืบทอดคุณสมบัติไปใช้เท่านั้น มี _ 1 ตัวเป็น protected

# Private(_) เป็นการประกาศระดับการเข้าถึงที่เข้มงวดที่สุด กล่าวคือ จะมีแต่คลาสของ
# ตัวมันเองเท่านั้นที่มีสิทธ์ใช้งานได้ มี__ 2 ตัวเป็น Private

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


emp1 = Employee('ชิน', 50000, 'วิชาการ')
emp1.salary = 51000
emp1.showData()