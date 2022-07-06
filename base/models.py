from django.db import models


# Create your models here.
class slider(models.Model):
    image = models.ImageField(upload_to="slider_img")


class about(models.Model):
    image = models.ImageField(upload_to="about_img")
    about_text = models.CharField(max_length=2000)

    def __str__(self):
        return self.about_text


class category(models.Model):
    image = models.ImageField(upload_to="Cat_img")
    text_cat = models.CharField(max_length=20)

    def __str__(self):
        return self.text_cat


class product(models.Model):
    image = models.ImageField(upload_to="products_img")
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class advantage(models.Model):
    image = models.ImageField(upload_to="advantage_image")
