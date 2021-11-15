from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Rejestracja nowego użytkownika"""

    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()  #zwraca nowo-utworzony obiekt użytkownika

            #Zalogowanie użytkownika i przekierowanie go na stronę główną
            login(request, new_user)    #funckja pozwalająca na zalogowanie się po podaniu prawidłowych danych
            return redirect('learning_logs:index')
    context={'form':form}
    return render(request, 'registration/register.html',context)

# Create your views here.
