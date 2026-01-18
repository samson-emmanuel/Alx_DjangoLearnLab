from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Function to check if user is Admin
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Function-based Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
