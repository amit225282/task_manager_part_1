import pickle
import random
from classes import Task
import datetime
from files import load_tasks, save_tasks, load_categories, save_categories
def intro_login():

    
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
#intro_login()

def menu():
    while True:
        command=input("""
1) Add task
2) Display all tasks                      
3) Edit task
4) Delete task
5) Add category  
6) Search task by task name
7) Search tasks by task performer                                                   
8) Search tasks by task category 
9) Exit  

Please enter your command: """)                                                                                                             

    
        if command=='1':
            print("You chose- Add task.")
            pass

        if command=='2':
            print("You chose- Display all tasks .")
            pass

        if command=='3':
            print("You chose- Edit task.")
            pass

        if command=='4':
            print("You chose- Delete task. ")
            pass

        if command=='5':
            print("You chose- Add category. ")

            pass

        if command=='6':
            print("You chose- Search task by task name.")
            pass

        if command=='7':
            print("You chose- Search tasks by task performer. ")
            pass

        if command=='8':
            print("You chose- Search tasks by task category. ")
            pass

        if command=='9':
            print("bye bye")
            exit()
#menu()

def add_task(task:Task):  #קיים שדרוג לפונקציה בפונקציה הבאה
    '''This function adds to file a task.'''
    tasks=load_tasks()
    lengh1=len(tasks)
    tasks.append(task)
    lengh2=len(tasks)
    save_tasks(tasks=tasks)
    if lengh2>lengh1:              #קיים לבדיקה שדרוג בהמשך
            print("Task added successfully!")


#add_task(task=input("enter task to add: "))
#print(load_tasks())


def add_task(task:Task):  #שדרוג לפונקציה הקודמת
    '''This function adds to file a task.'''
    tasks=load_tasks()
    test_task=task.task_name
    tasks.append(task)
    save_tasks(tasks=tasks)
    tasks=load_tasks()

    for task in tasks:
        if task.task_name.find(test_task)==0:
              print("Task added successfully!")

#tasks=load_tasks()              #!בדיקה לשדרוג לטסט
#for task in tasks:
#    if task.task_name.find("ido")==0:
#        print("great!")

def setup_categories(categories_file="categories.pickle"):
    '''This function creates a file with categories list.'''
    with open (categories_file, 'wb') as f:
        categories=["clean", "work", "money", "family"]
        pickle.dump(categories, f)
        return categories
#print(setup_categories())
        

def add_category(category):
    '''This function adds to file a category.'''
    categories=load_categories()
    lengh1=len(categories)
    categories.append(category)
    categories=set(categories)
    categories=list(categories)
    lengh2=len(categories)
    save_categories(categories=categories)
    if lengh2>lengh1:
        print("Category added successfully!")
    else:
        print("Category already exists!")

#add_category(category=input("enter category to add: "))
#print(load_categories())
def create_category():
    '''This function create a new category.'''
    category=input("Please enter new category: ")
    add_category(category)


#insert_date.sort(key= lambda x:x ,reverse=True)#
#print(load_tasks())  

def choose_add_category():
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
            category=input("Please enter new category: ")
            add_category(category)
            return category

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
                    print("Wrong number, category not found")        
                    question=input(" category from the list, 'q' to exit: ")

        command=input(f"""     
- If you want to choose a category from the list, PRESS 1.
- If you want to add a new category, PRESS 2. 
- If you want to exit, PRESS 'q'
""")
#print(choose_add_category())



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
#create_task()
#print(load_tasks()) 


