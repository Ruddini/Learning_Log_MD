from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Temat poznawany przez użytkownika"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # podłączenie pod użytkownika

    def __str__(self):
        """Zwraca reprezentacje modelu w postaci ciągu tekstowego"""
        return self.text


class Entry (models.Model):
    """Konkretne informacje o postępie w nauce"""
    topic = models.ForeignKey(Topic , on_delete=models.CASCADE) #połączenie każdego wpisuz określonym Topic, po usunięciu
                                                                # Topic, wszystkie wpisy z nim powiązane ostaną usunięte
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries' #jeżeli by tego nie było django używałby formy "Entrys" a nie 'entries'

    def __str__(self):
        """Zwraca reprezentacje w postaci ciągu tekstowego
            Określa które informacje mają być wyświetlone
            po odwołaniu się do poszczególnych wpisów"""
        if len(self.text)>50:
            return f"{self.text[:100]}..."
        else:
            return self.text