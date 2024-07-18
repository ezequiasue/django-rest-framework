
# Django Rest Framework 
Working with Django Rest Framework

This project demonstrates the basic usage of Django Rest Framework to create a simple API for managing books.

## Prerequisites

Before you begin, make sure you have Python and Poetry installed on your system.


Step-by-Step Guide to Creating a Django Rest Framework Project
1. Install Required Tools
Make sure you have Python and Poetry installed on your system.

Python: Version 3.6 or higher

Poetry: Dependency management and virtual environment tool for Python.

To install Poetry, run the following command:

```bash
curl -sSL https://install.python-poetry.org | python -
```
2. Create a Django Project
Open a terminal and navigate to the directory where you want to create your project.

```bash
# Create a new Django project named 'bookstore'
django-admin startproject bookstore
cd bookstore
```

3. Set Up a Django Application (API)
Create a Django app named api within your project.

```bash
python manage.py startapp API
```
4. Configure Django Rest Framework
Install Django Rest Framework using Poetry.

```bash
poetry add djangorestframework
```

5. Configure Django Settings
In your settings.py file (bookstore/settings.py), add 'rest_framework' to INSTALLED_APPS:

```bash
INSTALLED_APPS = [
    # Other apps
    'rest_framework',
    'api',  # Your API app
]
```


**Usage**

**Models**

The project includes a simple model for Book:

- **Book**:
- `title` (CharField): Title of the book.
- `author` (CharField): Author of the book.
- `published_date` (DateField): Publication date of the book.
- `isbn` (CharField): ISBN of the book.

### Usage Examples

#### List all books

Send a GET request to `/books/` to retrieve a list of all books.

#### Create a new book

Send a POST request to `/books/` with JSON data for the book:”

**json code**

`{ "title": "Example Book",
 "author": "Book Author",
  "published_date": "2024-07-18",
   "isbn": "1234567890123" }`”

![image](https://github.com/user-attachments/assets/654516dd-63ac-4a12-9918-26616ced6737)

![image](https://github.com/user-attachments/assets/2620a9fd-3994-4c2c-9c37-0a75541821df)

![image](https://github.com/user-attachments/assets/e9766532-f0cc-4125-8bae-c2c93161755a)

**json code**
![image](https://github.com/user-attachments/assets/c482af67-1362-43c5-93db-88df9c5ec7af)



Now, the README.md includes an example of how to make a POST request using cURL to create a new book in the Django Rest Framework API.
