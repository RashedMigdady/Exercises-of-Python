from functools import reduce


class Person:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getAddress(self):
        return self._address

    def setAddress(self, address):
        self._address = address

    def __del__(self):
        print(f'Student {self._name} has been deleted')


class Employee(Person):
    def __init__(self, employee_number, name, address, salary, job_title, loans):
        super().__init__(name, address)
        self.employee_number = employee_number
        self.__salary = salary
        self.__job_title = job_title
        self.__loans = loans

    def getSalary(self):
        return self.__salary

    def setSalary(self, salary):
        self.__salary = salary

    def getJobTitle(self):
        return self.__job_title

    def setJobTitle(self, job_title):
        self.__job_title = job_title

    def getTotalLoans(self):
        return sum(self.__loans)

    def getMaxLoans(self):
        if len(self.__loans) < 1:
            return None
        return max(self.__loans)

    def getMinLoans(self):
        if len(self.__loans) < 1:
            return None
        return min(self.__loans)

    def setLoans(self, loans):
        self.__loans = loans

    def getLoans(self):
        return self.__loans

    def printInfo(self):
        print(f'''
Name: {self._name}
Address: {self._address}
Employee Number: {self.employee_number}
Salary: {self.__salary}
Job Title: {self.__job_title}
Loans: {self.__loans}
        ''')

    def __del__(self):
        print(f'Employee: {self.employee_number} have been deleted')



class Student(Person):
    def __init__(self, student_number, name, address, subject, marks):
        super().__init__(name, address)
        self.student_number = student_number
        self.__subject = subject
        self.__marks = marks

    def getSubject(self):
        return self.__subject

    def setSubject(self, subject):
        self.__subject = subject

    def getMarks(self):
        return self.__marks

    def setMarks(self, marks):
        self.__marks = marks

    def getAverage(self):
        summation = 0
        length = 0

        for key, value in self.__marks.items():
            summation += value
            length += 1

        average = summation / length
        return average

    def getAllMarks(self):
        average = self.getAverage()

        if average >= 90:
            True
        else:
            return False
        # return list(filter(lambda x: x >= 90, self.__marks))

    def printInfo(self):
        print(f'''
Name: {self._name}
Address: {self._address}
Student nUmber: {self.student_number}
Subject: {self.__subject}
Marks: {self.__marks}
        ''')

    def __del__(self):
        print(f'Student: {self.student_number} I have been deleted')

print('-------------------------')

employee1 = Employee(1000, 'Ahamad Yazan', 'Amman, Jordan', 500, 'HR Consultant', [434, 200, 1020])
employee2 = Employee(2000, 'Hala Rana', 'Aqaba, Jordan', 750, 'Department Manager', [150, 3000, 250])
employee3 = Employee(3000, 'Mariam Ali', 'Mafraq, Jordan', 600, 'HR S Consultant', [304, 1000, 250, 3000, 5000, 235])
employee4 = Employee(4000, 'Yasmeen Mohammad', 'Karak, Jordan', 865, 'Director', [])

student1 = Student(20191000, 'Khalid Ali', 'Irbid, Jordan', 'History', {
    'english': 80,
    'arabic': 90,
    'art': 95,
    'management': 75
})
student2 = Student(20182000, 'Reem Hani', 'Zarqa, Jordan', 'Software Eng', {
    'english': 80,
    'arabic': 90,
    'management': 75,
    'calculus': 85,
    'os': 73,
    'programming': 90
})
student3 = Student(20161001, 'Nawras Abdulllah', 'Amman, Jordan', 'Arts', {
    'english': 83,
    'arabic': 92,
    'art': 90,
    'management': 70
})
student4 = Student(20172030, 'Amal Raed', 'Tafelah, Jordan', 'Computer Eng', {
    'english': 83,
    'arabic': 92,
    'art': 90,
    'management': 70,
    'calculus': 80,
    'os': 79,
    'programming': 91
})

    
# 1
EmployeesList = [employee1, employee2, employee3, employee4]

print('-------------------------')

# 2
StudentsList = [student1, student2, student3, student4]

print('-------------------------')

# 3 & 4
def len_list(lst_name, lst):
    print(lst_name + ' has ' + str(len(lst)) + ' Persons')


len_list('EmployeesList', EmployeesList)
len_list('StudentsList', StudentsList)

print('-------------------------')

# 5
for employee in EmployeesList:
    employee.printInfo()
    print('Total Loans: ', employee.getTotalLoans())
    print('\n\n')

print('-------------------------')

# 6
for student in StudentsList:
    student.printInfo()
    print('Average: ' + str(student.getAverage()))

print('-------------------------')

# 7
highest_student_average = 0

for student in StudentsList:
    if highest_student_average < student.getAverage():
        highest_student_average = student.getAverage()

print('Highest student average: ' + str(highest_student_average))

