from .models import Note
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, NoteForm
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'notetaker_app/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')    
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegisterForm()
    return render(request, 'notetaker_app/registration.html', {'form': form})


@login_required
def user_notes(request):
    notes = Note.objects.filter(user=request.user)  # Get notes for the logged-in user
    return render(request, 'notetaker_app/user_notes.html', {'notes': notes})


@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # Set the note's user to the current user
            note.save()
            return redirect('user_notes')  # Redirect to the list of notes after creation
    else:
        form = NoteForm()

    return render(request, 'notetaker_app/note_create.html', {'form': form})


class NoteUpdateView(UpdateView):
    model = Note
    fields = ['theme', 'text']
    template_name = 'notetaker_app/note_edit.html'
    success_url = reverse_lazy('user_notes')  # Redirect to the note list view after editing

    def get_queryset(self):
        # Only allow editing notes that belong to the current user
        return super().get_queryset().filter(user=self.request.user)

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notetaker_app/note_delete.html'
    success_url = reverse_lazy('user_notes')  # Redirect to the note list view after deleting

    def get_queryset(self):
        # Only allow deleting notes that belong to the current user
        return super().get_queryset().filter(user=self.request.user)

