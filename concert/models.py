from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)


class Venue(models.Model):
    venue_id = models.PositiveIntegerField(default=0)
    venue_title = models.CharField(max_length=50)
    venue_adress = models.CharField(max_length=150)
    region = models.PositiveIntegerField(default=0)

class Ivents(models.Model):
    ivent_id = models.PositiveIntegerField(default=0)
    date_times = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    venue_id = models.ManyToManyField(Venue)

class Artist(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Ivents = models.ManyToManyField(Ivents)

class Ticket(models.Model):
    ticket_id = models.PositiveIntegerField(default=0)
    ivent_id = models.OneToOneField(Ivents, on_delete=models.CASCADE)
    ovner = models.OneToOneField(Person, on_delete=models.CASCADE)
    order_id = models.PositiveIntegerField(default=0)
    row = models.PositiveIntegerField(default=0)
    number = models.PositiveIntegerField(default=0)

class Sector(models.Model):
    ticket_id = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=30)

class Sounds(models.Model):
    title = models.CharField(max_length=100)
    artist = models.OneToOneField(Artist, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

rates = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

class Rate(models.Model):
    ovner = models.OneToOneField(Person, on_delete=models.CASCADE)
    artist = models.OneToOneField(Artist, on_delete=models.CASCADE)
    value = models.PositiveIntegerField(choices = rates)

class Session(models.Model):
    session_id = models.PositiveIntegerField(default=0)
    friend = models.ForeignKey(Person, on_delete=models.CASCADE)
