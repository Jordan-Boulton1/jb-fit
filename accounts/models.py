from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

# Create your models here.

class UserProfile(models.Model):
    """
    User profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_images/', blank=True)
    gender = models.CharField(
        max_length=10, choices=[
            ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    date_of_birth = models.DateField(blank=True, null=True)
    current_weight = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    goal_weight = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class WeightLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.weight} kg on {self.entry_date.strftime('%Y-%M-%D')}"