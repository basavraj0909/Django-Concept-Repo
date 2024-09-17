# Django Employee Management System

This project demonstrates how to set up and use a simple Django model, `Employee`, with SQLite as the database. It includes basic CRUD (Create, Read, Update, Delete) operations in a Python script.

## Prerequisites

- Python 3.x
- Django 3.x or later

## Setup

1. **Clone the repository** or create a directory for your project:

    ```bash
    mkdir django_crud_example
    cd django_crud_example
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Django**:

    ```bash
    pip install django
    ```

4. **Create the `Employee` model and run migrations**:

    Since this example uses SQLite and is run as a script, no migrations are required upfront. The table will be created when the script is executed.

## Running the Script

The script sets up a Django environment in a standalone Python script and includes the following:

- **Model Setup**: Defines the `Employee` model with fields for first name, last name, email, mobile number, and password.
- **CRUD Operations**:
  - **Create**: Adds a new employee record.
  - **Read**: Retrieves all employee records.
  - **Update**: Modifies an employee record.
  - **Delete**: Removes an employee record.

### Example Script

Below is the core script (`app.py`) that handles the setup and CRUD operations:

```python
import os
import django
from django.conf import settings
from django.db import models

# Django setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    },
    INSTALLED_APPS=[
        '__main__',
    ],
)

django.setup()

# Django model definition
class Employee(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.fname} {self.lname}'

# Create the table if not exists
if not Employee.objects.exists():
    Employee.objects.create(
        fname="John",
        lname="Doe",
        email="john@example.com",
        mobile="1234567890",
        password="securepassword"
    )

# CRUD operations
# Create
employee = Employee.objects.create(
    fname="Jane",
    lname="Doe",
    email="jane@example.com",
    mobile="0987654321",
    password="securepassword"
)

# Read
print("All Employees:")
for emp in Employee.objects.all():
    print(emp)

# Update
employee.fname = "Jane Updated"
employee.save()
print("Updated Employee:", Employee.objects.get(id=employee.id))

# Delete
employee.delete()
print("After Deletion:")
for emp in Employee.objects.all():
    print(emp)
