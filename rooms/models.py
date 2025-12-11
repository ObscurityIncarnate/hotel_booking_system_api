from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Room(models.Model):
    class RoomTypes(models.TextChoices):
        CLASSIC = "Classic Suite"
        SUPREME = "Supreme Suite"
        DELUXE = "Deluxe Suite"
        EXECUTIVE = "Executive Suite"
        SUPER_EXECUTIVE = "Super Executive Suite"
        SELF_CAT_EXECUTIVE = "Self Catering Execuitve Suite"
    branchId = models.ForeignKey(
        to='branches.branch',
        related_name="branch_rooms",
        on_delete= models.CASCADE,
    )
    price_per_night = models.DecimalField(max_digits=5, decimal_places=2)
    max_guests = models.IntegerField()
    type = models.CharField(
        max_length= 50,
        choices= RoomTypes,
        default= RoomTypes.CLASSIC
    )
    images = ArrayField(
        models.URLField(),
        size=8,
        default=list
    )
    description = models.CharField(max_length=1000)