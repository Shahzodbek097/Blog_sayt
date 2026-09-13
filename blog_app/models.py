from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.

class Avtor(models.Model):
    ism=models.CharField(max_length=10,blank=True,null=True)
    yosh=models.SmallIntegerField()
    link=models.URLField(null=True)

    def __str__(self):
        return self.ism

class Janri(models.Model):
    janr_nomi=models.CharField(max_length=10)

    def __str__(self):
        return self.janr_nomi


class Kitoblar(models.Model):
    nomi=models.CharField(max_length=15)
    avtor=models.ForeignKey(Avtor,null=True,on_delete=models.CASCADE)
    janr=models.ForeignKey(Janri,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.nomi

class Post(models.Model):
    sarlavha=models.CharField(max_length=100)
    slag=models.SlugField(max_length=255,default=True,blank=True,null=True)
    matni=models.TextField()
    avtor=models.ForeignKey(Avtor,null=True,on_delete=models.CASCADE)
    chop_etish_sana=models.DateTimeField(default=timezone.now)  #Admin panelda ko'rsatadi, hozirgi vaqt va o'zgartirsa bo'ladi
    yaratish_sana=models.DateTimeField(auto_now_add=True)       #Adminda ko'rinmaydi, yaratilgan vaqt va o'zgartirib bo'lmaydi
    ozgarish_sana=models.DateTimeField(auto_now=True)           #Adminda ko'rinmaydi, o'zgartirilgan vaqt va o'zgartirib bo'lmaydi

    def __str__(self):
        return self.sarlavha

    def saqlash(self,*args,**kwargs):
        if not self.slag:
            self.slag=slugify(self.sarlavha)
        super().save(*args,**kwargs)


