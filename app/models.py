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
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='АВТОР')
    like_count = models.IntegerField(default=0,editable=False,blank=False,null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новости '
        verbose_name_plural = 'Новости'
class Comments(models.Model):
    newsObject = models.ForeignKey(News,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True,editable = False)
class NewsImages(models.Model):
    newsObject = models.ForeignKey(News,on_delete=models.CASCADE)
    image = models.ImageField()
    def __str__(self):
        return self.newsObject
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Новости Фото'
class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()



class NewsDetails(models.Model):
    newsobject = models.ForeignKey(News,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()
    def __str__(self):
        return f"{self.newsobject.title} - {self.title}"

class Admins(models.Model):
    selectedUser = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,unique=True)
    


