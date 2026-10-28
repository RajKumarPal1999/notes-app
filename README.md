
# Linux Notes Web Application

A simple Notes web application deployed on an Ubuntu EC2 instance.

## Technologies Used

- Linux (Ubuntu)
- Python
- Flask
- SQLite
- Gunicorn
- Nginx
- systemd
- Git and GitHub

## Features

- Create and view notes
- Delete saved notes
- Store notes in an SQLite database
- Display the server hostname
- Run the Flask application as a systemd service
- Use Nginx as a reverse proxy

## Project Structure

```text
notes-app-repo/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── templates/
    └── index.html
```

## Local Setup

1. Install Python 3 and create a virtual environment.
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the directory `/var/lib/notes-app/` exists
   and is writable by the application user, or set the
   `NOTES_DB` environment variable to a writable database path.
4. Run the application:

   ```bash
   python app.py
   ```

The application listens on `127.0.0.1:5000` when
started directly. For EC2 deployment, use Gunicorn
and configure Nginx as a reverse proxy.

## Security Notes

This is a learning project. Add authentication, CSRF
protection, HTTPS, and appropriate backup procedures
before using it with real users.
