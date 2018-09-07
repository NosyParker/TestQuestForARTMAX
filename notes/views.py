from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Note
from .forms import NoteForm


def notes(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.publish()
            note.save()
        else:
            note = NoteForm()

    notes = Note.objects.filter(published_date__lte = timezone.now()).order_by('published_date')

    paginator = Paginator(notes, 5)
    page = request.GET.get('page')

    try:
        notes = paginator.get_page(page)
    except PageNotAnInteger:
        notes = paginator.get_page(1)
    except EmptyPage:
        notes = paginator.get_page(paginator.num_pages)

    return render(request, 'notes/notes_list.html', {'form': form, 'notes':notes})


def note_selected(request, pk):
    note = get_object_or_404(Note, pk=pk)
    
    return render(request, 'notes/note_selected.html', {'note': note})


