from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)  # Ensure this field is defined correctly

    def __str__(self):
        return f"Message from {self.name}"

class UserImages(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    face_image=models.ImageField(upload_to="user_faces/")

    def __str__(self):
        return self.user.username


