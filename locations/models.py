from django.db import models
from districts.models import District

class Location(models.Model):
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        related_name='locations'
    )
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('district', 'name')
        ordering = ['name']

    def __str__(self):
        return f"{self.name}, {self.district.name}"