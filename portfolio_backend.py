### Admin Login
import json
import os

def login():
    if not os.path.exists("admin.json"):
        print("Admin file not found! Please create admin.json first.")
        return False
    with open("admin.json", "r") as f:
        try:
            admin = json.load(f)
        except json.JSONDecodeError:
            print("Error: admin.json is empty or invalid JSON.")
            return False

    attempts = 3
    while attempts > 0:
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()

        if username == admin["username"] and password == admin["password"]:
            print("Login Successful!")
            return True
        else:
            attempts -= 1
            print(f"❌ Invalid login! Attempts left: {attempts}\n")

    print("Too many attempts. Access denied!")
    return False

def dashboard():
    while True:
        print("-----Wellcome to Dashboard-----")
        print("1. Manage Skills")
        print("2. Manage Projects")
        print("3. Manage Experience")
        print("4. View Messages")
        print("5. Exit! ")
        
        choice=input("Enter Choice: ")
        if choice=="1":
            skills_manager()
        elif choice=="2":
            project_manager()
        elif choice=="3":
            experience_manager()
        elif choice=="4":
            message_manager()
        elif choice=="5":
            print("Exit Dashboard!")
            break
        
def skills_manager():
    while True:
        print("\n--- Skills Manager ---")
        print("1. Add Skill")
        print("2. View Skills")
        print("3. Delete Skill")
        print("4. Update Skill")
        print("5. Back to Dashboard")

        choice = input("Enter choice: ")

        if choice == "1":
            add_skill()
        elif choice == "2":
            view_skills()
        elif choice == "3":
            delete_skill()
        elif choice == "4":
            update_skill()
        elif choice == "5":
            break
        else:
            print("Invalid Choice")
            
def add_skill():
            Skill_name=input("Enter the Skills: ")
            level=input("Enter level: ")
            category=input("Enter the category: ")
            
            
            if not os.path.exists("skills.json"):
                skills=[]
            else:
    
             with open("skills.json", "r") as f:
              skills = json.load(f) 
              
            new_skill = {
                  "skill": Skill_name,
                   "level": level,
                   "category": category
                    }
            skills.append(new_skill)
            with open("skills.json", "w") as f:
                json.dump(skills,f, indent=4)
            
              
            print(f"\n skill,'{Skill_name}'added Successfully!\n ]")
              
def view_skills():
         if not os.path.exists("skills.json"):
             print("\nNo skills added yet.\n")
         
  
         with open("skills.json", "r") as f:
             skills = json.load(f)

         if not skills:
             print("\nNo skills added yet.\n")
             return

         print("\n--- All Skills ---")
         for idx, skill in enumerate(skills, 1):
             print(f"{idx}. {skill['skill']} - {skill['level']} ({skill['category']})")
             print("")  
            
    
def delete_skill():
        if not os.path.exists("skills.json"):
             print("\nNo skills added yet.\n")
             return
        with open("skills.json", "r") as f:
          skills = json.load(f)
        if not skills:
          print("\nNo skills added yet.\n")
          return

        print("\n--- Delete Skill ---")
        for idx, skill in enumerate(skills, 1):
         print(f"{idx}. {skill['skill']} - {skill['level']} ({skill['category']})")

        try:
         choice = int(input("Enter skill number to delete: "))
         if 1 <= choice <= len(skills):
            removed_skill = skills.pop(choice - 1)
            with open("skills.json", "w") as f:
                json.dump(skills, f, indent=4)
            print(f"\n✅ Skill '{removed_skill['skill']}' deleted successfully!\n")
         else:
            print("❌ Invalid number. No skill deleted.\n")
        except ValueError:
          print("❌ Invalid input. Enter a number.\n")
 

 
def update_skill():
        if not os.path.exists("skills.json"):
           print("\nNo skills added yet.\n")
           return
        with open("skills.json", "r") as f:
           skills = json.load(f)
        if not skills:
            print("\nNo skills added yet.\n")
            return

        print("\n--- Update Skill ---")
        for idx, skill in enumerate(skills, 1):
           print(f"{idx}. {skill['skill']} - {skill['level']} ({skill['category']})")

        try:
           choice = int(input("Enter skill number to update: "))
           if 1 <= choice <= len(skills):
            selected_skill = skills[choice - 1]

            new_name = input(f"Enter new skill name [{selected_skill['skill']}]: ")
            new_level = input(f"Enter new level [{selected_skill['level']}]: ")
            new_category = input(f"Enter new category [{selected_skill['category']}]: ")

            if new_name.strip():
                selected_skill['skill'] = new_name
            if new_level.strip():
                selected_skill['level'] = new_level
            if new_category.strip():
                selected_skill['category'] = new_category

            with open("skills.json", "w") as f:
                json.dump(skills, f, indent=4)
            print(f"\n✅ Skill '{selected_skill['skill']}' updated successfully!\n")
           else:
            print("❌ Invalid number. No skill updated.\n")
        except ValueError:
            print("❌ Invalid input. Enter a number.\n")
            
            
