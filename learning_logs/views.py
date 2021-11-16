from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect , Http404

def index(request):
    """Strona główna dla aplikacji learning_logs"""
    return render(request, 'learning_logs/index.html')

@login_required #dzięki temu tylko zalogowani użytkownicy bedą mieli dostęp do wyświetlania tematów
                #jeżeli użytkownik chce wyśwuetlić strone zostanie przeniesiony do strony logowania
def topics(request):
    """Wyświetlanie wszystkich tematów"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')    #zapytanie do bazy danych
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Wyświetla pojeyńczy temat i wszystkie związane z nim wbisy"""
    topic = get_object_or_404(Topic, id=topic_id)

    #upewnienie się że temat należy do danego użytkownika
    check_topic_owner(topic, request)

    entries = topic.entry_set.order_by('-date_added')   # '-' oznacza odwrotną kolejność
    context = {'topic': topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Dodaj nowy temat"""

    #Nie przekazano żadnych danych, należy otworzyć pusty formularz
    if request.method != 'POST':
        form = TopicForm()

    #Przekazano dane za pomocą metody POST
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics') #przekierowuje użytkownika do zakładki topics kiedy dodaj już swój topic

    #wyświetlenie pustego formularza
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html',context)


@login_required
def new_entry(request,topic_id):
    """Dodaje nowy wpis do określonego tematu"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #Nie przekazano żadnych danych, utworzenie nowego formularza
        form = EntryForm()

    else:
        form = EntryForm(data=request.POST)
        check_topic_owner(topic, request)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic',topic_id = topic_id)

    #Wyświetlanie pustego formularza
    context = {'topic' : topic, 'form' : form}
    return render(request, 'learning_logs/new_entry.html',context)


@login_required
def edit_entry(request, entry_id):
    """Edycja istniejącego wpisu"""

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    check_topic_owner(topic, request)

    if request.method!= "POST":
        #żądanie początkowe
        form = EntryForm(instance=entry)
    else:
        #żądanie które należy przetworzyć
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)
    context = {"entry": entry, "topic":topic, 'form' :form}
    return render(request,'learning_logs/edit_entry.html',context)

#upewnienie się że temat należy do danego użytkownika
def check_topic_owner(topic, request):
    if topic.owner != request.user:
        raise Http404 #generowanie wyjątku HTTP 404

