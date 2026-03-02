from todo import Todo
from utils import importtd, exporttd

def extract_task(cmd, keyword):
    return cmd.replace(keyword, "").strip()


def main():
    print(" --- Todo List Manager ---")

    manager = Todo()
    importtd(manager)
    print("Data imported.")

    while True:
        usr_cmd = input("[TODO] >>> ").lower()

        if usr_cmd.startswith("add"):
            task = extract_task(usr_cmd,"add")
            if manager.add(task):
                print(f"{task} was added in the todo list.")
            else:
                print("[!] Task name invalid.")


        elif usr_cmd.startswith("rm"):
            task = extract_task(usr_cmd,"rm")
            if manager.rm(task):
                print(f"{task} was removed.")
            else:
                print(f"[!] {task} was not found.")

        elif usr_cmd.startswith("mark"):
            task = extract_task(usr_cmd, "mark")
            if manager.mark(task):
                print(f"{task} was marked as completed.")
            else:
                print(f"[!] {task} wasn't found.")
        

        elif usr_cmd == "check":
            print(f"\n {manager.check()} \n")


        elif usr_cmd == "export":
            exporttd(manager)
        

        elif usr_cmd == "import":
            importtd(manager)
        

        elif usr_cmd == "exit": 
            print("Saving...")
            exporttd(manager)
            print("Exiting...")
            break
        

        else:
            print(f" Command {usr_cmd} not found.")


if __name__ == "__main__":
    main()