print('-------------------------')

# 8
employee_has_loans = list(filter(lambda e: e.getMinLoans(), EmployeesList))
min_employee_loan = min(list(map(lambda e: e.getMinLoans(), employee_has_loans)))
print('Employees\' Min Loans is: ' + str(min_employee_loan))

print('-------------------------')

# 9
max_employee_loan = max(list(map(lambda e: e.getMaxLoans(), employee_has_loans)))
print('Employees\' Max Loans is: ' + str(max_employee_loan))

print('-------------------------')

# 10
employees_loans = list(map(lambda e: e.getLoans(), employee_has_loans))
employees_total_loans = list(map(lambda e: e.getTotalLoans(), employee_has_loans))
print(f'''
Employees Loans: {employees_loans}
Employees Total Loans: {employees_total_loans}
''')

print('-------------------------')

# 11

LoanDictionary = list(map(lambda e: {e.employee_number: e.getLoans()}, employee_has_loans))
# print(LoanDictionary)
for item in LoanDictionary:
    print(item)

print('-------------------------')


# 12
def get_max_loan(employee_loans):
    max_loan = reduce(lambda a, b: a if a > b else b, employee_loans)
    return max_loan


def get_min_loan(employee_loans):
    min_loan = reduce(lambda a, b: a if a < b else b, employee_loans)
    return min_loan


for employee in employee_has_loans:
    print(
        f'Employee Name: {employee._name} Min Loan: {get_min_loan(employee.getLoans())} Max Loan: {get_max_loan(employee.getLoans())}')

print('-------------------------')

# 13
students_got_a = list(filter(lambda s: s.getAllMarks(), StudentsList))
for student in students_got_a:
    print(f'''
Name: {student.getName()}
Subject: {student.getSubject()}
Marks: {student.getMarks()}
''')

print('-------------------------')

# 14
employee_salaries = list(map(lambda e: e.getSalary(), EmployeesList))
max_employee_salary = max(employee_salaries)
print('Maximum Employee Salary', max_employee_salary)

print('-------------------------')

# 15
min_employee_salary = min(employee_salaries)
print('Minimum Employee Salary', min_employee_salary)

print('-------------------------')

# 16
total_salaries = reduce(lambda a, b: a + b, employee_salaries)
print('Total Employees Salaries ', total_salaries)

print('-------------------------')

# 17
def delete_object(lst_object):
    for item in lst_object:
        del item


delete_object(EmployeesList)
delete_object(StudentsList)

print('-------------------------')

# project 2

employees_list = []
students_list = []

from tkinter import * 


root = Tk()
root.title('menu_win')
def notdone():
    messagebox.showinfo('Note implemented', 'Not yet available')
top = Menu(root)
root.config(menu=top)

def open_about():
    messagebox.showinfo('About Us', 'Made by Moath Gharib & Rashed Mgdadi & Emad Alrashed')

# adding employees
def open_add():
    top = Toplevel(root)
    top.title('Add new employee')
    top.geometry('500x250+510+230')
    
    Label(top, text ='Name: ').grid(row = 0, column = 0)
    
    Label(top, text = 'Employee Number: ').grid(row = 1, column = 0)
    
    Label(top, text = 'Address: ').grid(row = 2, column = 0)
    
    Label(top, text = 'Salary: ').grid(row = 3, column = 0)
    
    Label(top, text = 'Job title: ').grid(row = 4, column = 0)
    
    Label(top, text = 'Loans ').grid(row = 5, column = 0)
    
    name_value = StringVar()
    emp_num_value = IntVar()
    address_value = StringVar()
    salary_value = IntVar()
    job_title_value = StringVar()
    loans_value = StringVar()
    
    name = Entry(top, textvariable = name_value).grid(row = 0, column = 1)
    emp_num = Entry(top, textvariable = emp_num_value).grid(row = 1, column = 1)
    address = Entry(top, textvariable = address_value).grid(row = 2, column = 1)
    salary = Entry(top, textvariable = salary_value).grid(row = 3, column = 1)
    job_title = Entry(top, textvariable = job_title_value).grid(row = 4, column = 1)
    loans = Entry(top, textvariable = loans_value).grid(row = 5, column = 1)
    
    
    def Pressed():
        employee = Employee(
                emp_num_value.get(), 
                name_value.get(), 
                address_value.get(), 
                salary_value.get(), 
                job_title_value.get(), 
                [200, 160, 50])
        
        employee.printInfo()
        employees_list.append(employee)

    submit = Button(top, text = "Submit", command = Pressed).grid(row = 6, column = 0)

