import os
import json
from pathlib import Path

# Todo List project root for data folder
a = Path("data/TD - data.json")
project_root = Path(__file__).parent.parent.parent
# Data folder/file
datafolder = project_root / "data"
datafile = datafolder / "TD - data.json"
datafolder_path = os.path.join(datafolder, datafile)

# Utils Functions

def exporttd(manager):
    foldertd()
    if a.exists():
      print("Overwriting existing file...")

    json_data = {
      "Uncompleted tasks": manager.todo_list,
      "Completed tasks": manager.todo_list_checked
    }

    with open(datafolder_path, "w", encoding="utf-8") as f :
      json.dump(json_data,f, indent=2, ensure_ascii=False)
      print(f"Done, saved in {datafile}.")



def importtd(manager):
    if not datafile.exists():
       print("Importation impossible : aucune données.")
       return [], []
    
    try:
        with open(datafile, "r", encoding="utf-8") as f : 
            json_data = json.load(f)
        manager.todo_list = json_data.get("Uncompleted tasks", [])
        manager.todo_list_checked = json_data.get("Completed tasks", [])
    
    except json.JSONDecodeError:
        print("Importation impossible : fichier corrompu")
        return [], []


def foldertd():
    if not os.path.exists(datafolder):
        os.makedirs(datafolder)
        print("Data folder was not found : New folder created.")

