from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    profile_photo = models.ImageField(upload_to='media/')
    bio = models.TextField() 
 

    def __str__(self):
        return self.bio 

    def save_profile(self):
        self.save()

    def del_profile(self):
        self.delete()      
class Images(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    actual_image = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=60) 
    caption = models.TextField()
    comments = models.TextField() 
    created_time = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.name 

    def save_image(self):
        self.save()

    def del_image(self):
        self.delete()

    @classmethod
    def search_by_name(cls,search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images
    


    

  