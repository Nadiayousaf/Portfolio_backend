import json
import os

class Login:
    def __init__(self, filename="admin.json"):
        self.filename = filename
        self.admin = self.load_admin()

    def load_admin(self):
        if not os.path.exists(self.filename):
            print("Admin file not found! Please create admin.json first.")
            return None
        with open(self.filename, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Error: admin.json is empty or invalid JSON.")
                return None

    def authenticate(self):
        if not self.admin:
            return False

        attempts = 3
        while attempts > 0:
            username = input("Enter Username: ").strip()
            password = input("Enter Password: ").strip()

            if username == self.admin.get("username") and password == self.admin.get("password"):
                print("✅ Login Successful!\n")
                return True
            else:
                attempts -= 1
                print(f"❌ Invalid login! Attempts left: {attempts}\n")

        print("Too many attempts. Access denied!")
        return False
    
    

# Usage:
# login_system = Login()
# if login_system.authenticate():
#     dashboard()   # We'll create dashboard next

class Dashboard:
    def __init__(self):
        self.skills_manager = SkillManager()
        self.project_manager = ProjectManager()
        self.experience_manager = ExperienceManager()
        self.message_manager = MessageManager()

    def show(self):
        while True:
            print("\n----- Welcome to Dashboard -----")
            print("1. Manage Skills")
            print("2. Manage Projects")
            print("3. Manage Experience")
            print("4. View Messages")
            print("5. Exit")

            choice = input("Enter choice: ").strip()
            if choice == "1":
                self.skills_manager.show_menu()
            elif choice == "2":
                self.project_manager.show_menu()
            elif choice == "3":
                self.experience_manager.show_menu()
            elif choice == "4":
                self.message_manager.show_menu()
            elif choice == "5":
                print("Exiting dashboard!")
                break
            else:
                print("❌ Invalid choice!")
                
            
class BaseManager:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def add(self, item):
        self.data.append(item)
        self.save_data()

    def delete(self, index):
        try:
            removed = self.data.pop(index)
            self.save_data()
            return removed
        except IndexError:
            return None

    def update(self, index, new_item):
        try:
            self.data[index] = new_item
            self.save_data()
            return True
        except IndexError:
            return False

    def view_all(self):
        return self.data
    
    
    
    
class SkillManager(BaseManager):
    def __init__(self, filename="skills.json"):
        super().__init__(filename)

    def show_menu(self):
        while True:
            print("\n--- Skill Manager ---")
            print("1. Add Skill")
            print("2. View Skills")
            print("3. Update Skill")
            print("4. Delete Skill")
            print("5. Back to Dashboard")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.add_skill()
            elif choice == "2":
                self.view_skills()
            elif choice == "3":
                self.update_skill_menu()
            elif choice == "4":
                self.delete_skill_menu()
            elif choice == "5":
                break
            else:
                print("❌ Invalid choice!")

    def add_skill(self):
        skill = input("Skill Name: ").strip()
        level = input("Level: ").strip()
        category = input("Category: ").strip()
        self.add({"skill": skill, "level": level, "category": category})
        print(f"✅ Skill '{skill}' added successfully!")

    def view_skills(self):
        if not self.data:
            print("\nNo skills added yet.\n")
            return
        print("\n--- All Skills ---")
        for idx, s in enumerate(self.data, 1):
            print(f"{idx}. {s['skill']} - {s['level']} ({s['category']})")

    def delete_skill_menu(self):
        self.view_skills()
        try:
            index = int(input("Enter skill number to delete: ")) - 1
            removed = self.delete(index)
            if removed:
                print(f"✅ Deleted skill '{removed['skill']}'")
            else:
                print("❌ Invalid number")
        except ValueError:
            print("❌ Enter a valid number")

    def update_skill_menu(self):
        self.view_skills()
        try:
            index = int(input("Enter skill number to update: ")) - 1
            if 0 <= index < len(self.data):
                skill = self.data[index]
                new_name = input(f"New name [{skill['skill']}]: ").strip() or skill['skill']
                new_level = input(f"New level [{skill['level']}]: ").strip() or skill['level']
                new_cat = input(f"New category [{skill['category']}]: ").strip() or skill['category']
                self.update(index, {"skill": new_name, "level": new_level, "category": new_cat})
                print(f"✅ Updated skill '{new_name}'")
            else:
                print("❌ Invalid number")
        except ValueError:
            print("❌ Enter a valid number")
            
            
            
class ProjectManager(BaseManager):
    def __init__(self, filename="projects.json"):
        super().__init__(filename)

    def show_menu(self):
        while True:
            print("\n--- Project Manager ---")
            print("1. Add Project")
            print("2. View Projects")
            print("3. Update Project")
            print("4. Delete Project")
            print("5. Back to Dashboard")

            choice = input("Enter choice: ").strip()
            if choice == "1":
                self.add_project()
            elif choice == "2":
                self.view_projects()
            elif choice == "3":
                self.update_project_menu()
            elif choice == "4":
                self.delete_project_menu()
            elif choice == "5":
                break
            else:
                print("❌ Invalid choice!")

    def add_project(self):
        title = input("Title: ").strip()
        description = input("Description: ").strip()
        technology = input("Technology: ").strip()
        github = input("GitHub URL: ").strip()
        self.add({"title": title, "description": description, "technology": technology, "github": github})
        print(f"✅ Project '{title}' added successfully!")

    def view_projects(self):
        if not self.data:
            print("\nNo projects added yet.\n")
            return
        print("\n--- All Projects ---")
        for idx, p in enumerate(self.data, 1):
            print(f"{idx}. {p['title']} - {p['technology']}")
            print(f"   Description: {p['description']}")
            print(f"   GitHub: {p['github']}\n")

    def delete_project_menu(self):
        self.view_projects()
        try:
            index = int(input("Enter project number to delete: ")) - 1
            removed = self.delete(index)
            if removed:
                print(f"✅ Deleted project '{removed['title']}'")
            else:
                print("❌ Invalid number")
        except ValueError:
            print("❌ Enter a valid number")

    def update_project_menu(self):
        self.view_projects()
        try:
            index = int(input("Enter project number to update: ")) - 1
            if 0 <= index < len(self.data):
                proj = self.data[index]
                new_title = input(f"Title [{proj['title']}]: ").strip() or proj['title']
                new_desc = input(f"Description [{proj['description']}]: ").strip() or proj['description']
                new_tech = input(f"Technology [{proj['technology']}]: ").strip() or proj['technology']
                new_git = input(f"GitHub [{proj['github']}]: ").strip() or proj['github']
                self.update(index, {"title": new_title, "description": new_desc, "technology": new_tech, "github": new_git})
                print(f"✅ Updated project '{new_title}'")
            else:
                print("❌ Invalid number")
        except ValueError:
            print("❌ Enter a valid number")
            
            

class ExperienceManager(BaseManager):
    def __init__(self, filename="experience.json"):
        super().__init__(filename)

    def show_menu(self):
        while True:
            print("\n--- Experience Manager ---")
            print("1. Add Experience")
            print("2. View Experience")
            print("3. Update Experience")
            print("4. Delete Experience")
            print("5. Back to Dashboard")

            choice = input("Enter choice: ").strip()
            if choice == "1":
                self.add_experience()
            elif choice == "2":
                self.view_experience()
            elif choice == "3":
                self.update_experience_menu()
            elif choice == "4":
                self.delete_experience_menu()
            elif choice == "5":
                break
            else:
                print("❌ Invalid choice!")

    def add_experience(self):
        company = input("Company: ").strip()
        role = input("Role: ").strip()
        duration = input("Duration: ").strip()
        description = input("Description: ").strip()
        self.add({"company": company, "role": role, "duration": duration, "description": description})
        print(f"✅ Experience at '{company}' added successfully!")

    def view_experience(self):
        if not self.data:
            print("\nNo experience added yet.\n")
            return
        print("\n--- All Experience ---")
        for idx, e in enumerate(self.data, 1):
            print(f"{idx}. {e['company']} | {e['role']} | {e['duration']}")
            print(f"   Description: {e['description']}\n")

    def delete_experience_menu(self):
        self.view_experience()
        try:
            index = int(input("Enter experience number to delete: ")) - 1
            removed = self.delete(index)
            if removed:
                print(f"✅ Deleted experience at '{removed['company']}'")
            else:
                print("❌ Invalid number")
        except ValueError:
            print("❌ Enter a valid number")

    def update_experience_menu(self):
        self.view_experience()
        try:
            index = int(input("Enter experience number to update: ")) - 1
            if 0 <= index < len(self.data):
                exp = self.data[index]
                new_company = input(f"Company [{exp['company']}]: ").strip() or exp['company']
                new_role = input(f"Role [{exp['role']}]: ").strip() or exp['role']
                new_duration = input(f"Duration [{exp['duration']}]: ").strip() or exp['duration']
                new_desc = input(f"Description [{exp['description']}]: ").strip() or exp['description']
                self.update(index, {"company": new_company, "role": new_role, "duration": new_duration, "description": new_desc})
                print(f"✅ Updated experience at '{new_company}'")
            else:
                print("❌ Invalid number")
        except ValueError:
            print("❌ Enter a valid number")
            
            
            
class MessageManager(BaseManager):
    def __init__(self, filename="messages.json"):
        super().__init__(filename)

    def show_menu(self):
        while True:
            print("\n--- Message Manager ---")
            print("1. Add Message")
            print("2. View Messages")
            print("3. Delete Message")
            print("4. Back to Dashboard")

            choice = input("Enter choice: ").strip()
            if choice == "1":
                self.add_message()
            elif choice == "2":
                self.view_messages()
            elif choice == "3":
                self.delete_message_menu()
            elif choice == "4":
                break
            else:
                print("❌ Invalid choice!")

    def add_message(self):
        sender = input("Sender Email: ").strip()
        subject = input("Subject: ").strip()
        content = input("Message Content: ").strip()
        self.add({"sender": sender, "subject": subject, "content": content})
        print("✅ Message added successfully!")

    def view_messages(self):
        if not self.data:
            print("\nNo messages yet.\n")
            return
        print("\n--- All Messages ---")
        for idx, m in enumerate(self.data, 1):
            print(f"{idx}. {m['sender']} | {m['subject']}")
            print(f"   Content: {m['content']}\n")

    def delete_message_menu(self):
        self.view_messages()
        try:
            index = int(input("Enter message number to delete: ")) - 1
            removed = self.delete(index)
            if removed:
                print(f"✅ Deleted message from '{removed['sender']}'")
            else:
                print("❌ Invalid number")
        except ValueError:
            print("❌ Enter a valid number")     
            
            
            
            
            
            
            
            
            
if __name__ == "__main__":
    login_system = Login()
    if login_system.authenticate():
        dashboard = Dashboard()
        dashboard.show()