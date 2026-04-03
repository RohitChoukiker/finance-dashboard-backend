#  Finance Dashboard Backend 

A role-based backend system for managing financial records and generating dashboard analytics.
This project demonstrates clean backend architecture, access control, and data aggregation.

---

##  Overview

This backend system allows users to manage financial transactions and view insights based on their role.

The system supports:

* User authentication and role management
* Financial record CRUD operations
* Dashboard analytics (income, expense, trends)
* Role-based access control

---

## Architecture

The project follows a **modular layered architecture** to ensure clean separation of concerns:

```
Request → Router → Controller → Service → Repository → Database
```

###  Modules

* **Auth Module** - Authentication & user handling
* **Transactions Module** - Financial records management
* **Dashboard Module** - Aggregated analytics

---

##  Role-Based Access Control

| Role    | Permissions              |
| ------- | ------------------------ |
| Viewer  | Read-only access to data |
| Analyst | View records + analytics |
| Admin   | Full CRUD access         |

Access is enforced using FastAPI dependencies.ess control rather than UI.
The goal is to demonstrate strong backend engineering fundamentals and clean architecture.

# Author
# Rohit Choukiker
