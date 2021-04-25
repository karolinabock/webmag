from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=128)


class Film(models.Model):
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField(default="")
    realase_date = models.DateField(null=False, blank=False)
    movielength = models.IntegerField(default=1, )
    poster = models.ImageField(upload_to="images", blank=True)  # ważne żeby podać gdzie ma załadowąć zdjęcie
    director = models.OneToOneField(Director, on_delete=models.CASCADE,
                                    null=True, blank=True)

    def __str__(self):
        return self.title


class Prize(models.Model):
    name = models.CharField(max_length=128)
    film = models.ForeignKey(Film, on_delete=models.CASCADE,
                             related_name="prize")


""""musi być coś w nawiasie, zeby django wiedzial jak stworzyć
    blank = czy pole wymagane
    deflaut = co pisze na początku
    null = jest deflautowo False
    unique = unikalne coś w stylu ID
    choises = lista rzeczy które możemy przypisać do fieldów"""
