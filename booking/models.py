from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    tel_num = models.CharField(max_length=9)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Visit(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField

    def __str__(self):
        return self.name

class Booking(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    dt = models.DateTimeField()

    def __str__(self):
        return self.person.name + ' : ' + self.place.name + ' : ' + str(self.dt) + ' : ' + self.visit.name
