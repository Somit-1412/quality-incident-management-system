# Quality Incident Management System

## Project Objective

The objective of this project is to develop a role-based quality incident management system with workflow lifecycle management, validation rules, resilience simulation, audit logging, and reporting capabilities.

The project simulates a simplified enterprise incident management workflow similar to systems used in quality engineering and operational monitoring environments.

---

# Features Implemented

## Incident Management
- Create incidents
- View incidents
- Incident detail page
- Workflow lifecycle tracking

## Role-Based Access Control (RBAC)
- Reporter role
- Reviewer role
- Admin role
- Restricted workflow actions

## Workflow Lifecycle
Incident workflow follows:

```text
New
↓
In Review
↓
Assigned
↓
Resolved
↓
Closed
```

Invalid workflow transitions are blocked.

---

# Validation Rules
- Mandatory title validation
- Duplicate incident prevention
- Severity validation
- Restricted status movement validation

---

# Audit Logging
The system tracks:
- Incident creation
- Status changes
- Workflow activities
- Timestamped audit history

---

# Filtering and Search
The dashboard supports filtering by:
- Severity
- Status

---

# Reporting Dashboard
The reporting module provides:
- Total incidents
- Open incidents
- Closed incidents
- Severity distribution

---

# Resilience Simulation
The project simulates backend degradation by introducing artificial delay for Critical incidents.

This demonstrates basic resilience and failure simulation concepts.

---

# Technologies Used

| Component | Technology |
|---|---|
| Backend | Flask |
| Frontend | HTML + Bootstrap |
| Database | SQLite |
| ORM | SQLAlchemy |
| IDE | VS Code |
| Version Control | Git + GitHub |

---

# Project Structure

```text
Quality-Incident-Management/
│
├── app.py
├── requirements.txt
├── instance/
├── templates/
├── static/
├── screenshots/
├── reports/
├── README.md
├── issue-log.docx
└── final-report.docx
```

---

# Installation Steps

## 1. Clone Repository

```bash
git clone <repository-url>
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

---

## 3. Activate Virtual Environment

### PowerShell

```bash
.venv\Scripts\Activate.ps1
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# Key Concepts Demonstrated
- Workflow management
- RBAC implementation
- Audit trail tracking
- Validation handling
- ORM usage
- Database persistence
- Dashboard reporting
- Resilience simulation
- Incident lifecycle management

---

# Conclusion

The project successfully demonstrates a mini enterprise-style quality incident management system with role-based workflow handling, audit tracking, reporting, validation enforcement, and operational monitoring concepts.