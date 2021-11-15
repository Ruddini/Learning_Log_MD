from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):

    class Meta:
    #Klasa Meta wskazuje Model dla formularza
        model = Topic   # model będący podstawą dla formularza
        fields = ['text']   #uwzględnieie w formularzu liste kolumn 'text'
        labels = {'text':''} # dla kolumny 'text' nie powinna być generowana etykieta

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text' : ''}
        widgets = {'text': forms.Textarea(attrs={'col' : 80 })} #poszerzenie kolumy text do
