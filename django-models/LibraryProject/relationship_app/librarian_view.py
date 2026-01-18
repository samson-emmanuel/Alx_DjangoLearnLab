from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Function to check if user is a Librarian
def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# Function-based Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
