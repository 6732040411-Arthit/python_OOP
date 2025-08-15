# getter / setter method
# setter การกำหนดค่าให้ object
# getter การดึงค่าจาก object

# Ex_Setter
    # def setName(self, newname):
    #   self.__name = newname
# Ex_Getter
    # def getName(self):
    #   return self.__name

# getter / setter method
# setter การกำหนดค่าให้ object
# getter การดึงค่าจาก object

# Ex_Setter
    # def setName(self, newname):
    #   self.__name = newname
# Ex_Getter
    # def getName(self):
    #   return self.__name

class Employee:
    def __init__(self, name, salary, department):
        # private attribute
        self.__name = name
        self.__salary = salary
        self.__department = department

    # public method
    def _showData(self):
        print('ชื่อพนักงาน = {}'+self.getname())
        print('เงินเดือน = {}'+self.getsalary())
        print('แผนก = {}'+self.getdepartment())

    #setter method
    def setname(self, newname):
        self.__name = newname
    def setSalary(self, newsalary):
        self.__salary = newsalary
    def setDepartment(self, newdepartment):
        self.__department = newdepartment

    # getter method
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getDepartment(self):
        return self.__department

emp1 = Employee('อาทิตย์', 50000, 'วิชาการ')
print('พนักงานดีเด่นประจำปี = {}'.format(emp1.getName()))
print('เงินเดือน = {}'.format(emp1.getSalary()))
print('แผนก = {}'.format(emp1.getDepartment()))