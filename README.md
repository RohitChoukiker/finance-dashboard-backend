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


## Auth Module

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
The project is fully tested using pytest:
- Auth module tests
- Transactions module tests
- Dashboard tests
- CRUD operations
- Validation checks

# Design Decisions
- Used UUID for scalable user identification
- Implemented RBAC for secure access control
- Modular architecture for maintainability
- Dependency-based authorization for clean code


## Transactions Module (Detailed)

The Transactions module manages financial records including income and expenses with full CRUD functionality, filtering, sorting, and audit logging.

# Features
- Create income and expense transactions
- Update and delete transactions
- Fetch transactions with pagination
- Filter by type (income / expense)
- Search by category or description
- Sort transactions (amount, created_at)
- Category-based validation
- Audit logging for all actions
- Role-based data access

# Transaction Types
- income
- expense

# Categories

## Income
- salary

## Expense
- food
- travel
- shopping
- rent
- bills
- health
- entertainment

# API Endpoints

## Transactions
- POST   /transactions                      → Create transaction
- GET    /transactions                      → Get all transactions (with filters)
- GET    /transactions/{transaction_id}     → Get single transaction
- PUT    /transactions/{transaction_id}     → Update transaction
- DELETE /transactions/{transaction_id}     → Delete transaction

## Query Parameters
- type (income / expense)
- search (text search)
- sort_by (amount / created_at)
- order (asc / desc)
- page (pagination)
- limit (number of records)

# Validation Rules
- Category must match transaction type
- Category is optional
- Invalid category throws error
- Pagination limit is restricted

# Audit Logging
All transaction actions are logged:

- CREATE_TRANSACTION
- UPDATE_TRANSACTION
- DELETE_TRANSACTION

Each log stores:
- user_id
- action
- entity
- entity_id
- metadata

# Design Decisions
- Used enums for type safety
- Implemented filtering, sorting, and pagination for scalability
- Clean separation of service and repository layers
- Added audit logs for traceability

## Dashboard Module 

Provides aggregated financial insights for users.

# Features
- Total income and expense calculation
- Balance calculation
- Category-wise breakdown with percentage
- Monthly trends

# API Endpoints
- GET /transactions/dashboard/summary   → Overall summary
- GET /transactions/dashboard/category  → Category breakdown
- GET /transactions/dashboard/monthly   → Monthly trends

# Design Decisions
- Used aggregation queries for performance
- Optimized grouping using SQL functions


The goal is to demonstrate strong backend engineering fundamentals and clean architecture.

## Author
Rohit Choukiker
