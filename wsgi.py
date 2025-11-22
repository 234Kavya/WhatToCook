from app import app

# This is the entry point for production servers (gunicorn, etc.)
application = app

if __name__ == "__main__":
    app.run()
