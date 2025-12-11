from django.db import models

# Create your models here.
class Reservation(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    reserved_by = models.ForeignKey(
        to='users.User',
        related_name='reservations_held',
        on_delete=models.CASCADE
    )
    reserved_room =models.ForeignKey(
        to='rooms.room',
        related_name='reservations',
        on_delete= models.CASCADE
    )
    cost = models.DecimalField(max_digits=9,decimal_places=2)
    reserved_on = models.DateTimeField(auto_now_add=True)
