"""Definiuje wzorce adresów URL dla learning_logs."""

from django.urls import path

from . import views     #'.' to importowanie widoków z tego samego katalogu

app_name = 'learning_logs'  # pomaga w odróżnieniu plików z innych katalogów o tej samej nazwie
                            # przestrzeń nazw do której odwołuje się bazowy html

urlpatterns = [ #lista ston które mogą być żądane od aplikacji learning_logs
    #Strona główna
    path('',views.index, name='index'),
    # Wyświetlanie wszystkich tematów
    path('topics/',views.topics, name='topics'),
    # Strona szczegółowa dotycząca pojedyńczego tematu
    path('topics/(<int:topic_id>)/',views.topic, name='topic'), # /(<int:topic_id>)/ dopasowanie liczby całowitej
                                                                  # znajdującej się za słowem topics i przypisanie do zmiennej topic_id
    #Strona przeznaczona do dodawania nowego Topicu
    path('new_topic/', views.new_topic, name='new_topic'),
    #Srona przeznaczona do dodawania nowego wpisu
    path('new_entry/(<int:topic_id>)/',views.new_entry, name='new_entry'),

    #Strona do edycji wpisu
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]

