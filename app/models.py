from django.db import models
from django.utils import timezone
from django.conf import settings
class News(models.Model):
    title  = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    main_img = models.ImageField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,editable = False)
    counter = models.IntegerField(editable=False,default=0,blank=True,null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)



    def __str__(self):
        return self.title
    
class NewsImages(models.Model):
    newsObject = models.ForeignKey(News,on_delete=models.CASCADE)
    image = models.ImageField()
    def __str__(self):
        return self.newsObject
    
class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    
