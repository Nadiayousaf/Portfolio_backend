### Admin Login
import json
import os
def login():
    
    if not os.path.exists("admin.json"):
        print("Admin file not found! Please create admin.json first.")
        return False
     # admin is a dictionary: {"username": "...", "password": "..."}
    with open("admin.json", "r") as f:
     try:
        admin = json.load(f)
     except json.JSONDecodeError:
        print("Error: admin.json is empty or invalid JSON.")
        return False
    
    username=input("Enter Username: ")
    password=input("Enter password: ")
    attempts=3
    while attempts>0:
        if username==admin["username"] and password==admin["password"]:
            print("Login SuccessFULl")
            return True
        else:
            attempts-=1
            print(f"Invalid login! Attmpts left :{attempts}\n")
            
    print("Too many Attempts, Attempt failed!")
    

def dashboard():
    while True:
        print("1. Manage Skills")
        print("2. Manage Projects")
        print("3. Manage Experience")
        print("4. View Messages")
        print("5. Exit! ")
        
        choice=input("Enter Choice: ")
        if choice=="1":
            skills_manager()
        elif choice=="2":
            print("Project Manager")
        elif choice=="3":
            print("Experience Manager")
        elif choice=="4":
            print("Message Section ")
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

if __name__ == "__main__":   
    if login():  
      dashboard()
 