# Lightweight Feature Flag Service

A centralized feature flag management service built with Python, FastAPI, and SQLite.

This system allows development teams to enable, disable, and gradually roll out features to users without redeploying their applications.

---

# Overview

Modern applications often need to release features safely and progressively. Instead of deploying code directly to all users, this service provides remote configuration controls that determine which users can access specific features.

The service supports:

- Feature flag creation and management
- User-specific targeting
- Percentage-based rollouts
- Global kill switches
- Audit logging
- Client-side feature evaluation

---

# Features

## Admin API

Manage feature flags through REST endpoints.

Supported operations:

- Create flags
- Update flags
- Delete flags
- View all flags

Each flag contains:

- Name
- Description
- Enabled/disabled status
- Percentage rollout
- Targeted users
- Kill switch state

---

## Percentage Rollouts

Flags can be enabled for a percentage of users.

Example:

- 30% rollout
- 50% rollout
- 100% rollout

The rollout system uses deterministic hashing to ensure:

- The same user always receives the same result
- Users do not randomly switch between enabled/disabled states

---

## User Targeting

Enable features for specific users.

Example:

```json
{
  "targeted_users": ["1001", "1002"]
}
```

Useful for:

- Internal testing
- Beta users
- QA validation
- VIP access

---

## Kill Switch

Emergency global disable for any feature flag.

Even if rollout rules exist, the kill switch overrides everything and disables the feature instantly.

Useful for:

- Production incidents
- Bug mitigation
- Safe rollbacks

---

## Audit Logging

Every change is recorded with:

- Flag name
- Action performed
- Who made the change
- Timestamp
- Previous state
- New state

This provides traceability and operational visibility.

---

# Tech Stack

- Python 3.14.5
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

---

# Project Structure

```text
feature-flag-service/
│
├── app.py
├── database.py
├── evaluator.py
├── models.py
├── schemas.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/rlin1214/Lightweight-Feature-Flag-Service.git
```

## Enter Project Folder

```bash
cd Lightweight-Feature-Flag-Service
```

---

# Create Virtual Environment

## Windows PowerShell

```powershell
python -m venv venv
```

Activate:

```powershell
venv\Scripts\activate
```

---

# Install Dependencies

```powershell
pip install -r requirements.txt
```

---

# Run The Server

```powershell
uvicorn app:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates Swagger UI documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Example API Usage

## Create Feature Flag

### POST

```text
/admin/flags?changed_by=ray
```

### Request Body

```json
{
  "name": "dark_mode",
  "description": "dark mode feature",
  "enabled": true,
  "kill_switch": false,
  "rollout_percentage": 30,
  "targeted_users": ["1001"]
}
```

---

## Evaluate Flags For User

### GET

```text
/client/flags/1001
```

### Response

```json
{
  "user_id": "1001",
  "flags": {
    "dark_mode": true
  }
}
```

---

# How Feature Evaluation Works

The evaluation engine follows this order:

1. Check kill switch
2. Check if flag enabled
3. Check targeted users
4. Check rollout percentage
5. Return final decision

---

# Deterministic Rollouts

The system hashes user IDs to produce stable rollout buckets.

Example:

```text
hash(user_id) % 100
```

This ensures:

- Consistent user experience
- Reliable testing
- Predictable rollouts

---

# Future Improvements

Potential production-grade improvements:

- PostgreSQL support
- JWT authentication
- Redis caching
- Role-based access control
- SDK support
- WebSocket updates
- Metrics and monitoring
- Environment separation
- Multivariate flags
- A/B testing

---

# License

This project is for educational and portfolio purposes.
