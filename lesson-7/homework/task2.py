import sys
import os


class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

    def to_file_format(self):
        return f"{self.emp_id},{self.name},{self.position},{self.salary}\n"

    @staticmethod
    def from_file_format(line):
        parts = line.strip().split(',')
        if len(parts) == 4:
            return Employee(parts[0], parts[1], parts[2], parts[3])
        return 
    



class EmployeeManager:
    File="lesson-6/homework/employees.txt"

    @staticmethod
    def add_employee():
            emp_id=input("Enter ID:")
            name=input("Enter a name:")
            position=input("Enter a position")
            salary=input("Enter a salary")
            emp=Employee(emp_id, name, position, salary)

            with open(EmployeeManager.File, mode='a') as file:
                file.write(emp.to_file_format())
            
            print("Employee added!") 


    @staticmethod
    def view_all():
        if not os.path.exists(EmployeeManager.File):
            print("Employee not found")
            return
        
        with open(EmployeeManager.File, mode= 'r') as file:
            print('\n ALL Employees: ')
            for line in file:
                emp=Employee.from_file_format(line)
                if emp:
                    print(emp)
    
    
    @staticmethod            
    def search_emp(emp_id):
        with open(EmployeeManager.File, mode='r') as file:
            for line in file:
                emp=Employee.from_file_format(line)
                if emp and emp.emp_id==emp_id:
                    print(emp)
                else:
                    print("Employee not found")
    @staticmethod    
    def update(emp_id):
        updated=False
        updated_lines=[]
        with open(EmployeeManager.File, mode='r') as file:
            for line in file:
                emp=Employee.from_file_format(line)
                if emp and emp.emp_id==emp_id:
                    print("employee found.Enter new details: ")
                    name=input("Enter a name:")
                    position=input("Enter a position")
                    salary=input("Enter salary")
                    updated_lines.append(emp.to_file_format())
                    updated=True
                else:
                    updated_lines.append(line)    

        with open(EmployeeManager.File, mode='w') as file:
            file.writelines(updated_lines)
            print("Successfully updated")

                
    @staticmethod
    def delete_employee(emp_id):
        deleted=False
        remainig_lines=[]
        with open(EmployeeManager.File, mode='r') as file:
            for line in file :
                emp=Employee.from_file_format(line)
                if emp and emp.emp_id== emp_id:
                    deleted=True
                    continue
                else:
                    remainig_lines.append(line)    

        with open(EmployeeManager.File, mode='w') as file:
            file.writelines(remainig_lines)
            print('Deleleted successfully') if deleted else "Employee not found"
    @staticmethod
    def exit_program():
        print('Goodbye')
        sys.exit()   
if __name__ == '__main__':
    while True:
            print("\n📋 --- Employee Management Menu ---")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            try:
                choice=int(input("Enter a choice(1-6): "))
            except ValueError:
                print("Invalid number")    
                continue
            if choice==1:
                EmployeeManager.add_employee()
            elif choice==2:
                EmployeeManager.view_all()
            elif choice==3:
                emp_id=input("Enter empoyee ID: ")
                EmployeeManager.search_emp(emp_id)
            elif choice ==4:
                emp_id=input("Enter empoyee ID to update: ")
                EmployeeManager.update(emp_id)
            elif choice ==5:
                emp_id=input("Enter empoyee ID to delete: ")
                EmployeeManager.delete_employee(emp_id)
            elif choice==6:
                EmployeeManager.exit_program()
            else:
                print('Invalid choice')    
   
               
