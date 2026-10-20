import json

def display_menu():
    print("\n=== PROJECTHUB ===")
    print("1 Display projects")
    print("2 Add projects")
    print("3 Delete a project")
    print("4 Exit")

def display_projects(projects):
    print("\n=== PROJECTHUB ===")

    if len(projects) == 0:
        print("No projects.")
    else:
        print("My projects:")
        for project in projects:
            print("- " + project)

def is_valid_project_name(project):
    valid = False
    if not isinstance(project, str):
        return valid
    else:
        p = project.strip()
        if len(p) > 0:
            valid = True
        return valid

def save_projects(projects):
    with open("projects.json","w", encoding="utf-8") as f:
        json.dump(projects, f, ensure_ascii=False, indent=4)

def add_project(projects):
    new_project = input("Project name: ")
    if is_valid_project_name(new_project):
        p = new_project.strip()
        projects.append(p)
        save_projects(projects)
        print("Project added succesfully.")
    else:
        print("Invalid project name.")

def load_projects():
    try:
        with open("projects.json", "x", encoding="utf-8") as f:
            f.write("[]")
    except FileExistsError:
        pass

    try:
        with open("projects.json","r", encoding="utf-8") as f:
            projects = json.load(f)
            if not isinstance(projects,list):
                return None
            else:
                for project in projects:
                    if not is_valid_project_name(project):
                        return None
            return projects
    except json.JSONDecodeError:
        return None

def delete_project(projects):
    print("\nWhat project do you want to delete? (enter the number):")

    if len(projects) == 0:
        print("No projects to delete.")
        return
    else:
        for index, project in enumerate(projects, start=1):
            print(index, project)
        
        choice = input("Project number: ")

        if choice.isdigit():
            choice = int(choice)
            if choice > len(projects) or choice <= 0:
                print("Invalid project number.")
            else:
                print("\nDo you want to delete the project " + projects[choice-1] + "? (y/Y)")
                confirmation = input()
                if confirmation == "y" or confirmation == "Y":
                    projects.pop(choice-1)
                    save_projects(projects)
                    print("Project deleted successfully.")
                else:
                    print("Aborting.")
        else:
            print("Invalid input.")

def main():

    projects = load_projects()

    if projects is None:
        print("Unable to load projects. Exiting program.")
        return

    while True:
        display_menu()
        option = input("\nChoose an option: ")
        match option:
            case "1":
                display_projects(projects)
            case "2":
                add_project(projects)
            case "3":
                delete_project(projects)
            case "4":
                break
            case _:
                print("Invalid option.")
        
if __name__ == "__main__":
    main()