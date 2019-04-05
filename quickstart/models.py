from django.conf import settings
from django.db import models
from django.utils import timezone
from jsonfield import JSONField
from passlib.hash import pbkdf2_sha256
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
import os
import uuid

class Client(models.Model):
   # attributes = JSONField(db_index=True)

    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True,null=True)
    lastname = models.TextField(blank=True,null=True)
    image = models.FileField(blank=True,null=True)
    login = models.TextField()
    active = models.TextField(default=0)
    email = models.TextField(blank=True,null=True)
    isModel = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def verify_password(self,raw_password):
        return pbkdf2_sha256.verify(raw_password,self.password)
        
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_name(self):
        return self.name


@receiver(models.signals.post_delete, sender=Client)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Client` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=Client)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Client` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Client.objects.get(pk=instance.pk).image
    except Client.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file and old_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)