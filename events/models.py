from django.db import models
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField


class Event(models.Model):
    YEAR_CHOICES = []
    for i in range(2019, timezone.now().year + 5):
        YEAR_CHOICES.append((i, i))
    name = models.CharField(max_length=50)
    year = models.IntegerField(default=timezone.now().year, choices=YEAR_CHOICES,
                               null=True, blank=True,
                               help_text='year that event is being held')

    def __str__(self):
        return self.name


class Staff(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, help_text='staff\'s full name', verbose_name='full name')

    team_role_choices = [('arrangement', 'Arrangement'),
                         ('designer', 'Designer'),
                         ('programmer', 'Programmer'),
                         ('talk team', 'Talk Team'),
                         ('others', 'Others'), ]

    role = models.CharField(choices=team_role_choices, max_length=30,
                            help_text='team\'s way of association in team', default='others')

    bio = models.TextField(blank=True, null=True, help_text='description about person e.g. role in team achievements')
    picture = models.ImageField(upload_to='pics/team/', help_text='team\'s picture')
    linkedin_account = models.CharField(max_length=100, null=True, blank=True,
                                        help_text='linkedin.com/in/[User_Account]')
    github_account = models.CharField(max_length=100, null=True, blank=True,
                                      help_text='github.com/[User_Account]')

    def __str__(self):
        return self.name


class Speaker(models.Model):
    event = models.ForeignKey(Event,
                              on_delete=models.CASCADE,
                              help_text='Choose Your Event:')

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('deactive', 'Deactive'),
    ]

    name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='pics/speakers/',
                                default='default.jpg')
    email = models.EmailField()
    phone_number = PhoneNumberField()
    professions = models.TextField(max_length=500)
    account_status = models.CharField(choices=STATUS_CHOICES,
                                      default='deactive', max_length=20)

    def __str__(self):
        return self.name
