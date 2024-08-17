from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()

    def __str__(self):
        return self.name
    
class Place(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    capacity = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    from_date = models.DateField()
    to_date = models.DateField()
    reservant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations", default=1)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="reservations", default=1)