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

Access is enforced using FastAPI dependencies.


# Auth Module (Detailed)

The Auth module provides a complete authentication and user management system with role-based access control.

# Features
- User Signup with validation
- Secure Login using JWT
- Password hashing using bcrypt
- Role-based access control (RBAC)
- Admin user auto-seeding on startup
- User management APIs (Admin only)
- Account activation and deactivation
- UUID-based user identification
- Fully tested using pytest

# Authentication Flow
User Signup → Store hashed password → Login → Generate JWT → Access protected routes

# JWT Token
Token contains:
- user email (sub)
- user role

Used for authentication in protected routes

Example:
Authorization: Bearer <token>

# API Endpoints

## Authentication
- POST /auth/signup       → Register new user
- POST /auth/login        → Login and get JWT token
- GET  /auth/me           → Get current user details

## User Management (Admin Only)
- GET  /auth/users                 → Get all users
- GET  /auth/users/count           → Get total users count
- PUT  /auth/users/{user_id}/role  → Change user role
- PUT  /auth/users/{user_id}/status → Activate/Deactivate user

# User Model
- id (UUID)
- name
- email
- password (hashed)
- role (admin / analyst / viewer)
- is_active (boolean)

# Security Features
- Password hashing using bcrypt
- JWT-based authentication
- Role-based authorization
- Restricted admin endpoints
- Inactive user login blocked

# Testing
Auth module is fully tested using pytest:
- Signup flow
- Login flow
- JWT validation
- Protected routes
- Admin APIs (users, role, status)

# Design Decisions
- Used UUID for scalable user identification
- Implemented RBAC for secure access control
- Modular architecture for maintainability
- Dependency-based authorization for clean code



The goal is to demonstrate strong backend engineering fundamentals and clean architecture.

# Author
# Rohit Choukiker
