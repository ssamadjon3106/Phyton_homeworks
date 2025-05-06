def add_employee():
    with open("lesson-6/homework/employees.txt", mode='a') as file:
        emp_id=input("Enter ID:")
        name=input("Enter a name:")
        position=input("Enter a position")
        salary=input("Enter a salary")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
    print("Employee added!") 

def view_all():
    with open("lesson-6/homework/employees.txt", mode= 'r') as file:
        print('\n ALL Employees: ')
        for line in file:
            print(line.strip()) 
def search_emp(emp_id):
    with open("lesson-6/homework/employees.txt", mode='r') as file:
        for line in file:
            if line.startswith(emp_id + ","):
                print("Employee found:")
                print(line.strip())
                return
    print("Employee not found")
def update(emp_id):
    updated=False
    lines=[]
    with open("lesson-6/homework/employees.txt", mode='r') as file:
        for line in file:
            if line.startswith(emp_id + ","):
                print("employee found.Enter new details: ")
                name=input("Enter a name:")
                position=input("Enter a position")
                salary=input("Enter salary")
                lines.append(f'{emp_id}, {name}, {position}, {salary}')
                updated=True
            else:
                lines.append(line)    

    with open("lesson-6/homework/employees.txt", mode='w') as file:
        file.writelines(lines)
        if updated:
            print("Uptaded successfully")
        else:
            print("employee not found")           
            

def delete_employee(emp_id):
    deleted=False
    lines=[]
    with open("lesson-6/homework/employees.txt", mode='r') as file:
        for line in file :
            if line.startswith(emp_id + ','):
                deleted=True
                continue
            else:
                lines.append(line)    

    with open("lesson-6/homework/employees.txt", mode='w') as file:
        file.writelines(lines)
    if deleted:
        print('deleted successfully')
    else:
        print('employee ID not found')

def exit_program():
    import sys
    sys.exit()   

def employee_manage_system():
    choice=0
    while choice!=6:
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
            add_employee()
        elif choice==2:
             view_all()
        elif choice==3:
            emp_id=input("Enter empoyee ID: ")
            search_emp(emp_id)
        elif choice ==4:
            emp_id=input("Enter empoyee ID to update: ")
            update(emp_id)
        elif choice ==5:
            emp_id=input("Enter empoyee ID to delete: ")
            delete_employee(emp_id)
        elif choice==6:
            print("👋 Exiting Employee Management System. Goodbye!") 
            break  

if __name__ == "__main__":
    employee_manage_system()
