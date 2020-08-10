from django.db import models

# Create your models here.
class Images(models.Model):
    actual_image = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=60)
    caption = models.TextField()
    comments = models.TextField() 

    def __str__(self):
        return self.name 

    def save_image(self):
        self.save()

    def del_image(self):
        self.delete()




class Profile(models.Model):
    
    profile_photo = models.ImageField(upload_to='media/')
    bio = models.TextField()  

    def __str__(self):
        return self.bio 

    def save_profile(self):
        self.save()

    def del_profile(self):
        self.delete()        