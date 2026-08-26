#!/usr/bin/env bash
# Exit on error
set -o errexit
  
pip install -r requirements.txt && python manage.py collectstatic --noinput 

echo "Running migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Creating default superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()

username = "oyewole"
email = "oyewole@gmail.com"
password = "Panasonic2020@"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created.")
else:
    print("Superuser already exists.")
EOF

echo "Build steps completed."
