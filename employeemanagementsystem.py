e={1:{"name":"Rohit","age":25,"experience":3,"sal":40000,"mob":1234554321},2:{"name":"Rohini","age":28,"experience":2,"sal":35000,"mob":5678998765},3:{"name":"Nikita","age":20,"experience":0,"sal":10000,"mob":1357975310},4:{"name":"Raj","age":29,"experience":5,"sal":45000,"mob":4545543443}}

def dashboard():
    print("""
        1.Add data
        2.View data
        3.Update data
        4.Filter data
        5.Delete data""")

def add(emp_id,name,age,exp,sal,mob):
    e[emp_id]={"name":name,"age":age,"exp":exp,"sal":sal,"mob":mob}
    return "Added Successfully !"

def view():
    print(f"-"*125)
    print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Emp_ID","Name","Age","Experience","Salary","Mobile No"))
    print(f"-"*125)
    for emp_id in e:
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(emp_id,e[emp_id]["name"],e[emp_id]["age"],e[emp_id]["experience"],e[emp_id]["sal"],e[emp_id]["mob"]))
        print(f"-"*125)

def update(emp_id):   
    print("""
        1.Name
        2.Age
        3.Experience
        4.Salary
        5.Mobile number""")
    ch = int(input("What You Want to Update please select (1/2/3/4/5): "))
    if ch == 1:
        e[emp_id]["name"]= input("Enter the Name: ")
        return "Updated successfully !"
    elif ch == 2:
        e[emp_id]["age"]= int(input("Enter the age: "))
        return "Updated successfully !"
    elif ch == 3:
        e[emp_id]["experience"]=eval(input("Enter the experience: "))
        return "Updated successfully !"
    elif ch == 4:
        e[emp_id]["sal"] = int(input("Enter the salary : "))
        return "Updated successfully !"
    elif ch == 5:
        e[emp_id]["mob"] = int(input("Enter the mobile number : "))
        return "Updated successfully !"

def delete():
    emp_id = int(input("Enter the employee id: "))
    for emp_id in e:
        del e[emp_id]
        return "Deleted Successfully !"
    
def filtere():
    print("""What you want to filter
          1.Name
          2.Age
          3.Experience
          4.Salary
          5.Mobile""")
    ch = int(input("Enter the choice(1/2/3/4/5): "))
    if ch == 1:
        pass
    elif ch==2:
        pass
    elif ch==3:
        pass
    elif ch==4:
        pass
    elif ch == 5:
        pass
print(f"-"*90)
print(f"|{" "*40}<< Wel-come to Employee Management System >> {" "*40}|")
print(f"-"*90)
while True:
    dashboard()
    ch = int(input("Enter the choice(1/2/3/4/5): "))
    if ch==1:
        emp_id = int(input("Enter the Employee id number: "))
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        exp = eval(input("Enter the experience: "))
        sal = eval(input("Enter the salary: "))
        mob = int(input("Enter the moible number: "))

        add(emp_id,name,age,exp,sal,mob)
    elif ch==2:
        view()

    elif ch ==3:
        emp_id = int(input("Enter the Employee ID: "))
        update(emp_id)
    elif ch ==4:
        print(filtere())
    elif ch==5:
        print(delete())

