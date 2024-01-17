import datetime
import random
from classes import Task
from files import load_tasks, save_tasks, load_categories, save_categories, setup_categories
def intro_login():
    '''This function activates a short intro and login task.'''
    
    print("""Hey! Welcome to task manager program.""")
    print("")
    user_name=input("please enter your name: ")
    given_otp= random.randrange(100000,999999)
    print("")
    print("")
    print(f'''Hey {user_name}! We want to make sure you are not a robot by a simple test.  

Your code is {given_otp}
''')
    otp=input("Please enter the code above: ")
    print("")
    counter=4
    while str(given_otp)!=otp and counter!=0:
        if str(given_otp)!=otp:
            print(f"""
Try again  :(
You have {counter} more tries.
""")
            print(f"Your code is {given_otp}")
            otp=input("Please enter the code above: ")
            counter-=1
        if counter==0:
            print("")
            print("Sorry, the system blocked you.")
            exit()
        if str(given_otp)==otp:
            print("")
            print(f"Great! Now, let's begin.")
            break

def menu():
    '''This function shows the menu.'''
    while True:
        command=input("""
1) Add task
2) Display all tasks                      
3) Edit task
4) Delete task
5) Delete a value in task
6) Add category  
7) Search task by task name
8) Search tasks by task performer                                                   
9) Search tasks by task category 
10) Exit  

Please enter your command: """)                                                                                                             

    
        if command=='1':
            print("You chose- Add task.")
            print("")
            choose_add_task()


        if command=='2':
            print("You chose- Display all tasks. ")
            print("")
            display_tasks()

        if command=='3':
            print("You chose- Edit task. ")
            print("")
            update()

        if command=='4':
            print("You chose- Delete task. ")
            print("")
            delete_item()

        if command=='5':
            print("You chose- Delete a value in task. ")
            print("")
            delete_value()

        if command=='6':
            print("You chose- Add category. ")
            print("")
            create_category()

        if command=='7':
            print("You chose- Search task by task name. ")
            print("")
            display_by_task_name()

        if command=='8':
            print("You chose- Search tasks by task performer. ")
            print("")
            display_by_task_performer()

        if command=='9':
            print("You chose- Search tasks by task category. ")
            print("")
            display_by_task_category()

        if command=='10':
            quit()



def add_task(task:Task):
    '''This function adds to file a task.'''
    tasks=load_tasks()
    test_task=task.task_name
    tasks.append(task)
    save_tasks(tasks=tasks)
    tasks=load_tasks()

    for task in tasks:
        if task.task_name.find(test_task)==0:
              print("Task added successfully!")
        
def add_category(category):
    '''This function adds to file a category.'''
    categories=load_categories()
    lengh1=len(categories)
    categories.append(category)
    categories=set(categories)
    categories=list(categories)
    save_categories(categories=categories)
    categories=load_categories()
    lengh2=len(categories)
    if lengh2>lengh1:
        return print("Category added successfully!")
    else:
        return print("Category already exists!")

def choose_add_category():
    '''This function chooses the way to add the category.'''
    counter=1
    print("Categories:")
    categories_num=[]
    for category in load_categories():
        category_num=f'{counter}. {category}'
        print(category_num)
        categories_num.append(category_num)
        counter+=1

    command=input(f"""     
- If you want to choose a category from the list, PRESS 1.
- If you want to add a new category, PRESS 2. 
- If you want to exit, PRESS 'q'
""")

    while command!='q':
        if command=='2':
            create_category()

        if command=='1':
            for category_num in categories_num:
                print(category_num)
            question=input("Select your category from the list ('q' to exit): ")
            while question !='q':
                for category_num in categories_num:
                    if question==category_num[0]:
                        category=category_num[3:]
                        return category
                if question!=category_num[0]:
                    for category_num in categories_num:
                        print(category_num)
                    print("")    
                    print("Wrong number, category not found.")        
                    question=input("Please select your category from the list above ('q' to exit): ")
        command=input(f"""     
- If you want to choose a category from the list, PRESS 1.
- If you want to add a new category, PRESS 2. 
- If you want to exit, PRESS 'q'
""")
    if command=='q':
        category=''
        return category

def create_task():
    '''This function creates a task manually.'''
    task_name=input("please enter task name: ")
    insert_date=datetime.date.today()
    end_date=input("please enter end date: ")
    task_performer=input("please enter task performer: ")
    task_description=input("please enter task description: ")
    category=choose_add_category()
    add_task(Task(task_name=task_name, insert_date=insert_date, end_date=end_date,
                   task_performer=task_performer,task_description=task_description, category=category))

def create_task_random():
    '''This function create a task with random values'''
    task_name=f'{random.choice(["wash", "clean", "go", "bring", "pay", "return"])} the {random.choice(["dog", "child", "bill", "dishes", "house", "car"])}'
    insert_date=datetime.date.today()
    end_date=datetime.datetime(random.randint(2023,2024), random.randint(8,12), random.randint(1,30))
    while ((end_date.year==insert_date.year) and (end_date.month<insert_date.month)) or ((end_date.year==insert_date.year) and (end_date.month==insert_date.month) and (end_date.day<insert_date.day)):
        end_date=datetime.datetime(random.randint(2023,2024), random.randint(1,12), random.randint(1,30))
    end_date=end_date.date()
    task_performer=random.choice(["Amit", "Tal", "Ido", "Mom"])
    more_text=f' very {random.choice(["good", "carefully", "fast"])}'
    task_description=task_name+more_text
    categories=load_categories()
    category=random.choice(categories)
    add_task(Task(task_name=task_name, insert_date=insert_date, end_date=end_date,
                   task_performer=task_performer,task_description=task_description, category=category))

