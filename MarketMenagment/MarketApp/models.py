from django.db import models
from django.contrib.auth.models import User

class Vrabotena(models.Model):
    ime=models.CharField(max_length=100)
    prezime=models.CharField(max_length=100)
    EMBG=models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    plata=models.DecimalField(max_digits=5,decimal_places=2)
    # markett = models.OneToOneField("Market", on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f'{self.ime} {self.prezime}'

class Kontakt(models.Model):
    ulica=models.CharField(max_length=100)
    broj=models.IntegerField()
    telefon=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return f'{self.ulica} {self.broj}'

class Proizvod(models.Model):
    VID=[
        ('HR','Hrana'),
        ('PI','Pijalok'),
        ('PK','Kozmetika'),
        ('PP','Pekara'),
        ('HI','Higiena')

    ]
    ime=models.CharField(max_length=100)
    vid=models.CharField(max_length=2,choices=VID)
    domasen=models.BooleanField()
    kod=models.IntegerField()

    def __str__(self):
        return self.ime

class Market(models.Model):
    ime=models.CharField(max_length=100)
    vraboten=models.OneToOneField("Vrabotena", on_delete=models.SET_NULL, null=True, blank=True)
    prozivod=models.ForeignKey(Proizvod, on_delete=models.CASCADE)
    kontakt=models.ForeignKey(Kontakt, on_delete=models.CASCADE)
    broj_na_marketi=models.IntegerField()
    datum_na_otvaranje=models.DateField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    rabotno_vreme_od=models.TimeField()
    rabotno_vreme_do=models.TimeField()

    def __str__(self):
        return self.ime


class MarketVraboten(models.Model):
    market=models.ForeignKey(Market, on_delete=models.CASCADE)
    Vrabotena=models.ForeignKey(Vrabotena, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.market} {self.Vrabotena}'

class MarketProizvod(models.Model):
    market=models.ForeignKey(Market, on_delete=models.CASCADE)
    proizvod=models.ForeignKey(Proizvod, on_delete=models.CASCADE)
    kolicina=models.IntegerField()

    def __str__(self):
        return f'{self.market} {self.proizvod} {self.kolicina}'

