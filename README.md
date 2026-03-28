

# Python Portfolio Backend Admin Dashboard

A **Python-based Admin Dashboard Backend** designed to manage dynamic portfolio content including **Skills, Projects, Experience, and Messages** using **JSON as a lightweight database**.

This project serves as the **backend foundation** for a future **Full-Stack Portfolio Website** using Flask.

---

# Project Purpose

This project was built to:

* Practice Python backend development
* Implement CRUD operations
* Work with JSON as a database
* Build admin panel logic
* Prepare backend for Flask integration
* Create a professional portfolio project

---

# Features

## Admin Authentication

* Secure admin login
* Credential storage using JSON
* Login validation
* Error handling for invalid credentials

---

## Skills Management

Admin can:

* Add new skills
* View skills
* Update skills
* Delete skills

Example:

```json
{
  "skill": "Python",
  "level": "Advanced",
  "category": "Programming"
}
```

---

## Projects Management

Admin can:

* Add projects
* View projects
* Update projects
* Delete projects

Example:

```json
{
  "title": "Portfolio Website",
  "description": "Personal portfolio project",
  "technologies": "HTML, CSS, JavaScript",
  "github": "github link"
}
```

---

## Experience Management

Admin can:

* Add experience
* View experience
* Update experience
* Delete experience

Example:

```json
{
  "company": "Tech Company",
  "role": "Python Developer",
  "duration": "2024-Present",
  "description": "Worked on backend development"
}
```

---

## Messages Management

Admin can:

* View messages
* Delete messages
* Store contact form messages

Example:

```json
{
  "name": "User Name",
  "email": "user@email.com",
  "message": "Hello, I want to collaborate"
}
```

---

# Technologies Used

* Python 3
* JSON (Lightweight Database)
* File Handling
* CRUD Operations
* CLI Admin Dashboard
* Git
* GitHub

---

# Project Architecture

```
Admin Login
     │
     ▼
Dashboard Menu
     │
     ├── Skills CRUD
     ├── Projects CRUD
     ├── Experience CRUD
     └── Messages CRUD
```

---

# Project Structure

```
portfolio_backend/
│
├── main.py
├── admin.json
├── skills.json
├── projects.json
├── experience.json
├── messages.json
└── README.md
```

---

# JSON Database Files

| File            | Purpose           |
| --------------- | ----------------- |
| admin.json      | Admin credentials |
| skills.json     | Skills data       |
| projects.json   | Projects data     |
| experience.json | Experience data   |
| messages.json   | Contact messages  |

---

# How to Run Project

### Clone Repository

```
git clone https://github.com/yourusername/portfolio_backend.git
```

---

### Navigate to Folder

```
cd portfolio_backend
```

---

### Run Project

```
python main.py
```

---

# Key Concepts Implemented

* Python File Handling
* JSON Data Storage
* CRUD Operations
* Admin Authentication
* Error Handling
* Modular Backend Design
* CLI Based Dashboard

---

# Errors Faced & Solutions

## JSONDecodeError

Problem:
Empty JSON file

Solution:
Used try-except

```
try:
    data = json.load(file)
except:
    data = []
```

---

## Missing Keys Error

Problem:
Different key names in JSON

Solution:
Used `.get()` method

```
data.get("company", "N/A")
```

---

## Remote Origin Already Exists

Problem:
Git remote already connected

Solution:
Skipped remote creation and pushed changes

---

# Learning Outcomes

This project helped in learning:

* Backend logic building
* Data persistence
* Admin panel architecture
* Debugging techniques
* Git version control
* Clean code structure

---

# Future Improvements

This project will be enhanced with:

## Advanced Python Features

* Input validation
* Search functionality
* Sorting functionality
* Duplicate prevention
* Password hashing
* Modular architecture

---

## Backend Improvements

* Database integration (SQLite / MySQL)
* API development
* REST architecture

---

## Flask Integration

Convert CLI to Web Application:

* Flask routes
* HTML templates
* Form handling
* API integration

---

# Project Roadmap

| Version   | Description                  |
| --------- | ---------------------------- |
| Version 1 | Python CLI Admin Dashboard   |
| Version 2 | Advanced Python Features     |
| Version 3 | Flask Backend                |
| Version 4 | Full Stack Portfolio Website |

---

# Project Status

Version 1 Completed
Currently Upgrading to Advanced Concepts

---

# Why This Project Matters

This project demonstrates:

* Real backend development
* CRUD operations
* Data persistence
* Admin panel architecture
* Professional Git workflow

This is a **portfolio-ready backend project**.

---

# Author

Nadia Yousaf
Python Developer
Full Stack Learner

