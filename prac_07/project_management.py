"""
Estimated time: 1.5 hours
Actual time: 2 hours
"""

import datetime

from project import Project


def load_projects(file_name):
    projects = []
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()[1:]  # Skip the header
            for line in lines:
                data = line.strip().split('\t')
                name, start_date, priority, cost_estimate, completion_percentage = data
                project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
                projects.append(project)
    except FileNotFoundError:
        projects = []
    return projects


def save_projects(file_name, projects):
    with open(file_name, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate:.2f}\t{project.completion_percentage}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_completed()]
    completed_projects = [project for project in projects if project.is_completed()]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, date):
    filtered_projects = [project for project in projects if project.start_date > date]
    filtered_projects.sort(key=lambda p: p.start_date)

    for project in filtered_projects:
        print(f"{project}")


def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    print("Project List:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))

    if 0 <= project_choice < len(projects):
        project = projects[project_choice]
        print(project)
        new_completion_percentage = int(input("New Percentage: "))
        new_priority = input("New Priority: ")
        if new_priority:
            project.priority = int(new_priority)
        project.completion_percentage = new_completion_percentage


def main():
    file_name = 'projects.txt'
    projects = load_projects(file_name)

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").strip().lower()
        if choice == 'l':
            projects = load_projects(file_name)
        elif choice == 's':
            save_projects(file_name, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_projects(file_name, projects)
            print("Thank you for using custom-built project management software.")
            break


if __name__ == "__main__":
    main()
