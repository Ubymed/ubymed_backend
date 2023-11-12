# Ubymed Backend 

## Description
 Backend code for the Ubymed project, providing APIs, data management, and authentication.


## Index
- [Technology stack](#technology-stack)
- [Recommended software](#recommended-software)
- [Project structure](#project-structure)
- [How to setup guide](#how-to-setup-guide)
- [How to use the API](#how-to-use-the-api)
- [Contribution](#contribution)
- [Contact](#contact)

## Technology Stack

- **Operating System**: The project was developed on macOS and tested on an Ubuntu server environment. Some adjustments may be needed to work on your environment.
- **Database**: PostgreSQL is used as the database management with the PostGIS extension for geospatial data support, to store and retrieve data efficiently.
- **Backend Framework**: The backend of this project is built with Django, a high-level Python web framework.
- **Code Language**: The project is written in Python.


## Recommended Software
The following software was used for the development of this project:

- **Postgres**: Full-featured PostgreSQL installation packaged as a standard Mac app. (Required)
- **Postgis**: Open source software program that adds support for geographic objects to the PostgreSQL database.
- **pgAdmin**: Used to easily manage PostgreSQL databases. (Optional)
- **Terminal**: Access to Command Line Interface. (Required)
- **Visual Studio Code**: Used to easily manage and edit code. (Optional)
- **Safari or Chrome**: To test browser access to the project. (Optional)
- **Postman**: To test API access to the project. (Optional)


## Project Structure
The project is organized with the following directory structure:

- `ubymed_backend/`: This directory contains the main application code.
  - `ubymed_backend/`: Configuration and general files for the project.
    - `settings.py/`: Configuration file for the project.
    - `urls.py/`: Project-wide URL routing.
    - `wsgi.py`: WSGI configuration for deployment.
  - `users/`: Contains Django models, views, serializers for handling users and authentication.
  - `partners/`: Contains Django models, views, serializers for handling partners.
  - `services/`: Contains Django models, views, serializers for handling services.
  - `orders/`: Contains Django models, views, serializers for handling orders.
  - `static/`: Stores static assets such as CSS, JavaScript, and images used in the application.


## How to Setup Guide
To test and work on this code you will need to:

1. Clone this repository.
2. Setup virtual environment
3. Install dependencies
4. Configure a database
5. Migrate to database
6. Run a development server


### Cloning Repository
To clone this repository, run the following command in your terminal:

```bash
git clone https://github.com/ubymed/ubymed_backend.git
```

### Setting up Virtual Environment
To test and work on this code, it's recommended to create a Python virtual environment using `venv`. If you're using Python 3.3 or later, you can create a virtual environment with the following commands:

```bash
python -m venv venv
```

Then activate the virtual environment:

```bash
source venv/bin/activate
```

Now, your development environment is isolated from the system Python, and you can install the project's dependencies inside the virtual environment.


### Installing Dependencies
Ensure that you have Python and pip installed on your system and that you virtual environment in active. Then, install the project's dependencies:

#### Ubuntu:
```bash
pip install -r requirements_ubuntu.txt
```

#### MacOS:
```bash
pip install -r requirements_macos.txt
```


### Database Configuration
This project uses PostgreSQL as the database with the PostGIS extension for geospatial data support. 
Ensure you have a configured PostgreSQL instance with PostGIS enabled and update the database configuration in `settings.py`.


### Migrations and Database Creation
Run migrations to create the database and necessary tables:

```bash
python manage.py makemigrations
python manage.py migrate
```


### Run the Development Server
To run the development server, use the following command:

```bash
python manage.py runserver
```
The server will be available at http://localhost:8000/.


## How to Use the API

### Making API Requests
To interact with the API, you can make HTTP requests using your preferred tool or programming language. Here are some basic examples:

- **Using cURL**:
  ```bash
  curl -X GET https://your-api-endpoint.com/resource
  ```

- **Using Python and requests library**:
  ```python
  import requests
  response = requests.get('https://your-api-endpoint.com/resource')
  data = response.json()
  ```

- **Using JavaScript and fetch**:
  ```js
  fetch('https://your-api-endpoint.com/resource')
  .then(response => response.json())
  .then(data => {
    // Handle data
  });
  ```


### API Documentation
To read more about API endpoints, urls and supported methods please refer to our detailed documentation:

- [Open Swagger Documentation](https://your-api-endpoint.com/swagger)
- [Open Redoc Documentation](https://your-api-endpoint.com/redoc)


## Contribution

If you'd like to contribute to the project, follow these steps:

1. Fork this repository.
2. Create a branch for your feature or bug fix: `git checkout -b my-feature`
3. Make your changes and commit: `git commit -m "Added my feature"`
4. Push to your branch: `git push origin my-feature`
5. Create a Pull Request on GitHub.


## Contact
If you have any questions or need assistance, feel free to get in touch at mflores@ubymed.com.
