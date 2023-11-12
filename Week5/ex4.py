import datetime

class Employee:
    def __init__(self, name, years_of_experience):
        if years_of_experience < 0:
            raise ValueError("years_of_experience cannot be negative")
        self.name = name
        self.salary = self.get_base_salary() + years_of_experience * 1000
        self.years_of_experience = years_of_experience
        self.performance_reviews = []
    
    def increase_salary(self, amount):
        if amount < 0:
            raise ValueError("amount cannot be negative")
        self.salary += amount
    def get_base_salary(self):
        return 3000
    
    def add_performance_review(self,manager, review, date):
        if not isinstance(manager, Manager):
            raise ValueError("manager must be of type Manager")
        self.performance_reviews.append(( manager,review, date))

    def print_performance_reviews(self):
        print ("Performance reviews for "+self.name, end=": ")
        for review in self.performance_reviews:
            print("Review from " +review[0].name+" - "+review[1]+" - "+str(review[2]))

    def __str__(self):
        return "Employee: "+self.name+" with salary "+str(self.salary)
    

class Manager(Employee):
    def __init__(self, name, years_of_experience, department):
        self.managed_employees = []
        self.department = department
        super().__init__(name, years_of_experience)

    def add_managed_employee(self, employee):
        if not isinstance(employee, Employee):
            raise ValueError("employee must be of type Employee")
        if employee == self:
            raise ValueError("cannot manage self")
        self.managed_employees.append(employee)

    def remove_managed_employee(self, employee):
        if not isinstance(employee, Employee):
            raise ValueError("employee must be of type Employee")
        self.managed_employees.remove(employee)   
    
    def get_num_of_managed_employees(self):
        return len(self.managed_employees)
    
    def write_performance_review(self, employee, review):
        if not isinstance(employee, Employee):
            raise ValueError("employee must be of type Employee")
        if employee not in self.managed_employees:
            raise ValueError("employee is not managed by this manager")
        employee.add_performance_review(self, review, datetime.datetime.now() )

    def get_base_salary(self):
        return 15000
    
class Engineer(Employee):
    def __init__(self, name, years_of_experience, specialization):
        super().__init__(name, years_of_experience)
        self.specialization = specialization
        self.tools = []

    def add_tool(self, tool):
        self.tools.append(tool)
    def remove_tool(self, tool):
        self.tools.remove(tool)
    def get_tools(self):
        return self.tools
    def get_base_salary(self):
        return 5000

class SalesPerson(Employee):
    def __init__(self, name, years_of_experience):
        super().__init__(name, years_of_experience)
        self.profit_brought = 0
        self.sales = []
    def make_sale(self, sale, project):
        if sale < 0:
            raise ValueError("sale amount cannot be negative")
        self.profit_brought += sale
        self.sales.append((project, sale))
        self.increase_salary(self.bonus_for_sale(sale))
    def bonus_for_sale(self,sale):
        return sale * 0.01
    def print_sales(self):
        for sale in self.sales:
            print("Sale of "+str(sale[1])+" for project "+sale[0])
    def get_base_salary(self):
        return 6000

try:
    emp1 = Employee("John", 5)
    emp2 = Employee("Bob", 3)

    manager = Manager("Alice", 10, "IT")
    manager.add_managed_employee(emp1)
    manager.add_managed_employee(emp2)

    manager.write_performance_review(emp1, "Good job")
    manager.write_performance_review(emp2, "Bad job")

    eng = Engineer("Jack", 2, "Python")
    eng.add_tool("PyCharm")
    eng.add_tool("VsCode")
    #print(eng.get_tools())

    manager.add_managed_employee(eng)
    manager.write_performance_review(eng, "Skipped work without announcing") 
    eng.print_performance_reviews()

    sales = SalesPerson("Mary", 1)
    sales.make_sale(1000, "Project 1")
    sales.make_sale(2000, "Project 2")
    sales.print_sales()
    print(sales)
   
    print(manager)
except ValueError as e:
    print(e)
