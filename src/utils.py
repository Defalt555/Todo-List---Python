import os
import json
from pathlib import Path


a = Path("data/TD - data.json")
datafolder = "data"
datafile = "TD - data.json"
datafolder_path = os.path.join(datafolder, datafile)


def exporttd(todo_list, todo_list_checked):
    if a.exists():
      print("Overwriting existing file...")

    json_data = {
      "Uncompleted tasks": todo_list,
      "Completed tasks": todo_list_checked
    }

    with open(datafolder_path, "w", encoding="utf-8") as f :
      json.dump(json_data,f, indent=2, ensure_ascii=False)
      print("Done.")



def importtd():
    if not os.path.exists(datafolder_path):
       print("Importation impossible : aucune données.")
       return [], []
    
    try:
        with open("data/TD - data.json", "r", encoding="utf-8") as f : 
            json_data = json.load(f)
        todo_list = json_data["Uncompleted tasks"]
        todo_list_checked = json_data["Completed tasks"]
        return todo_list, todo_list_checked      
    
    except json.JSONDecodeError:
        print("Importation impossible : fichier corrompu")
        return [], []


def foldertd():
    if not os.path.exists(datafolder):
        os.makedirs(datafolder)
    print("Data folder was not found : New folder created.")

# Functions here