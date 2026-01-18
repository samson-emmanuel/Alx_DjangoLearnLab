from django.urls import path

from LibraryProject.bookshelf import views
from LibraryProject.relationship_app.admin import admin_view
from .views import list_books, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView
from . import librarian_view

urlpatterns = [
path('books/', list_books, name='list_books'),
path('library/[int:pk](int:pk)/', LibraryDetailView.as_view(), name='library_detail'),
path('register/', views.register, name='register'),  # <- matches "views.register"
path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
path('admin-view/', admin_view.admin_view, name='admin_view'),
 path('librarian-view/', librarian_view.librarian_view, name='librarian_view'),
]