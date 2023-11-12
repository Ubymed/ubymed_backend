# ubymed_backend

## Description
 Backend code for the Ubymed project, providing APIs, data management, and authentication.

## Setup Guide
To test and work on this code you will need to:

1. Clone this repository.
2. Install dependencies
3. Configure a database
4. Migrate to database
5. Run a development server

### Cloning Repository
To clone this repository, run the following command in your terminal:

```bash
git clone https://github.com/ubymed/ubymed_backend.git
```
### Installing Dependencies
Ensure that you have Python 3 and pip installed on your system. Then, install the project's dependencies:

```bash
pip install -r requirements.txt
```

### Database Configuration
This project uses PostgreSQL as the database. Ensure you have a configured PostgreSQL instance and update the database configuration in `settings.py`.

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

## Project Structure

## Contribution

If you'd like to contribute to the project, follow these steps:

1. Fork this repository.
2. Create a branch for your feature or bug fix: `git checkout -b my-feature`
3. Make your changes and commit: `git commit -m "Added my feature"`
4. Push to your branch: `git push origin my-feature`
5. Create a Pull Request on GitHub.