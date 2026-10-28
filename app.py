
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
import socket

app = Flask(__name__)

DB_PATH = os.environ.get(
    "NOTES_DB",
    "/var/lib/notes-app/notes.db"
)

SERVER_NAME = socket.gethostname()


def get_db():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_db():
    with get_db() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


initialize_db()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        if title and content:
            with get_db() as connection:
                connection.execute(
                    "INSERT INTO notes (title, content) VALUES (?, ?)",
                    (title, content)
                )

        return redirect(url_for("index"))

    with get_db() as connection:
        notes = connection.execute(
            "SELECT * FROM notes ORDER BY id DESC"
        ).fetchall()

    return render_template(
        "index.html",
        notes=notes,
        server_name=SERVER_NAME
    )


@app.route("/delete/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    with get_db() as connection:
        connection.execute(
            "DELETE FROM notes WHERE id = ?",
            (note_id,)
        )

    return redirect(url_for("index"))


@app.route("/health")
def health():
    return {
        "status": "ok",
        "server": SERVER_NAME
    }


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
