## Company API
A Django REST API project for managing companies and their employees. This project provides robust CRUD operations via RESTful endpoints, built using Django 5 and Django REST Framework.

Features
Manage companies and their employees with full CRUD support

Organized RESTful endpoints

Serialization of models using DRF

Easy extension and flexible structure

Simple test coverage for basic app functionality

## Project Structure
companyapi/
├── api/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serilizers.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
├── companyapi/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py

## Models
### Company
companyid: AutoField (PK)

name: CharField

location: CharField

about: TextField

type: CharField (choices: IT, Non IT, Mobile Phones)

addeddate: DateField (auto-add)

active: BooleanField

### Employees
name, email, address, phone, about: Various CharField/TextField

position: CharField (choices: Manager, Software Developer, Project Leader)

companyId: ForeignKey (to Company)

## Endpoints
API Root
All API endpoints are accessible under /apiv1/.

## Companies
Method	Endpoint	Action
GET	/companies/	List all companies
POST	/companies/	Create a company
GET	/companies/<id>/	Retrieve company by ID
PUT	/companies/<id>/	Update company by ID
DELETE	/companies/<id>/	Delete company by ID
GET	/companies/<id>/employees/	List employees for a company
Employees
Method	Endpoint	Action
GET	/employees/	List all employees
POST	/employees/	Create an employee
GET	/employees/<id>/	Retrieve employee by ID
PUT	/employees/<id>/	Update employee by ID
DELETE	/employees/<id>/	Delete employee by ID

## Installation

Clone the repository.

Ensure you have Python 3.10+ and pip.

Install dependencies:
pip install django djangorestframework
Apply migrations:

python manage.py migrate
Run the server:

python manage.py runserver
Access the API at: http://127.0.0.1:8000/apiv1/

## Testing
Basic testing is set up using Django's TestCase in tests.py.

Extend to add your own test cases as needed.

## Configuration
Project settings can be found and adjusted in companyapi/settings.py.

Default database is SQLite (db.sqlite3), but you can configure a different backend.

## Admin Panel
Register models in admin.py for admin access.

## Run:
python manage.py createsuperuser
Then log in via /admin/.

## License
This project is for education and demonstration purposes.