def project_manager():
    while True:
        print("\n--- Project Manager ---")
        print("1. Add Project")
        print("2. View Project")
        print("3. Delete Project")
        print("4. Update Project")
        print("5. Back to Dashboard")

        choice = input("Enter choice:")

        if choice == "1":
            add_project()
        elif choice == "2":
            view_project()
        elif choice == "3":
            delete_project()
        elif choice == "4":
            update_project()
        elif choice == "5":
            break
        else:
            print("Invalid Choice")
def add_project():

    Title = input("Project Title: ").strip()
    description = input("Project Description: ").strip()
    technology = input("Project technology: ").strip() 
    github = input("Github: ").strip()

    if not os.path.exists("projects.json"):
        projects = []
    else:
        with open("projects.json", "r") as f:
            projects = json.load(f)

    new_project = {
        "title": Title,
        "description": description,
        "technology": technology,
        "github": github
    }

    projects.append(new_project)

    with open("projects.json", "w") as f:
        json.dump(projects, f, indent=4)

    print(f"\nProject '{Title}' added Successfully!\n")
    
def view_project():
    if not os.path.exists("projects.json"):
        print("\nNo projects added yet.\n")
        return

    try:
        with open("projects.json", "r") as f:
            projects_raw = json.load(f)
    except json.JSONDecodeError:
        projects_raw = []

    # Normalize all entries to avoid missing keys or wrong capitalization
    projects = []
    for p in projects_raw:
        if not isinstance(p, dict):
            continue
        projects.append({
            "title": p.get("title") or p.get("Title", "N/A"),
            "description": p.get("description") or p.get("Description", "N/A"),
            "technology": p.get("technology") or p.get("Technology", "N/A"),
            "github": p.get("github") or p.get("Github") or "N/A"
        })

    if not projects:
        print("\nNo projects added yet.\n")
        return

    print("\n--- All Projects ---")
    for idx, project in enumerate(projects, 1):
     if isinstance(project, dict):
        print(f"{idx}. {project.get('title','N/A')}")
        print(f"   Description : {project.get('description','N/A')}")
        print(f"   Technology  : {project.get('technology','N/A')}")
        print(f"   Github      : {project.get('github','N/A')}\n")
     else:
        print(f"{idx}. Invalid project entry\n")

def delete_project():
    if not os.path.exists("projects.json"):
        print("\nNo projects added yet.\n")
        return

    with open("projects.json", "r") as f:
        projects = json.load(f)

    if not projects:
        print("\nNo projects added yet.\n")
        return

    print("\n--- Delete Project ---")
    for idx, project in enumerate(projects, 1):
        print(f"{idx}. {project.get('title', 'N/A')}")

    try:
        choice = int(input("Enter project number to delete: "))
        if 1 <= choice <= len(projects):
            removed = projects.pop(choice - 1)
            with open("projects.json", "w") as f:
                json.dump(projects, f, indent=4)
            print(f"\n✅ Project '{removed.get('title', 'N/A')}' deleted successfully!\n")
        else:
            print("❌ Invalid number. No project deleted.\n")
    except ValueError:
        print("❌ Invalid input. Enter a number.\n")
        
        
def update_project():
    if not os.path.exists("projects.json"):
        print("\nNo projects added yet.\n")
        return

    with open("projects.json", "r") as f:
        projects = json.load(f)

    if not projects:
        print("\nNo projects added yet.\n")
        return

    print("\n--- Update Project ---")
    for idx, project in enumerate(projects, 1):
        print(f"{idx}. {project.get('title', 'N/A')}")

    try:
        choice = int(input("Enter project number to update: "))
        if 1 <= choice <= len(projects):
            selected = projects[choice - 1]

            # Prompt user with current values as default
            new_title = input(f"Enter new title [{selected.get('title', 'N/A')}]: ").strip()
            new_description = input(f"Enter new description [{selected.get('description', 'N/A')}]: ").strip()
            new_technology = input(f"Enter new technology [{selected.get('technology', 'N/A')}]: ").strip()
            new_github = input(f"Enter new GitHub URL [{selected.get('github', 'N/A')}]: ").strip()

            # Only update if input is not empty
            if new_title:
                selected['title'] = new_title
            if new_description:
                selected['description'] = new_description
            if new_technology:
                selected['technology'] = new_technology
            if new_github:
                selected['github'] = new_github

            with open("projects.json", "w") as f:
                json.dump(projects, f, indent=4)

            print(f"\n✅ Project '{selected.get('title', 'N/A')}' updated successfully!\n")
        else:
            print("❌ Invalid number. No project updated.\n")
    except ValueError:
        print("❌ Invalid input. Enter a number.\n")
        
        
        ####################### Experience ############################
