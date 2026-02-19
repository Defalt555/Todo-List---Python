from math import *
import os.path

todo_list = []
todo_list_checked = []

print("--- Welcome to Todo-List creator, please enter a command --- \n")

while True:
  usr_cmd = input("[TD] >>> ").lower()

  if "add" in usr_cmd:
    task_name_split = usr_cmd.split()
    if "add" not in task_name_split:
      print(f"Error : add wasn't spelled properly in {task_name_split}.")
      continue
    if "add" not in task_name_split[0]:
      print(f"Error : Wrong order of command.")
      continue
    task_name_split.remove("add")
    task_name = " ".join(str(x) for x in task_name_split)
    print(f"[DEBUG] : current value is {task_name}")
    todo_list.append(task_name)
    print(f"{task_name} has successfully been added.")

  if "rm" in usr_cmd:
    task_name_split = usr_cmd.split()
    if "rm" not in task_name_split:
      print(f"Error : rm wasn't spelled properly in {task_name_split}.")
      continue
    if "rm" not in task_name_split[0]:
      print(f"Error : Wrong order of command.")
      continue
    task_name_split.remove("rm")
    task_name = " ".join(str(x) for x in task_name_split)
    print(f"[DEBUG] : current value is {task_name}")
    if task_name in todo_list:
      todo_list.remove(task_name)
      print(f"{task_name} has successfully been removed.")
    else:
      print(f"{task_name} hasn't been found in this list. Try Again.")

  if "mark" in usr_cmd:
    task_name_split = usr_cmd.split()
    if "mark" not in task_name_split:
      print(f"Error : mark wasn't spelled properly in {task_name_split}.")
      continue
    if "mark" not in task_name_split[0]:
      print(f"Error : Wrong order of command.")
      continue
    task_name_split.remove("mark")
    task_name = " ".join(str(x) for x in task_name_split)
    print(f"[DEBUG] : current value is {task_name}")
    if task_name in todo_list:
      todo_list_checked.append(task_name)
      todo_list.remove(task_name)
      print(f"{task_name} has successfully been checked.")
    else:
      print(f"{task_name} hasn't been found in this list. Try Again.")
  
  if usr_cmd == "import" :
    task_name_split = usr_cmd.split()
    if "import" not in task_name_split:
      print(f"Error : import wasn't spelled properly in {task_name_split}.")
      continue
    if "import" not in task_name_split[0]:
      print(f"Error : Wrong order of command.")
      continue
    task_name_split.remove("import")
    task_name = " ".join(str(x) for x in task_name_split)
    print(f"[DEBUG] : current value is {task_name}")
    pass 

  if usr_cmd == "export" :
    task_name_split = usr_cmd.split()
    if "export" not in task_name_split:
      print(f"Error : export wasn't spelled properly in {task_name_split}.")
      continue
    if "export" not in task_name_split[0]:
      print(f"Error : Wrong order of command.")
      continue
    task_name_split.remove("export")
    task_name = " ".join(str(x) for x in task_name_split)
    print(f"[DEBUG] : current value is {task_name}")
    try :
      f = open("TD - datas.txt", "x")
    except FileExistsError : 
      print("[ ! ] file already exists")

  if usr_cmd == "check" :
    if len(todo_list) != 0:
      print(f"currently, there is {todo_list} in the todo list that were not checked.")
    else:
      print("There is no task remaining.")
    if len(todo_list_checked) > 0 :
      print(f"And there is {todo_list} that are checked.")
  
  if usr_cmd == "exit" :
    print("Exiting script.")
    exit()