class Drive:
    def __init__(self, HP, generated_money):
        self.HP = HP
        self.generated_money = generated_money

    def drive_A(self):
        self.HP = self.HP - 10
        self.generated_money = self.generated_money + 10

    def care(self):
        self.HP = self.HP + 10
        self.generated_money = self.generated_money - 10

    def report(self):
        print(f"HP = {self.HP}, generated money = {self.generated_money}")


drive_A = Drive(100, 100)
drive_A.drive_A()
drive_A.report()
drive_A.care()
drive_A.report()
print("")