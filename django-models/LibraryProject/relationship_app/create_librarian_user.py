import os
import sys
from pathlib import Path
import django

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from django.contrib.auth.models import User
from relationship_app.models import UserProfile

def create_librarian(username, password, email):
    """
    Creates a new user and assigns them the 'Librarian' role.
    """
    if User.objects.filter(username=username).exists():
        print(f"User '{username}' already exists.")
        user = User.objects.get(username=username)
    else:
        user = User.objects.create_user(username=username, password=password, email=email)
        print(f"Created user: '{username}'")

    # Set user role to 'Librarian'
    # The UserProfile is created automatically with the 'Member' role.
    # We need to update it.
    try:
        user.userprofile.role = 'Librarian'
        user.userprofile.save()
        print(f"User '{username}' role updated to 'Librarian'.")
    except UserProfile.DoesNotExist:
        print(f"UserProfile for '{username}' not found. A UserProfile should be created automatically.")

if __name__ == '__main__':
    # Replace with desired credentials for the librarian user
    create_librarian('librarian_user', 'strongpassword123', 'librarian@example.com')
