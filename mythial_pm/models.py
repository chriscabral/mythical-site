from django.db import models
from django.contrib.auth.models import User
from mezzanine.pages.models import Page

# class Project(Page):
#     name = models.CharField(max_length=200)
#     owner = models.ForeignKey(User, editable=False)
#     has_been_created = models.BooleanField(default=False)
#     is_on = models.BooleanField(default=False)
#     public_dns = models.CharField(max_length=500)
#     private_key = models.CharField(max_length=1000)
    