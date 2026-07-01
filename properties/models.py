from django.db import models
from districts.models import District
from locations.models import Location


class Property(models.Model):

    PROPERTY_TYPES = [
        ('HOUSE', 'House'),
        ('APARTMENT', 'Apartment'),
        ('HOSTEL', 'Hostel'),
        ('ROOM', 'Rental Room'),
        ('COMMERCIAL', 'Commercial Building'),
    ]

    PURPOSE_CHOICES = [
        ('BUY', 'Buy'),
        ('RENT', 'Rent'),
    ]

    STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('SOLD', 'Sold'),
        ('RENTED', 'Rented'),
    ]

    title = models.CharField(max_length=200)

    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPES
    )

    purpose = models.CharField(
        max_length=10,
        choices=PURPOSE_CHOICES
    )

    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )

    address = models.TextField()

    description = models.TextField()

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    owner_name = models.CharField(max_length=150)

    phone = models.CharField(max_length=15)

    whatsapp = models.CharField(
        max_length=15,
        blank=True
    )

    bedrooms = models.PositiveIntegerField(default=0)

    bathrooms = models.PositiveIntegerField(default=0)

    area_sqft = models.PositiveIntegerField()

    land_area = models.CharField(
        max_length=100,
        blank=True
    )

    furnished = models.BooleanField(default=False)

    parking = models.BooleanField(default=False)

    google_map_link = models.URLField(
        blank=True,
        null=True,
        verbose_name="Google Maps Link")

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='AVAILABLE'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class PropertyImage(models.Model):

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(
        upload_to='properties/'
    )

    def __str__(self):
        return self.property.title