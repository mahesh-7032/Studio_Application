from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    shoot_location = models.CharField(max_length=255)
    preferred_date = models.DateField()
    additional_requirements = models.TextField()

    def __str__(self):
        return self.name


