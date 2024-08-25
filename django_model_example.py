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


# Create the table
if not Employee.objects.exists():
    Employee.objects.create(fname="John",
                            lname="Doe",
                            email="john@example.com",
                            mobile="1234567890",
                            password="securepassword")

# CRUD operations
# Create
employee = Employee.objects.create(fname="Jane",
                                   lname="Doe",
                                   email="jane@example.com",
                                   mobile="0987654321",
                                   password="securepassword")

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
