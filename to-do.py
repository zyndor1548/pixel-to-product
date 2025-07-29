# class Task:
#     def __init__(self,name,time):
#         self.name = name
#         self.time = time
#     def __str__(self):
#         return f"{self.name} for {self.time} mins"
#     def __reper__(self):
#         return f"{self.name}:{self.time}"
# class todo:
#     def __init__(self):
#         self.tasks = []
#     def add_task(self,task):
#         self.tasks.append(task)
#     def delete_task(self,id):
#         self.tasks.pop(id)
#     def view_task(self):
#         return [task for task in self.tasks]


# if __name__ == "__main__":
    
#     da = todo()
#     while True:
#         print("---Menu---")
#         print("1. Add Task")
#         print("2. delete task")
#         print("3. display task")
#         print("4. exit")
#         choice = input("Enter choice : ")
#         match choice:
#             case "1": 
#                 task = input("Enter task name : ")
#                 time = input("enter time for task : ")
#                 da.add_task(Task(task,time))
#             case "2":
#                 id = int(input("Enter task name : "))
#                 da.delete_task(id)
#             case "3":
#                 for i in da.view_task():
#                     print("\t",i)
#             case "4":
#                 break
#             case _:
#                 print("invalid option")


class Task:
    def __init__(self,name,time):
        self.name = name
        self.time = time
    def __str__(self):
        return f"{self.name} for {self.time} mins"
    def __reper__(self):
        return f"{self.name}:{self.time}"
class todo:
    def __init__(self):
        self.tasks = []
    def add_task(self,task):
        self.tasks.append(task)
    def delete_task(self,id):
        self.tasks.pop(id)
    def view_task(self):
        return [task for task in self.tasks]


if __name__ == "__main__":
    
    da = todo()
    while True:
        print("---Menu---")
        print("1. Add Task")
        print("2. delete task")
        print("3. display task")
        print("4. exit")
        choice = input("Enter choice : ")
        match choice:
            case "1": 
                task = input("Enter task name : ")
                time = input("enter time for task : ")
                da.add_task(Task(task,time))
            case "2":
                id = int(input("Enter task name : "))
                da.delete_task(id)
            case "3":
                for i in da.view_task():
                    print("\t",i)
            case "4":
                break
            case _:
                print("invalid option")
