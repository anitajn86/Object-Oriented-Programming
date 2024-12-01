class Application:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.users = []
        self.projects = []
    
    def add_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' added to the application.")

    def add_project(self, project):
        self.projects.append(project)
        print(f"Project '{project.name}' added to the application.")

    def list_users(self):
        if len(self.users) > 0:
            print("Users in the application:")
            for user in self.users:
                print(f"- {user.name}")
        else:
            print("No users in the application.")

    def list_projects(self):
        if len(self.projects) > 0:
            print("Projects in the application:")
            for project in self.projects:
                print(f"- {project.name}")
        else:
            print("No projects in the application.")


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.applications = []

    def add_application(self, application):
        self.applications.append(application)
        print(f"Application '{application.name}' added to user '{self.name}'.")

    def list_applications(self):
        if len(self.applications) > 0:
            print(f"Applications for user '{self.name}':")
            for application in self.applications:
                print(f"- {application.name}")
        else:
            print(f"No applications for user '{self.name}'.")

    def remove_application(self, application):
        if application in self.applications:
            self.applications.remove(application)
            print(f"Application '{application.name}' removed from user '{self.name}'.")
        else:
            print(f"User '{self.name}' does not have the application '{application.name}'.")

    def update_role(self, new_role):    
        self.role = new_role
        print(f"Role for user '{self.name}' updated to '{self.role}'.")

    def list_roles(self):
        print(f"Role for user '{self.name}': {self.role}")
        



    