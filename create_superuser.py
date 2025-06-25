import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thalapathytransport.settings')  # Adjust this if your settings module is named differently
django.setup()

from django.contrib.auth import get_user_model

def create_superuser():
    User = get_user_model()

    username = 'natesh'
    email = 'natesh@gmail.com'
    password = 'natesh1499'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser '{username}' created successfully.")
    else:
        print(f"Superuser '{username}' already exists.")

if __name__ == '__main__':
    create_superuser()
