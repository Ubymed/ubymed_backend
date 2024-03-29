# Ubymed Backend 

## Description
Backend code for the Ubymed project, providing APIs, data management, and authentication.

## Status
Active Development

## Table of Contents
- [Built With](#built-with)
- [Getting Started](#getting-started)
- [Project structure](#project-structure)
- [Run local server](#run-local-server)
- [Run remote server](#run-remote-server)
- [How to use the API](#how-to-use-the-api)
- [Contribution](#contribution)
- [Contact](#contact)

## Built With

- **Operating System**: The project was developed on macOS and tested on an Ubuntu server environment. Some adjustments may be needed to work on your environment.
- **Database**: PostgreSQL is used as the database management with the PostGIS extension for geospatial data support, to store and retrieve data efficiently.
- **Backend Framework**: The backend of this project is built with Django, a high-level Python web framework.
- **Code Language**: The project is written in Python.


## Getting Started

### Prerequisites
Before you start, ensure you have the following software installed in your machine:
- **Terminal**: Access to Command Line Interface.
- **Postgres (v16.1 or later)**: Full-featured PostgreSQL installation packaged as a standard Mac app.
- **Postgis (v3.4.0 or later)**: Open source software program that adds support for geographic objects to the PostgreSQL database.
- **Gunicorn (v21.2.1 or later)**: Web server gateway interface (WSGI) server for running Python web applications.
- **Nginx (v1.18.0 or later)**: High-performance web server and reverse proxy server.

### Recommended tools
The following software was used for the development of this project:
- **pgAdmin**: Used to easily manage PostgreSQL databases. (Optional)
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


## Run Local Server
To test and work on this code you will need to:

1. Clone this repository.
2. Setup virtual environment
3. Install dependencies
4. Configure a database
5. Migrate to database
6. Run server


### 1. Cloning Repository
To clone this repository, run the following command in your terminal:

```bash
git clone https://github.com/ubymed/ubymed_backend.git
```

### 2. Setting up Virtual Environment
To test and work on this code, it's recommended to create a Python virtual environment using `venv`. If you're using Python 3.3 or later, you can create a virtual environment with the following commands:

```bash
python -m venv venv
```

Then activate the virtual environment:

```bash
source venv/bin/activate
```

Now, your development environment is isolated from the system Python, and you can install the project's dependencies inside the virtual environment.

### 3. Installing Dependencies
Ensure that you have Python and pip installed on your system and that you virtual environment in active. Then, install the project's dependencies:

#### MacOS:
```bash
pip install -r requirements_macos.txt
```

### 4. Database Configuration
This project uses PostgreSQL as the database with the PostGIS extension for geospatial data support. 
Ensure you have a configured PostgreSQL instance with PostGIS enabled and update the database configuration in `settings.py`.

### 5. Migrations and Database Creation
Run migrations to create the database and necessary tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run Server
To run the development server, use the following command:

```bash
python manage.py runserver
```
The server will be available at http://localhost:8000/.



## Run Remote Server
To run a remote server you will need to:

1. Connect to remote server via SSH.
2. Clone this repository.
3. Setup virtual environment
4. Install dependencies
5. Configure a database
6. Migrate to database
7. Collect static files
8. Install Gunicorn
9. Install Nginx
10. Run server


### 1. Connect to remote server via SSH
For this step you should already have a remote server configured, and access it through SSH. We used Amazon Web Services and an Ubuntu Server for development.

### 2. Cloning Repository
To clone this repository, run the following command in your terminal:

```bash
git clone https://github.com/ubymed/ubymed_backend.git
```

### 3. Setting up Virtual Environment
To test and work on this code, it's recommended to create a Python virtual environment using `venv`. If you're using Python 3.3 or later, you can create a virtual environment with the following commands:

```bash
python -m venv venv
```

Then activate the virtual environment:

```bash
source venv/bin/activate
```

Now, your development environment is isolated from the system Python, and you can install the project's dependencies inside the virtual environment.


### 4. Installing Dependencies
Ensure that you have Python and pip installed on your system and that you virtual environment in active. Then, install the project's dependencies:

#### Ubuntu:
```bash
pip install -r requirements_ubuntu.txt
```

### 5. Database Configuration
This project uses PostgreSQL as the database with the PostGIS extension for geospatial data support. 
Ensure you have a configured PostgreSQL instance with PostGIS enabled and update the database configuration in `settings.py`.

### 6. Migrations and Database Creation
Run migrations to create the database and necessary tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Collect Static Files
To work in a remote server you have to collect static files. To do that do the following:

Edit the following line in `settings.py`

```python
STATIC_URL = '/static/'
```

Run the following command to collect static files in the defines directory:

```bash
python manage.py collectstatic
```

### 8. Install Gunicorn

To install Gunicorn run:

```bash
pip install gunicorn
```

### 9. Install and Configure Nginx

To install Nginx run:

```bash
sudo apt-get install nginx
```

Configure Nginx by editing the file `/etc/nginx/sites-available/default.txt` to:

```txt
server {
    listen 80;
    server_name your_domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;  # Replace with your Gunicorn host and port
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    location /static/ {
                alias /static/;
    }
}
```

### 10. Run Server

Configure the application as a service with systemd. To do this create a file called `ubymed_backend.service` in `/etc/systemd/system/` containing:

```ini
[Unit]
Description=Gunicorn instance to serve ubymed_backend
After=network.target

[Service]
User=usuario_de_tu_app
Group=grupo_de_tu_app
WorkingDirectory=/ruta/a/tu/app
ExecStart=/ruta/a/tu/app/venv/bin/gunicorn --workers=3 --bind=0.0.0.0:8000 tu_app.wsgi:application

[Install]
WantedBy=multi-user.target
```

Reload systemd:

```bash
sudo systemctl daemon-reload
```

Enable new application service:

```bash
sudo systemctl enable ubymed_app
```



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

- [Open Swagger Documentation](https://api.ubymed.com/swagger)
- [Open Redoc Documentation](https://api.ubymed.com/redoc)



## Contribution

If you'd like to contribute to the project, follow these steps:

1. Fork this repository.
2. Create a branch for your feature or bug fix: `git checkout -b my-feature`
3. Make your changes and commit: `git commit -m "Added my feature"`
4. Push to your branch: `git push origin my-feature`
5. Create a Pull Request on GitHub.



## Contact
If you have any questions or need assistance, feel free to get in touch at mflores@ubymed.com.
