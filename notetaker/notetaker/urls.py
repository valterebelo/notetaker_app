from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from notetaker_app.views import register, home, user_notes, note_create, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='notetaker_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register, name='create_account'),
    path('notes/user/', user_notes, name='user_notes'),
    path('notes/create', note_create, name='note_create'),
    path('notes/<int:pk>/edit/', NoteUpdateView.as_view(), name='note_edit'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
]