def create_task_random():
    '''This function create a task with random values'''
    task_name=f'{random.choice(["wash", "clean", "go", "bring", "pay", "return"])} the {random.choice(["dog", "child", "bill", "dishes", "house", "car"])}'
    insert_date=datetime.date.today()
    end_date=datetime.datetime(random.randint(2023,2024), random.randint(8,12), random.randint(1,30))
    while ((end_date.year==insert_date.year) and (end_date.month<insert_date.month)) or ((end_date.year==insert_date.year) and (end_date.month==insert_date.month) and (end_date.day<insert_date.day)):
        end_date=datetime.datetime(random.randint(2023,2024), random.randint(1,12), random.randint(1,30))
    task_performer=random.choice(["Amit", "Tal", "Ido", "Mom"])
    more_text=f' very {random.choice(["good", "carefully", "fast"])}'
    task_description=task_name+more_text
    categories=load_categories()
    category=random.choice(categories)
    add_task(Task(task_name=task_name, insert_date=insert_date, end_date=end_date,
                   task_performer=task_performer,task_description=task_description, category=category))
    
#create_task_random()
#print(load_tasks())



#insert_date=datetime.date.today()  #כל מיני בדיקות שביצעתי
#print(insert_date)

#end_date=datetime.datetime(random.randint(2023,2024), random.randint(1,12), random.randint(1,30))
#print(end_date)
#while ((end_date.year==insert_date.year) and (end_date.month<insert_date.month)) or ((end_date.year==insert_date.year) and (end_date.month==insert_date.month) and (end_date.day<insert_date.day)):
#    end_date=datetime.datetime(random.randint(2023,2024), random.randint(1,12), random.randint(1,30))

#print(end_date)
#print(end_date.year==insert_date.year and end_date.month>insert_date.month)




def update():
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

#update()
#print(load_tasks())        


def delete_value():
    '''This function deletes task value by task name.'''
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
        
#delete_value()
#print(load_tasks())


def delete_item():
    '''This function deletes a task by task name.'''
    tasks=load_tasks()
    name=input("Please enter task name: ")
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
#delete_item()
#print(load_tasks())

def choose_add_task():
    '''In this function you choose the way to add your task.'''
    command=input("""
Please choose:
1. Add task manually.
2. Add task randomaly.
3. Exit
""")
    while command!='3':
        if command=='1':
            create_task()
            break
        if command=='2':
            create_task_random()
            break
        print("")
        print("Wrong number, try again.")
        command=input("""
Please choose:
1. Add task manually.
2. Add task randomaly.
3. Exit
""")
    
#choose_add_task()

def display_tasks():
    tasks=load_tasks()
    print(f"Task name\tInsert date\tEnd date\tPerformer\tdescription\tCategory")
    print("----------------------------------------------------------------------------------------")
    tasks.sort(key=lambda t: (t.task_name)) 
    for task in tasks:
        print(task)
#display_tasks()

def display_by_task_name():
    tasks=load_tasks()
    name=input("Please enter task name (1 letter minimum): ")
    print(f"Task name\t\tInsert date\tEnd date\tPerformer\tdescription\tCategory")
    print("----------------------------------------------------------------------------------------")
    tasks.sort(key=lambda t: (t.task_name)) 
    lengh=len(name)
    for task in tasks:
        if str(task.task_name)[:lengh]==name:
            print(task)


def display_by_task_performer():
    tasks=load_tasks()
    name=input("Please enter performer name (1 letter minimum): ")
    print(f"Task name\t\tInsert date\tEnd date\tPerformer\tdescription\tCategory")
    print("----------------------------------------------------------------------------------------")
    tasks.sort(key=lambda t: (t.task_performer)) 
    lengh=len(name)
    for task in tasks:
        if str(task.task_performer)[:lengh]==name:
            print(task)
#display_by_task_performer()


def display_by_task_category():
    tasks=load_tasks()
    name=input("Please enter task category (1 letter minimum): ")
    print(f"Task name\t\tInsert date\tEnd date\tPerformer\tdescription\tCategory")
    print("----------------------------------------------------------------------------------------")
    tasks.sort(key=lambda t: (t.category)) 
    lengh=len(name)
    for task in tasks:
        if str(task.category)[:lengh]==name:
            print(task)
#display_by_task_category()

















