from files import load_tasks, load_categories, save_tasks, save_categories
class Task:
    def __init__(self,task_name="default name", insert_date="default insert", end_date="default end",
                  task_performer="default performer", task_description="default description",
                    category="default category"):
        self.task_name=task_name
        self.insert_date=insert_date
        self.end_date=end_date
        self.task_performer=task_performer
        self.task_description=task_description
        self.category=category

    def __repr__(self):
        return f"{self.task_name} : {self.task_performer}"


    def __str__(self):
        return f"{self.task_name}\t\t{self.insert_date}\t{self.end_date}\t{self.task_performer}\t{self.task_description}\t\t{self.category}"
    
    
    def set_property(self, property, value):
        if property=="Task name":
            self.task_name=value
        if property=="End date":
            self.end_date=value
        if property=="Task performer":
            self.task_performer=value
        if property=="Task_description":
            self.task_description=value
        if property=="Category":
            self.category=value
    

    def set_property_delete(self, property):
        if property=="Task name":
            self.task_name=""
        if property=="End date":
            self.end_date=""
        if property=="Task performer":
            self.task_performer=""
        if property=="Task_description":
            self.task_description=""
        if property=="Category":
            self.category=""
            


    def pick_parameter(self):
        property=input("""pls enter what you want to change:
        1) Task name
        2) End date
        3) Task performer
        4) Task description
        5) Category               
        """)
        if property=="1":
            property="Task name"
        if property=="2":
            property="End date"
        if property=="3":
            property="Task performer"
        if property=="4":
            property="Task description"
        if property=="5":
            property="Category"
        return property



    