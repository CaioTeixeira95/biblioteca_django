from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Books(models.Model):

    ACTION = 'ac'
    ADVENTURE = 'ad'
    HORROR = 'h'
    THRILLER = 'th'
    DRAMA = 'd'
    COMEDY = 'c'
    MANGA = 'm'
    COMICS = 'co'

    GENDER_CHOICES = [
        (ACTION, 'action'),
        (ADVENTURE, 'adventure'),
        (HORROR, 'horror'),
        (THRILLER, 'thriller'),
        (DRAMA, 'drama'),
        (COMEDY, 'comedy'),
        (MANGA, 'manga'),
        (COMICS, 'comics'),
    ]

    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=ADVENTURE)  # NOQA
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    author = models.CharField(max_length=100)
    reg_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.title


class Loan(models.Model):

    id_book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='books')  # NOQA
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')  # NOQA
    loan_date = models.DateField(auto_now=True)
    devolution_date = models.DateField()
    is_devolved = models.BooleanField(default=False)

    class Meta:
        db_table = 'loan'
