from django.db import models
import uuid
from passlib.hash import pbkdf2_sha256
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
import os
# Create your models here.
from django.utils import timezone


class Dispatcher(models.Model):
   # attributes = JSONField(db_index=True)

    id = models.AutoField(primary_key=True)
    login = models.TextField()
    password = models.TextField()
    email = models.TextField(blank=True, null=True)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def verify_password(self,raw_password):
        return pbkdf2_sha256.verify(raw_password,self.password)
        
    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Categories(models.Model):
   # attributes = JSONField(db_index=True)

    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    picture = models.FileField(null=True)
   

    def verify_password(self,raw_password):
        return pbkdf2_sha256.verify(raw_password,self.password)
        
    def get_fields(self):
        return dict({
            "id" : self.id,
            "name": self.name,
            "description": self.description,
            "picture"  : Categories.objects.filter(id=self.id).values('picture')[0]['picture']
        })

    def get_name(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()



class Brands(models.Model):
   # attributes = JSONField(db_index=True)

    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    logo = models.FileField(blank=True,null=True)
   

    def verify_password(self,raw_password):
        return pbkdf2_sha256.verify(raw_password,self.password)
        

    def get_fields(self):
        return dict({
            "id" : self.id,
            "name": self.name,
            "description": self.description,
            "logo"  : Brands.objects.filter(id=self.id).values('logo')[0]['logo']
        })

    def get_name(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()



class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True,null=True)
    code = models.TextField(blank=True,null=True)
    continent_name = models.TextField(blank=True,null=True)

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def get_continent_name(self):
        return self.continent_name


class Items(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    vender_code = models.TextField(blank=True,null=True)
    manufacturer_code = models.TextField(blank=True,null=True)
    country_of_origin = models.ForeignKey(Country, on_delete=models.CASCADE,related_name="countries",null=True)
    season = models.TextField(blank=True,null=True)
    brands = models.ForeignKey(Brands, on_delete=models.CASCADE,related_name="brands")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,related_name="categorys")

    def save(self, *args, **kwargs):
        super(Items, self).save(*args, **kwargs)



    def get_fields(self):
        return dict({
            "id" : self.id,
            "name": self.name,
            "description": self.description,
            "vender_code": self.vender_code,
            "manufacturer_code": self.manufacturer_code,
            "country_of_origin": self.country_of_origin.get_name(),
            "season" : self.season,
            "brands_name" : self.brands.get_name(),
            "category_name" : self.category.get_name(),
        })


    def get_fields_all(self):
        return dict({
            "id" : self.id,
            "name": self.name,
            "description": self.description,
            "vender_code": self.vender_code,
            "manufacturer_code": self.manufacturer_code,
            "country_of_origin": self.country_of_origin.get_name(),
            "brands" : self.brands.get_fields(),
            "category" : self.category.get_fields(),
        })
 
class ItemsImage(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Items, related_name='image',on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True)


    def get_fields(self):
        return dict({
            "id" : self.id,
        })


class ItemVariant(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Items,related_name="product_variant", on_delete=models.CASCADE)
    name = models.TextField(blank=True,null=True)
    color = models.TextField(blank=True,null=True)
    size = models.TextField(blank=True,null=True)
    price = models.TextField(blank=True,null=True)
    stock = models.TextField(blank=True,null=True)
    vendor = models.ForeignKey(Dispatcher, on_delete=models.CASCADE,related_name="dispatcher",null=True)
    
    def get_fields(self):
        return dict({
            "id" : self.id,
            "name": self.name,
            "color": self.color,
            "size": self.size,
            "price": self.price,
            "stock": self.stock
        })



