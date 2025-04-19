from django.db import models

# Create your models here.
class Header(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return self.name
    
class Bullet(models.Model):
    content = models.CharField(max_length=500)
    category = models.ForeignKey(Header, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    
class moreInfo(models.Model):
    content = models.CharField(max_length=500)
    category = models.ForeignKey(Bullet, on_delete=models.CASCADE)

    def __str__(self):
        return self.content