def experience_manager():
    while True:
        print("\n--- Experience Manager ---")
        print("1. Add Experience")
        print("2. View Experience")
        print("3. Delete Experience")
        print("4. Update Experience")
        print("5. Back to Dashboard")

        choice = input("Enter choice: ")

        if choice == "1":
            add_experience()
        elif choice == "2":
            view_experience()
        elif choice == "3":
            delete_experience()
        elif choice == "4":
            update_experience()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")
            
def add_experience():
    company = input("Company: ").strip()
    role = input("Role: ").strip()
    duration = input("Duration: ").strip()
    description = input("Description: ").strip()

    if not os.path.exists("experience.json"):
        experiences = []
    else:
        with open("experience.json", "r") as f:
            experiences = json.load(f)

    new_exp = {
        "company": company,
        "role": role,
        "duration": duration,
        "description": description
    }
    experiences.append(new_exp)
    with open("experience.json", "w") as f:
        json.dump(experiences, f, indent=4)
    print(f"\nExperience at '{company}' added successfully!\n")

# --- View Experience ---
def view_experience():
    if not os.path.exists("experience.json"):
        print("\nNo experience added yet.\n")
        return
    with open("experience.json", "r") as f:
        experiences = json.load(f)
    if not experiences:
        print("\nNo experience added yet.\n")
        return
    
    print("\n--- All Experience ---")
    for idx, exp in enumerate(experiences, 1):
      company = exp.get("company", "N/A")
      role = exp.get("role", "N/A")
      duration = exp.get("duration", "N/A")
      description = exp.get("description", "N/A")
      print(f"{idx}. {company} | {role} | {duration}")
      print(f"   Description: {description}\n")
      
# --- Delete Experience ---
def delete_experience():
    view_experience()
    with open("experience.json", "r") as f:
        experiences = json.load(f)
    try:
        choice = int(input("Enter experience number to delete: "))
        if 1 <= choice <= len(experiences):
            removed = experiences.pop(choice - 1)
            with open("experience.json", "w") as f:
                json.dump(experiences, f, indent=4)
            print(f"✅ Deleted experience at '{removed['company']}'")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Enter a valid number.")

# --- Update Experience ---
def update_experience():
    view_experience()
    with open("experience.json", "r") as f:
        experiences = json.load(f)
    try:
        choice = int(input("Enter experience number to update: "))
        if 1 <= choice <= len(experiences):
            exp = experiences[choice-1]
            company = input(f"Company [{exp['company']}]: ").strip() or exp['company']
            role = input(f"Role [{exp['role']}]: ").strip() or exp['role']
            duration = input(f"Duration [{exp['duration']}]: ").strip() or exp['duration']
            description = input(f"Description [{exp['description']}]: ").strip() or exp['description']

            exp.update({"company":company,"role": role, "duration": duration, "description": description})
            with open("experience.json", "w") as f:
                json.dump(experiences, f, indent=4)
            print(f"✅ Updated experience at '{company}'")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Enter a valid number.")
        
        
################## Messages ##################################

def message_manager():
    while True:
        print("\n--- Message Manager ---")
        print("1. Add Message")
        print("2. View Messages")
        print("3. Delete Message")
        print("4. Back to Dashboard")

        choice = input("Enter choice: ")

        if choice == "1":
            add_message()
        elif choice == "2":
            view_messages()
        elif choice == "3":
            delete_message()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

# --- Add Message ---
def add_message():
    sender = input("Sender Email: ").strip()
    subject = input("Subject: ").strip()
    content = input("Message Content: ").strip()

    if not os.path.exists("messages.json"):
        messages = []
    else:
        with open("messages.json", "r") as f:
            messages = json.load(f)

    new_msg = {"sender": sender, "subject": subject, "content": content}
    messages.append(new_msg)

    with open("messages.json", "w") as f:
        json.dump(messages, f, indent=4)
    print("\nMessage added successfully!\n")

# --- View Messages ---
def view_messages():
    if not os.path.exists("messages.json"):
        print("\nNo messages yet.\n")
        return
    with open("messages.json", "r") as f:
        messages = json.load(f)
    if not messages:
        print("\nNo messages yet.\n")
        return
    
    print("\n--- All Messages ---")
    for idx, msg in enumerate(messages, 1):
     if not isinstance(msg, dict):
        continue
     sender = msg.get("sender", "N/A")
     subject = msg.get("subject", "N/A")
     content = msg.get("content", "N/A")
     print(f"{idx}. {sender} | {subject}")
     print(f"   Content: {content}\n")

# --- Delete Message ---
def delete_message():
    view_messages()
    with open("messages.json", "r") as f:
        messages = json.load(f)
    try:
        choice = int(input("Enter message number to delete: "))
        if 1 <= choice <= len(messages):
            removed = messages.pop(choice - 1)
            with open("messages.json", "w") as f:
                json.dump(messages, f, indent=4)
            print(f"✅ Deleted message from '{removed['sender']}'")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Enter a valid number.")
        
        
if __name__ == "__main__":   
    if login():  
      dashboard()
 

