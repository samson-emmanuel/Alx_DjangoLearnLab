from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView

def is_librarian(user):
    """Function to check if a user has the 'Librarians' role."""
    from .models import UserProfile
    try:
        return user.is_authenticated and user.userprofile.role == 'Librarians'
    except UserProfile.DoesNotExist:
        return False

class LibrarianView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """
    A view for users with the 'Librarian' role.
    """
    template_name = 'relationship_app/librarian_view.html'

    def test_func(self):
        """The test function for the UserPassesTestMixin."""
        return is_librarian(self.request.user)

# Keep the function-based view for reference or if the CBV doesn't work.
# from django.shortcuts import render
# from django.contrib.auth.decorators import user_passes_test
#
# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')