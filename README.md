# Category Post Project Setup Guide

This Flask project requires proper environment setup and database configuration to run correctly.

## Prerequisites

- Python 3.7 or higher
- PostgreSQL installed and running
- pip (Python package installer)

## Setup Instructions

### 1. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Database Setup

#### Create PostgreSQL Database

1. Create the database:
```sql
CREATE DATABASE 0304;
```

2. Exit PostgreSQL:
```sql
\q
```

#### Initialize Database Tables

1. Open Flask shell:
```bash
flask shell
```

2. Create all database tables:
```python
from app import db
db.create_all()
exit()
```

### 4. Run the Application

```bash
flask run
```

The application will be available at http://127.0.0.1:5000