# Viewing employees
def view_employee():
    top = Toplevel(root)
    top.title("View Employee")
    top.geometry("500x500+510+230")
    Label(top, text="View Employee").grid()
    x = 100
    y = 100
    for employee in employees_list:
        data = f"Name: {employee.getName()} \t" \
               f"Address: {employee.getAddress()} \t" \
               f"Number: {employee.employee_number} \t" \
               f"Title: {employee.getJobTitle()} \t" \
               f"Salary: {employee.getSalary()} \t" \
               f"Loans: {employee.getLoans()} \t" \
               f""
        Label(top, text=data).grid()
        y += 20
        
# Deleting Employees
def delete_employee():
    c = Toplevel(root)
    c.title("Delete Employee")
    c.geometry("500x500+510+230")
    Label(c, text="Delete Employee").grid()

    Label(c, text="Employee Number").place(x=20, y=20)
    employee_number_value = IntVar()
    
    def del_employee():
        global employees_list
        old_length = len(employees_list)
        employees_list = list(filter(lambda e: not e.employee_number == employee_number_value.get(), employees_list))
        new_length = len(employees_list)

        if not old_length == new_length:
            messagebox.showinfo('Success', f'Employee has been deleted, with number {employee_number_value.get()}')
        else:
            messagebox.showinfo('warning', 'There is not employee with the provided number')

    Entry(c, textvariable=employee_number_value).place(x=150, y=20)
    Button(c, text="Delete", command=del_employee).place(x=20, y=40)


# adding students
def add_student():
    c = Toplevel(root)
    c.title("Add New Student")
    c.geometry("500x500+510+230")
    Label(c, text="Add New Student").grid()
    
    Label(c, text = 'Student Number').grid(row = 0, column = 0)
    Label(c, text = 'Name').grid(row = 1, column = 0)
    Label(c, text = 'Address').grid(row = 2, column = 0)
    Label(c, text = 'Subject').grid(row = 3, column = 0)
    Label(c, text = 'Mark').grid(row = 4, column = 0)
    
    student_number_value = IntVar()
    name_value = StringVar()
    address_value = StringVar()
    subject_value = StringVar()
    marks_value = IntVar()
    
    student_number = Entry(c, textvariable = student_number_value).grid(row = 0, column = 1)
    name = Entry(c, textvariable = name_value).grid(row = 1, column = 1)
    address = Entry(c, textvariable = address_value).grid(row = 2, column = 1)
    subject = Entry(c, textvariable = subject_value).grid(row = 3, column = 1)
    marks = Entry(c, textvariable = marks_value).grid(row = 4, column = 1)
    
    # saving students
    def save_student():
        student = Student(
                student_number_value.get(),
                name_value.get(),
                address_value.get(),
                subject_value.get(),
                marks_value.get())
        student.printInfo()
        students_list.append(student)
        
    button = Button(c, text = 'Submit', command = save_student).grid(row = 5, column = 0)

# viewing students
def view_student():
    c = Toplevel(root)
    c.title("View Student")
    c.geometry("500x500+510+230")
    Label(c, text="View Student").grid()
    
    x = 100
    y = 100
    
    for student in students_list:
        data = f"Name: {student.getName()} \t" \
               f"Address: {student.getAddress()} \t" \
               f"Number: {student.student_number} \t" \
               f"Subject: {student.getSubject()} \t" \
               f"Marks: {student.getMarks()} \t" \
               f""
        Label(c, text=data).grid()
        y += 20


# Deleting student    
def delete_student():
    c = Toplevel(root)
    c.title("Delete Student")
    c.geometry("500x500+510+230")
    Label(c, text="Delete Student").grid()

    Label(c, text="Student Number").place(x=20, y=20)
    student_number_value = IntVar()

    def del_student():
        global students_list
        old_length = len(students_list)
        students_list = list(filter(lambda e: not e.student_number == student_number_value.get(), students_list))
        new_length = len(students_list)

        if not old_length == new_length:
            messagebox.showinfo('Success', f'Student with number "{student_number_value.get()}" has been deleted')
        else:
            messagebox.showinfo('Warning', 'There is not student with the provided number')

    Entry(c, textvariable=student_number_value).place(x=150, y=20)
    Button(c, text="Delete", command=del_student).place(x=20, y=40)

file = Menu(top, tearoff=0)
file.add_command(label="Report", command=notdone)
file.add_separator()
file.add_command(label="Exit", command=root.destroy)
top.add_cascade(label="File", menu=file)

employee = Menu(top, tearoff=0)
employee.add_command(label='Add', command=open_add)
employee.add_command(label="View", command=view_employee)
employee.add_command(label="Delete", command=delete_employee)
top.add_cascade(label="Employees", menu=employee)

student = Menu(top, tearoff=0)
student.add_command(label='Add', command=add_student)
student.add_command(label="View", command=view_student)
student.add_command(label="Delete", command=delete_student)
top.add_cascade(label="Student", menu=student)

help_ = Menu(top, tearoff=0)
help_.add_command(label='About', command=open_about)
top.add_cascade(label="Help", menu=help_)

root.mainloop()