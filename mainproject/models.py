from django.db import models
import random, string
import hashlib
import uuid
import datetime


# def get_uid():
#     uid_obj = uuid.uuid4()
#     uid = str(uid_obj.int)
#     return uid


# Create your models here.
class Urlhacked(models.Model):
    original_url = models.URLField(max_length=256)
    short_url = models.CharField(max_length=8, unique=True)

    def __repr__(self):
        self.original_url = original_url
        self.short_url = short_url
