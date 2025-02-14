# 某公司有三种类型的员工，分别是部门经理、程序员和销售员
# 需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪
# 部门经理的月薪是固定15000元
# 程序员按工作时间（以小时为单位）支付月薪，每小时200元
# 销售员的月薪由1800元底薪加上销售额5%的提成两部分构成。
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def salary_display(self):
        print(f'{self.name}(工号：{self.id})的工资为：{self.salary}')

class Manager(Employee):
    def __init__(self,name,id,monthly_salary):
        super().__init__(name,id)
        self.monthly_salary = monthly_salary
        self.salary = monthly_salary

class Programmer(Employee):
    def __init__(self,name,id,work_hours):
        super().__init__(name,id)
        self.work_hours =work_hours
        self.salary = work_hours * 200

class Salesperson(Employee):
    def __init__(self,name,id,sales):
        super().__init__(name,id)
        self.sales = sales
        self.salary = 1800 + sales * 0.05

manager1 = Manager('小陈','022002','8000')
manager1.salary_display()

programmer1 = Programmer('小延','022003',40)
programmer1.salary_display()

salesperson1 = Salesperson('小金','022004',80000)
salesperson1.salary_display()