# Start the Gunicorn server
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "production"

# Using python -m gunicorn instead of direct gunicorn command for better Windows compatibility
python -m gunicorn --workers 4 --bind 0.0.0.0:5000 wsgi:app