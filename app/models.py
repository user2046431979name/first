from django.db import models
from django.utils import timezone

class News(models.Model):
    title  = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    main_img = models.ImageField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,editable = False)

    def __str__(self):
        return self.title
    