class Todo:
    # cmds Functions
    def __init__(self):
        self.todo_list = []
        self.todo_list_checked = []

    def add(self, task_name):
        if task_name:
            self.todo_list.append(task_name)
            return True
        return False
    
    def rm(self, task_name):
        if task_name:
            try : 
                self.todo_list.remove(task_name)
            except ValueError :
                self.todo_list_checked.remove(task_name)
            return True
        return False
    
    def mark(self, task_name):
        if task_name in self.todo_list:
            self.todo_list.remove(task_name)
            self.todo_list_checked.append(task_name)
            return True
        return False
    
    def check(self):
        result = []
        if self.todo_list:
            result.append("Tasks remaining : ")
            for i, task in enumerate(self.todo_list, 1):
                result.append(f" {i} {task}")
        
        if self.todo_list_checked:
            result.append("Completed tasks : ")
            for i, task in enumerate(self.todo_list_checked, 1):
                result.append(f" {i} - {task}")

        return "\n".join(result) if result else "There is no tasks for now."
