import json

def display_menu():
    print("\n=== PROJECTHUB ===")
    print("1. Display projects")
    print("2. Add projects")
    print("3. Exit")

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

    with open("projects.json","r", encoding="utf-8") as f:
        projects = json.load(f)

    return projects

def main():

    projects = load_projects()

    while True:
        display_menu()
        option = input("\nChoose an option: ")
        match option:
            case "1":
                display_projects(projects)
            case "2":
                add_project(projects)
            case "3":
                break
            case _:
                print("Invalid option.")
        
if __name__ == "__main__":
    main()