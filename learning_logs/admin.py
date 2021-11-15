from django.contrib import admin

from .models import Topic, Entry #importowanie z models.py ( '.' działa tylko jeżeli znajduje się w tym samym katalogu)

admin.site.register(Topic) #umożliwia zarządzanie tym modelem przez witrynę administracyjną
admin.site.register(Entry)