def update():
    '''This function updates task value by task name.'''
    tasks=load_tasks()
    name=input("Please enter task name ('q' to exit): ")
    while name!='q':
        for task in tasks:
            if task.task_name==name:
                parameter=task.pick_parameter()
                value=input("Please enter value: ")
                test_task=value
                task.set_property(parameter,value)
                save_tasks(file="tasks.pickle",tasks=tasks)
                tasks=load_tasks()
                for task in tasks:
                    if str(task.task_name).find(test_task)==0 or str(task.end_date).find(test_task)==0 or str(task.task_performer).find(test_task)==0 or str(task.task_description).find(test_task)==0 or str(task.category).find(test_task)==0:
                        return print('Value updated.')
                    
                if str(task.task_name).find(test_task)!=0 or str(task.end_date).find(test_task)!=0 or str(task.task_performer).find(test_task)!=0 or str(task.task_description).find(test_task)!=0 or str(task.category).find(test_task)!=0:
                    return print("Something went wrong, try again :( ")
        print("")
        print("Wrong task name, try again.")
        name=input("Please enter task name ('q' to exit): ")

def delete_value():
    '''This function deletes a task value by task name.'''
    tasks=load_tasks()
    name=input("Please enter task name ('q' to exit): ")
    while name!='q':
        for task in tasks:
            if task.task_name==name:
                task.set_property_delete(task.pick_parameter())
                save_tasks(file="tasks.pickle",tasks=tasks)
                return print('Value deleted.')
        print("")
        print("Wrong task name, try again.")
        name=input("Please enter task name ('q' to exit): ")

def delete_item():
    '''This function deletes a task by task name.'''
    tasks=load_tasks()
    name=input("Please enter task name ('q' to exit): ")
    while name!='q':
        for task in tasks:
            if task.task_name==name:
                tasks.remove(task)
                save_tasks(file="tasks.pickle",tasks=tasks)
                tasks=load_tasks()
                for task in tasks:
                    if str(task.task_name).find(name)==0:
                        return print("Sorry, somthing went wrong, try again :(")
                return print('Task deleted.')
        print("")
        print("Wrong task name, try again.")
        name=input("Please enter task name ('q' to exit): ")

def choose_add_task():
    '''In this function you choose the way to add your task.'''
    command=input("""
Please choose ('q' to exit):
1. Add task manually.
2. Add task randomaly.
""")
    while command!='q':
        if command=='1':
            create_task()
            break
        if command=='2':
            create_task_random()
            break
        print("")
        print("Wrong number, try again.")
        command=input("""
Please choose ('q' to exit):
1. Add task manually.
2. Add task randomaly.
""")
        
def quit():
    '''This function closes the app with a nice goodbye :)'''
    print("""
bye bye. 
Hope you enjoyed :) """)
    exit()

def create_category():
    '''This function create a new category.'''
    category=input("Please enter new category ('q' to exit): ")
    while category !='q':
        add_category(category)
        break

def display_tasks():
    '''This function displays all tasks in a nice table.'''
    tasks=load_tasks()
    print(f"Task name\t\tInsert date\tEnd date\tPerformer\tdescription\t\t\tCategory")
    print("----------------------------------------------------------------------------------------------------------------")
    tasks.sort(key=lambda t: (t.task_name)) 
    for task in tasks:
        print(task)

def display_by_task_name():
    '''This function displays all tasks that contains the value in the "search" input in their task name.'''  
    tasks=load_tasks()
    search=input("Please enter task name (1 letter minimum): ")
    print(f"Task name\t\tInsert date\tEnd date\tPerformer\tdescription\t\t\tCategory")
    print("----------------------------------------------------------------------------------------------------------------")
    tasks.sort(key=lambda t: (t.task_name)) 
    lengh=len(search)
    for task in tasks:
        if str(task.task_name)[:lengh]==search:
            print(task)
    
def display_by_task_performer():
    '''This function displays all tasks that contains the value in the "search" input in their performer name.'''
    tasks=load_tasks()
    search=input("Please enter performer name (1 letter minimum): ")
    print(f"Task name\t\tInsert date\tEnd date\tPerformer\tdescription\t\t\tCategory")
    print("----------------------------------------------------------------------------------------------------------------")
    tasks.sort(key=lambda t: (t.task_performer)) 
    lengh=len(search)
    for task in tasks:
        if str(task.task_performer)[:lengh]==search:
            print(task)

def display_by_task_category():
    '''This function displays all tasks that contains the value in the "search" input in their task category.'''
    tasks=load_tasks()
    search=input("Please enter task category (1 letter minimum): ")
    print(f"Task name\t\tInsert date\tEnd date\tPerformer\tdescription\t\t\tCategory")
    print("----------------------------------------------------------------------------------------------------------------")
    tasks.sort(key=lambda t: (t.category)) 
    lengh=len(search)
    for task in tasks:
        if str(task.category)[:lengh]==search:
            print(task)

