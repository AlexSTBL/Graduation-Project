from django.conf import settings
from django.db import models


# Create your models here.

class Table(models.Model):
    Tables = (

        ('Single', 'Single'),
        ('Small', 'Two-Seats'),
        ('Medium', 'Four-Seats'),
        ('Large', 'Six-Seats'),

    )
    number = models.IntegerField()
    category = models.CharField(max_length=6, choices=Tables)
    seats = models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.category} with {self.seats} seats'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, auto_now_add=False)

    # def save(self, *args, **kwargs):
    #    if not self.pk and not self.check_out:
    #        check_in_datetime = datetime.combine(self.check_in_date, self.check_in_time)
    #        self.check_out = check_in_datetime + timedelta(hours=2)
    #    super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user} has booked {self.table} from {self.check_in} to {self.check_out}'
