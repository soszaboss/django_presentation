from django.db import models
import pycountry

all_countries = list(pycountry.countries)
list_all_countries_and_code = [(country.alpha_2, country.name) for country in all_countries]

class Authors(models.Model):
    fullname = models.CharField(max_length=100, null=False)
    birth_date = models.DateField(null=False)
    nationality = models.CharField(max_length=100, choices=list_all_countries_and_code)

    class Meta:
        verbose_name_plural = 'authors'
    
    def __str__(self):
        return self.fullname

class Books(models.Model):
    title = models.CharField(max_length=100, null=False)
    isbn = models.CharField(max_length=100, null=False, unique=True)
    publication_date = models.DateField(null=False)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'books'

    def author_fullname(self):
        return self.author.fullname if self.author else ''
    
    def __str__(self):
        return self.title
