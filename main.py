import json

def display_menu():
    print("\n=== PROJECTHUB ===")
    print("1. Mostrar proyectos")
    print("2. Añadir proyecto")
    print("3. Salir")

def display_projects(projects):
    print("\n=== PROJECTHUB ===")

    if len(projects) == 0:
        print("No projects.")
    else:
        print("Mis proyectos:")
        for project in projects:
            print("- " + project)

def add_project(projects):
    new_project = input("Nombre del proyecto: ")
    p = new_project.strip()
    if len(p) == 0:
        print("No project introduced.")
    else:
        projects.append(new_project)
        with open("projects.json","w", encoding="utf-8") as f:
            json.dump(projects, f, ensure_ascii=False, indent=4)
        print("Proyecto añadido correctamente.")

def main():

    try:
        with open("projects.json", "x", encoding="utf-8") as f:
            f.write("[]")
    except FileExistsError:
        pass

    with open("projects.json","r", encoding="utf-8") as f:
        projects = json.load(f)

    while True:
        display_menu()
        option = input("\nSelecciona una opción: ")
        match option:
            case "1":
                display_projects(projects)
            case "2":
                add_project(projects)
            case "3":
                break
            case _:
                print("Opción no válida.")
        
main()