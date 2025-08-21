# Employee Management System

This project is a Django-based application for managing employees, departments, and leave applications. It provides APIs for various functionalities related to employee management.

## Features

- Create and manage departments
- Create and manage employees
- Set base salaries for employees
- Update leave counts for employees
- Calculate payable salaries based on leave taken
- Retrieve high earners within the organization

## Project Structure

```
employee_management/
├── employee_management/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd employee_management
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## API Usage

- **Departments**
  - Create a department: `POST /api/departments/`
  - List all departments: `GET /api/departments/`

- **Employees**
  - Create an employee: `POST /api/employees/`
  - List all employees: `GET /api/employees/`
  - Update employee salary: `PATCH /api/employees/<id>/`
  - Retrieve high earners: `GET /api/employees/high-earners/`

- **Leave Applications**
  - Apply for leave: `POST /api/leaves/`
  - Update leave count: `PATCH /api/leaves/<id>/`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.