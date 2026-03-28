# Portfolio Backend Management System

A modular **Portfolio Backend Management System** built using **Python** and **Object-Oriented Programming (OOP)** principles. This project provides an **Admin Dashboard** to manage portfolio data including **Skills, Projects, Experience, and Messages** using **JSON-based storage**.

This system is designed to simulate a **real-world backend architecture** with reusable components, modular design, and scalable structure.

---

# Features

## Admin Authentication

* Secure admin login system
* JSON-based credential storage
* Input validation and error handling
* Multiple login attempt protection

---

## Admin Dashboard

The system provides a centralized dashboard:

```
1. Manage Skills
2. Manage Projects
3. Manage Experience
4. View Messages
5. Exit
```

---

# Modules

## Skills Manager

* Add skills
* View skills
* Update skills
* Delete skills

---

## Projects Manager

* Add projects
* View projects
* Update projects
* Delete projects

---

## Experience Manager

* Add experience
* View experience
* Update experience
* Delete experience

---

## Messages Manager

* View user messages
* Delete messages

---

# Project Structure

```
Portfolio_backend/
│
├── backend.py
├── admin.json
├── skills.json
├── projects.json
├── experience.json
├── messages.json
└── README.md
```

---

# Architecture

## BaseManager Class

The project follows **OOP inheritance** using a reusable `BaseManager` class.

### BaseManager Responsibilities

* Load data from JSON
* Save data to JSON
* Add new records
* Update existing records
* Delete records
* View records

All modules inherit from **BaseManager**:

* SkillManager
* ProjectManager
* ExperienceManager
* MessageManager

This improves:

* Code Reusability
* Maintainability
* Scalability
* Clean Architecture

---

# Technologies Used

* Python
* Object-Oriented Programming
* JSON Data Storage
* CLI Based Dashboard
* Git & GitHub

---

# Python Concepts Implemented

* Classes & Objects
* Inheritance
* Encapsulation
* Modular Programming
* File Handling
* JSON Handling
* Exception Handling
* CRUD Operations

---

# Installation & Usage

## Clone Repository

```
git clone https://github.com/Nadiayousaf/Portfolio_backend.git
```

## Navigate to Project

```
cd Portfolio_backend
```

## Run Project

```
python backend.py
```

---

# Example Workflow

1. Admin Login
2. Open Dashboard
3. Select Module
4. Perform CRUD Operations
5. Data Stored in JSON Files

---

# Future Improvements

* Decorators Implementation
* Logging System
* Input Validation
* REST API using Flask
* Database Integration (SQLite / MySQL)
* Frontend Integration

---

# Project Purpose

This project was developed to:

* Practice Advanced Python Concepts
* Implement OOP Architecture
* Build Portfolio Backend System
* Strengthen Backend Development Skills

---

# Author

**Nadia Yousaf**
Python Developer
Computer Science Student

---

# Version

**Version 1.0 — OOP Portfolio Backend System**

---

# Status

Completed
Flask version improvements planned
