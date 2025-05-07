class Tasks:
    def __init__(self,name=None,descriptions=None,due_date=None,priority="Medium",category=None):
        self.name = name
        self.descriptions = descriptions
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.tasks = []
        self.priority_table = ["High","Medium","Low"]
        
    def add_task(self, name,descriptions,due_date,priority="Medium",category=None):
        task = (name, descriptions, due_date, priority, category)
        self.tasks.append(task) 
        
    def add_sub_task(self, parent_task_name, due_date, descriptions, priority="Medium", category=None):
        parent_task_index = [task[0] for task in self.tasks].index(parent_task_name)
        sub_task = (parent_task_name, due_date, descriptions, priority, category)
        self.tasks.insert(parent_task_index+1, sub_task)
        print(f"Subtask '{parent_task_name}' added successfully.")
        return parent_task_name + " has a subtask."
        
    def sort_tasks_by_priority(self):
        self.tasks.sort(key=lambda x: self.priority_table.index(x[3]))
        
    def display_tasks(self):
        print("Task List:")
        self.sort_tasks_by_priority()
        for task in self.tasks:
            print(f"Task: {task[0]} | Due Date: {task[1]} | Description: {task[2]} | Priority: {task[3]}")
            
    def filter_tasks_by_category(self, category):
        filtered_tasks = [task for task in self.tasks if task[4] == category]
        print(f"Tasks for category {category}:")
        for task in filtered_tasks:
            print(f"Task: {task[0]} | Due Date: {task[1]} | Description: {task[2]} | Priority: {task[3]}")
            
    def search_and_filter_tasks(self, category,priority="High"):
        filtered_tasks = [task for task in self.tasks if task[4] == category and task[3] == priority]
        print(f"Tasks for category {category} and priority {priority}:")
        for task in filtered_tasks:
            print(f"Task: {task[0]} | Due Date: {task[1]} | Description: {task[2]} | Priority: {task[3]}")

if __name__ =='__main__':
    task1 = Tasks()
    task1.add_task("Buy Grocery","25-11-2024","Bread","High","Home")
    task1.add_task("Read a book","11-12-2022","Finish chapter 3","Low","Self Learning")
    task1.add_task("Clean the house","20-10-2023","Clean all the floors and windows","Medium","Home")
    #task1.filter_tasks_by_category("Home")
    #task1.add_sub_task("Clean the house","20-10-2023","Clean all the floors and windows","Medium","Home")
    #task1.display_tasks()
    #task1.add_sub_task("Read a book","20-10-2023","Finish chapter","High","Self Learning")
    
    task1.add_sub_task("Read a book","20-01-2023","Finish chapter","Low","Self Learning")
    #task1.search_and_filter_tasks("Home")
    task1.display_tasks()
